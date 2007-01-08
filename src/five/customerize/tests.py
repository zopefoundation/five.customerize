import unittest
from zope.testing.doctest import DocTestSuite
from Testing.ZopeTestCase import ZopeDocFileSuite
from Testing.ZopeTestCase import FunctionalDocFileSuite

import zope.component.testing
from zope.traversing.adapters import DefaultTraversable
from zope.publisher.browser import BrowserLanguages
from zope.publisher.http import HTTPCharsets

__docformat__ = "reStructuredText"

def setUp(test):
    zope.component.testing.setUp(test)
    zope.component.provideAdapter(DefaultTraversable, (None,))
    zope.component.provideAdapter(BrowserLanguages)
    zope.component.provideAdapter(HTTPCharsets)

def test_suite():
    return unittest.TestSuite([
        #DocTestSuite('five.customerize.browser'),
        ZopeDocFileSuite('zpt.txt', package="five.customerize",
                         setUp=setUp, tearDown=zope.component.testing.tearDown),
        ZopeDocFileSuite('customerize.txt', package="five.customerize"),
        FunctionalDocFileSuite('browser.txt', package="five.customerize")
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
