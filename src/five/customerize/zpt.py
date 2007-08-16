import zope.component
from AccessControl import getSecurityManager
from AccessControl import Unauthorized

from zope.viewlet.viewlet import ViewletBase
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate
from zope.app.container.interfaces import IObjectRemovedEvent
from zope.viewlet.interfaces import IViewlet, IViewletManager
from zope.interface import implements

from five.customerize.interfaces import ITTWViewTemplate


class TTWViewTemplate(ZopePageTemplate):
    """A template class used to generate Zope 3 views TTW"""
    implements(ITTWViewTemplate)

    manage_options = (
        ZopePageTemplate.manage_options[0],
        dict(label='Registrations', action='registrations.html'),
        ) + ZopePageTemplate.manage_options[2:]

    def __init__(self, id, text=None, content_type='text/html', strict=True,
                 encoding='utf-8', view=None, permission=None):
        self.view = view
        self.permission = permission
        super(TTWViewTemplate, self).__init__(id, text, content_type, encoding,
                                              strict)

    def __call__(self, context, request, viewlet=None, manager=None):
        #XXX raise a sensible exception if context and request are
        # omitted, IOW, if someone tries to render the template not as
        # a view.
        sm = getSecurityManager()
        if self.permission:
            if not sm.checkPermission(self.permission, context):
                raise Unauthorized('The current user does not have the '
                                   'required "%s" permission'
                                   % self.permission)
        if IViewletManager.providedBy(manager):
            return TTWViewletRenderer(context, request, self, self.view,
                viewlet, manager)
        else:
            return TTWViewTemplateRenderer(context, request, self, self.view)

    # overwrite Shared.DC.Scripts.Binding.Binding's before traversal
    # hook that would prevent to look up views for instances of this
    # class.
    def __before_publishing_traverse__(self, self2, request):
        pass

class TTWViewTemplateRenderer(object):
    """The view object for the TTW View Template.

    When a TTWViewTemplate-based view is looked up, an object of this
    class is instantiated.  It holds a reference to the
    TTWViewTemplate object which it will use in the render process
    (__call__).
    """

    def __init__(self, context, request, template, view):
        self.context = context
        self.request = request
        self.template = template
        self.view = view

    def __call__(self, *args, **kwargs):
        """Render the TTWViewTemplate-based view.
        """
        view = self._getView()
        # we need to override the template's context and request as
        # they generally point to the wrong objects (a template's
        # context usually is what it was acquired from, which isn't
        # what the context is for a view template).
        bound_names = {'context': self.context,
                       'request': self.request,
                       'view': view}
        template = self.template.__of__(self.context)
        return template._exec(bound_names, args, kwargs)

    def _getView(self):
        view = self.view
        if view is not None:
            # Filesystem-based view templates are trusted code and
            # have unrestricted access to the view class.  We simulate
            # that for TTW templates (which are trusted code) by
            # creating a subclass with unrestricted access to all
            # subobjects.
            class TTWView(view):
                __allow_access_to_unprotected_subobjects__ = 1
            view = TTWView(self.context, self.request)
        return view

    # Zope 2 wants to acquisition-wrap every view object (via __of__).
    # We don't need this as the TTWViewTemplate object is already
    # properly acquisition-wrapped in __call__.  Nevertheless we need
    # to support the __of__ method as a no-op.
    def __of__(self, obj):
        return self


class TTWViewletRenderer(object):
    """ analogon to TTWViewTemplateRenderer for viewlets """
    implements(IViewlet)

    __allow_access_to_unprotected_subobjects__ = True

    def __init__(self, context, request, template, view, viewlet=None, manager=None):
        self.context = context
        self.request = request
        self.template = template
        self.view = view
        self.viewlet = viewlet
        self.manager = manager
        self.ttwviewlet = None

    def update(self):
        """ update the viewlet before `render` is called """
        view = self._getViewlet().update()

    def render(self, *args, **kwargs):
        """ render the viewlet using the customized template """
        view = self._getViewlet()
        # we need to override the template's context and request as
        # they generally point to the wrong objects (a template's
        # context usually is what it was acquired from, which isn't
        # what the context is for a view template).
        bound_names = {'context': self.context,
                       'request': self.request,
                       'view': view}
        template = self.template.__of__(self.context)
        return template._exec(bound_names, args, kwargs)

    def _getViewlet(self):
        if self.ttwviewlet is not None:
            return self.ttwviewlet
        view = self.view
        if view is not None:
            # Filesystem-based view templates are trusted code and
            # have unrestricted access to the view class.  We simulate
            # that for TTW templates (which are trusted code) by
            # creating a subclass with unrestricted access to all
            # subobjects.
            class TTWViewlet(view, ViewletBase):
                __allow_access_to_unprotected_subobjects__ = 1
            view = TTWViewlet(self.context, self.request, self.viewlet, self.manager)
        self.ttwviewlet = view
        return view

    # Zope 2 wants to acquisition-wrap every view object (via __of__).
    # We don't need this as the TTWViewTemplate object is already
    # properly acquisition-wrapped in __call__.  Nevertheless we need
    # to support the __of__ method as a no-op.
    def __of__(self, obj):
        return self


@zope.component.adapter(TTWViewTemplate, IObjectRemovedEvent)
def unregisterViewWhenZPTIsDeleted(zpt, event):
    components = zope.component.getSiteManager(zpt)
    for reg in components.registeredAdapters():
        if reg.factory == zpt:
            components.unregisterAdapter(reg.factory, reg.required,
                                         reg.provided, reg.name)
            break
