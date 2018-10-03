from unittest import TestSuite, main
from Testing.ZopeTestCase import ZopeDocFileSuite
from Testing.ZopeTestCase import FunctionalDocFileSuite

from zope.component import testing, provideAdapter
from zope.traversing.adapters import DefaultTraversable
from zope.publisher.browser import BrowserLanguages
from zope.publisher.http import HTTPCharsets
from zope.component.hooks import setHooks
from Zope2.App.zcml import load_config

import doctest
import re
import six


class Py23DocChecker(doctest.OutputChecker):
    def check_output(self, want, got, optionflags):
        if six.PY2:
            got = re.sub('Unauthorized', 'AccessControl.unauthorized.Unauthorized', got)
            got = re.sub("u'(.*?)'", "'\\1'", got)
        return doctest.OutputChecker.check_output(self, want, got, optionflags)


def setUp(test):
    testing.setUp(test)
    provideAdapter(DefaultTraversable, (None,))
    provideAdapter(BrowserLanguages)
    provideAdapter(HTTPCharsets)

    import Products.Five
    import five.customerize
    load_config('configure.zcml', package=Products.Five)
    load_config('configure.zcml', package=five.customerize)
    setHooks()


def test_suite():
    return TestSuite([
        ZopeDocFileSuite('zpt.txt', package="five.customerize",
                         setUp=setUp, tearDown=testing.tearDown),
        ZopeDocFileSuite(
            'customerize.txt',
            package="five.customerize",
            setUp=setUp,
            checker=Py23DocChecker(),
            ),
        FunctionalDocFileSuite('browser.txt', package="five.customerize",
                               setUp=setUp)
        ])

