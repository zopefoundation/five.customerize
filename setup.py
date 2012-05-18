##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Setup for five.customerize package """

from setuptools import setup

version = '1.0.4.dev0'

setup(name = 'five.customerize',
      version = version,
      description = 'TTW customization of template-based Zope views',
      long_description = (open('README.txt').read() + "\n" +
                          open('CHANGES.txt').read()),
      keywords = 'zope views templates customization ttw',
      author = 'Zope Foundation and Contributors',
      author_email = 'z3-five@codespeak.net',
      url = 'http://pypi.python.org/pypi/five.customerize',
      license = 'ZPL 2.1',
      packages = ['five', 'five.customerize'],
      package_dir = {'': 'src'},
      namespace_packages = ['five',],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
        'setuptools',
        'plone.portlets',
        'zope.component',
        'zope.componentvocabulary',
        'zope.dottedname',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.pagetemplate',
        'zope.publisher',
        'zope.schema',
        'zope.site',
        'zope.testing',
        'zope.traversing',
        'zope.viewlet',
        'transaction',
        'Acquisition',
        'Zope2',
      ],
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope2',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
      ],
)
