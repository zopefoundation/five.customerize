from Products.PageTemplates.PageTemplateFile import PageTemplateFile as Z2PTF
from zope.pagetemplate.pagetemplatefile import PageTemplateFile as Z3PTF
from zope.app.pagetemplate.viewpagetemplatefile import BoundPageTemplate


def isTemplate(obj):
    """ check if the given object is a or is derived from a template class """
    # TODO: we should really check via interfaces, i.e. `providedBy` here,
    #       but the only class using interfaces atm is Z3PTF :(
    return isinstance(obj, Z2PTF) or isinstance(obj, Z3PTF) or \
        isinstance(obj, BoundPageTemplate)


def findViewletTemplate(viewlet):
    """ try to find the attribute holding the template within a viewlet """
    for attr in 'index', 'template', '__call__', 'render':
        item = getattr(viewlet, attr, None)
        if isTemplate(item):
            return attr, item
    attrs = [ attr for attr in dir(viewlet) if isTemplate(getattr(viewlet, attr, None)) ]
    if len(attrs) == 1:
        return attrs[0], getattr(viewlet, attrs[0])
    else:
        # TODO: we should pass on the message if we find multiple templates
        pass
    return None, None

