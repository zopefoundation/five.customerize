import unittest
from Testing.ZopeTestCase import ZopeDocFileSuite
from Testing.ZopeTestCase import FunctionalDocFileSuite
from zope.traversing.adapters import DefaultTraversable
import zope.component.testing

__docformat__ = "reStructuredText"

def setUp(test):
    zope.component.testing.setUp(test)
    zope.component.provideAdapter(DefaultTraversable, (None,))

def test_suite():
    return unittest.TestSuite([
        ZopeDocFileSuite('zpt.txt', package="five.customerize",
                         setUp=setUp, tearDown=zope.component.testing.tearDown),
        ZopeDocFileSuite('customerize.txt', package="five.customerize"),
        FunctionalDocFileSuite('browser.txt', package="five.customerize")
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
