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
"""Setup for five.customerize package

$Id$
"""
import os
from setuptools import setup, Extension

setup(name='five.customerize',
      version='0.1',
      url='http://svn.zope.org/five.customerize',
      license='ZPL 2.1',
      description='TTW customization of template-based Zope 3 views',
      author='Zope Corporation and Contributors',
      author_email='z3-five@codespeak.net',
      long_description='',
      
      packages=['five', 'five.customerize'],
      package_dir = {'': 'src'},
      namespace_packages=['five',],
      include_package_data = True,

      zip_safe = False,
      )
