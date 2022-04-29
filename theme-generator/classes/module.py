class Module:
    """
    Create a new module
    @param name string Module name
    @param gen_template function Return a template content
    """
    def __init__(self, name, gen_template):
        self.name = name
        self.gen_template = gen_template
