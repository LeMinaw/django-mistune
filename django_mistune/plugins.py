class HeaderLevels:
    def __init__(self, top=3):
        """Demotes all the headers of the document so the first level becomes
        the `top` parameter.

        This changes both the AST and the rendering of the document.
        """
        self.top = top
        assert top > 0, "Top level must be >= 1"

    def replace_level(self, token):
        """Replace the level of a heading token."""
        level = token["params"][0]
        token["params"] = (level + self.top - 1,)

    def find_headings(self, md, tokens, state):
        """Walk the token tree and search for heading tokens."""
        for tok in tokens:
            if tok["type"] == "heading":
                self.replace_level(tok)
            if "children" in tok.keys():
                self.find_headings(tok["children"])
        return tokens

    def __call__(self, md):
        md.before_render_hooks.append(self.find_headings)


class AddClasses:
    def __init__(self, tags=None):
        """Add HTML classes to all given HTML tags.

        For example, `tags={'p': ('a', 'b'), 'em': 'a'}` will add the `a` class
        to `p` and `em` tags of the document, and the `b` class to `p` tags.

        This only alters the rendering of the document, not its AST.
        """
        self.tags = tags or {}

    def add_classes(self, md, result, state):
        """Find bare HTML tags and add classes to them."""
        for tag, classes in self.tags.items():
            if not isinstance(classes, tuple):
                classes = (classes,)

            result = result.replace(
                f"<{tag}>", f"<{tag} class=\"{' '.join(classes)}\">"
            )

        return result

    def __call__(self, md):
        if md.renderer.NAME == "html":
            md.after_render_hooks.append(self.add_classes)
