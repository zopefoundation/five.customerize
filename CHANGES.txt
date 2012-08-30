CHANGES
=======

1.1.1 (unreleased)
------------------

- Nothing changed yet.


1.1 (2012-08-30)
----------------

- Removed dependency and support for zope.app.pagetemplate.


1.0.3 (2012-05-07)
------------------

- Fix bug which prevented authorization of TTW views in Zope 2.12+
  [davisagli]

1.0.2 (2011-10-07)
------------------

- Fixed: mangle works when a template has in its path
  a folder which name starts with a dot.
  [thomasdesvenain]

1.0.1 - 2011-04-03
------------------

- Made tests compatible with PluggableAuthService 1.7.3
  [esteele]

1.0 - 2010-06-13
----------------

- Package metadata cleanup and provide a buildout configuration for testing
  the package on its own.
  [hannosch]

- Made tests compatible with Zope 2.13 and avoid deprecation warnings.
  [hannosch]

1.0b1 - 2010-05-01
------------------

- Updated imports to avoid dependencies on zope.app.component and
  zope.app.container.
  [davisagli]

- Fixed a memory leak by making sure that TTW view subclasses are only
  generated once, rather than once per request.
  [davisagli]

- Make sure TTW viewlet and portlet classes get the containing view as the
  view parameter on initialization, rather than getting themselves.
  [davisagli]

1.0a1 - 2009-11-14
------------------

- Support Zope 2.12's BoundPageTemplateFile.

- Fixed deprecation warnings for use of Globals.

- Specify all package dependencies.

- Avoid a dependency on zope.app.apidoc by copying over the getViews method.

0.3 - 2008-07-07
----------------

- Fix for the long-standing issue where the security context had mysteriously
  gone missing.

0.2 - 2007-08-17
----------------

- Support for viewlets and portlets as used in Plone 3.0

0.1.3 - 2007-07-08
------------------

- Fix in setup.py

0.1.2 - 2007-05-04
------------------

- Release for Plone 3.0beta3 without OSX metadata

0.1.1 - 2007-03-03
------------------

- Minor tweaks and enhancements for the integration into Plone 3.0

0.1 - 2006-10-30
----------------

- Initial version.
