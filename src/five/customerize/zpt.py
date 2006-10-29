import zope.component
from AccessControl import getSecurityManager
from AccessControl import Unauthorized

from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate
from zope.app.container.interfaces import IObjectRemovedEvent

class TTWTemplate(ZopePageTemplate):
    """A template class used to generate Zope 3 views TTW"""

    def __init__(self, id, text=None, content_type=None, encoding='utf-8',
                 strict=False, view=None, permission=None):
        self.view = view
        self.permission = permission
        super(TTWTemplate, self).__init__(id, text, content_type, encoding,
                                          strict)

    def __call__(self, context, request):
        sm = getSecurityManager()
        if self.permission:
            allowed = sm.checkPermission(self.permission, context)
            if not allowed:
                raise Unauthorized, 'The current user does not have the '\
                      'required "%s" permission'%self.permission
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
        view = self._getView()
        bound_names = {'view': view,
                       'request': self.request,
                       'context': self.context}
        template = self.template.__of__(self.context)
        return template._exec(bound_names, args, kwargs)

    def _getView(self):
        view = self.view
        if view is not None:
            class TTWView(view):
                __allow_access_to_unprotected_subobjects__ = 1
            view = TTWView(self.context, self.request)
        return view

    def __of__(self, obj):
        return self

@zope.component.adapter(TTWTemplate, IObjectRemovedEvent)
def unregisterViewWhenZPTIsDeleted(zpt, event):
    components = zope.component.getSiteManager(zpt)
    for reg in components.registeredAdapters():
        if reg.factory == zpt:
            break
    components.unregisterAdapter(reg.factory, reg.required, reg.provided,
                                 reg.name)
