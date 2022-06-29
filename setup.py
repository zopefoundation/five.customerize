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

from setuptools import setup


version = '2.1.0'

setup(
    name='five.customerize',
    version=version,
    description='TTW customization of template-based Zope browser views',
    long_description=(open('README.rst').read() + "\n" +
                      open('CHANGES.rst').read()),
    keywords='zope views templates customization ttw',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='https://github.com/zopefoundation/five.customerize',
    project_urls={
        'Issue Tracker': ('https://github.com/zopefoundation/'
                          'five.customerize/issues'),
        'Sources': 'https://github.com/zopefoundation/five.customerize',
    },
    license='ZPL 2.1',
    packages=['five', 'five.customerize'],
    package_dir={'': 'src'},
    namespace_packages=['five'],
    include_package_data=True,
    platforms='Any',
    zip_safe=False,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    install_requires=[
        'setuptools',
        'plone.portlets',
        'zope.component',
        'zope.componentvocabulary',
        'zope.dottedname',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.pagetemplate',
        'zope.schema',
        'zope.traversing',
        'zope.viewlet',
        'Acquisition',
        'Zope',
    ],
    extras_require={
        'test': [
            'plone.testing>=7',
            'zope.publisher',
            'zope.site',
            'zope.testing',
            'transaction',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope :: 4',
        'Framework :: Zope :: 5',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
