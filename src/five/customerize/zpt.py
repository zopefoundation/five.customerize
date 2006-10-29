from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate

class TTWTemplate(ZopePageTemplate):
    """A template class used to generate Zope 3 views TTW"""

    def __init__(self, id, text=None, content_type=None, encoding='utf-8',
                 strict=False, view=None):
        self.view = view
        super(TTWTemplate, self).__init__(id, text, content_type, encoding,
                                          strict)

    def __call__(self, context, request):
        return TTWTemplateRenderer(context, request, self, self.view)


class TTWTemplateRenderer(object):
    def __init__(self, context, request, template, view):
        self.context = context
        self.request = request
        self.template = template
        self.view = view

    def __call__(self, *args, **kwargs):
        """Add the zope user to the security context, as done in
        PageTemplateFile"""
        view = self.view
        if view is not None:
            class TTWView(view):
                __allow_access_to_unprotected_subobjects__ = 1
            view = TTWView(self.context, self.request)
        bound_names = {'view': view,
                       'request': self.request,
                       'context': self.context}
        template = self.template.__of__(self.context)
        return template._exec(bound_names, args, kwargs)

    def __of__(self, obj):
        return self
