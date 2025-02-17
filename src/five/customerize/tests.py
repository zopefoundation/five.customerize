import doctest
import unittest

from plone.testing import Layer
from plone.testing import layered
from plone.testing import zca
from plone.testing import zope

from Products.Five.browser import BrowserView
from zope.configuration import xmlconfig


class FiveCustomerizeLayer(Layer):
    defaultBases = (zope.STARTUP,)

    def setUp(self):
        # Stack a new configuration context
        self['configurationContext'] = context = zca.stackConfigurationContext(
            self.get('configurationContext'))

        import Products.Five

        import five.customerize
        xmlconfig.file('configure.zcml', Products.Five, context=context)
        xmlconfig.file('configure.zcml', five.customerize, context=context)

    def tearDown(self):
        # Zap the stacked configuration context
        del self['configurationContext']


FIVE_CUSTOMERIZE_FIXTURE = FiveCustomerizeLayer()

FIVE_CUSTOMERIZE_FUNCTIONAL_TESTING = zope.FunctionalTesting(
    bases=(FIVE_CUSTOMERIZE_FIXTURE,), name="five.customerize:FUNCTIONAL")


class TestView(BrowserView):
    """A view class"""
    __name__ = 'mystaticview.html'

    def foo_method(self):
        return 'baz'

    def __call__(self):
        return 'Original View'


def test_suite():
    return unittest.TestSuite([
        layered(
            doctest.DocFileSuite('zpt.txt'),
            layer=FIVE_CUSTOMERIZE_FUNCTIONAL_TESTING,
        ),
        layered(
            doctest.DocFileSuite(
                'customerize.txt',
            ),
            layer=FIVE_CUSTOMERIZE_FUNCTIONAL_TESTING,
        ),
        layered(
            doctest.DocFileSuite('browser.txt', globs={
                'TestView': TestView,
            }),
            layer=FIVE_CUSTOMERIZE_FUNCTIONAL_TESTING,
        ),
    ])
