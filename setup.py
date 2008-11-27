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

version = '0.4'

setup(name = 'five.customerize',
      version = version,
      description = 'TTW customization of template-based Zope 3 views',
      keywords = 'zope3 views templates customization ttw',
      author = 'Zope Corporation and Contributors',
      author_email = 'z3-five@codespeak.net',
      url = 'http://svn.zope.org/five.customerize',
      download_url = 'http://cheeseshop.python.org/pypi/five.customerize/',
      license = 'ZPL 2.1',
      packages = ['five', 'five.customerize'],
      package_dir = {'': 'src'},
      namespace_packages = ['five',],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
        'setuptools',
      ],
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
      ],
)

