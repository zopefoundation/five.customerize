from zope.interface import Interface


class ITTWViewTemplate(Interface):
    """ ttw customizable page template view """

    def __call__(context, request):
        """ render the template/view """

