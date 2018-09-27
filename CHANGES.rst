=========
 CHANGES
=========

4.1.0 (2018-09-27)
==================

- Support newer zope.configuration and persistent. See `issue 2
  <https://github.com/zopefoundation/zope.preference/issues/2>`_.

- Add support for Python 3.7 and PyPy3.

- Drop support for Python 3.3.

4.0.0 (2017-05-09)
==================

- Add support for Python 3.4, 3.5 and 3.6.

- Add support for PyPy.

- Drop support for Python 2.6.


4.0.0a1 (2013-02-24)
====================

- Added support for Python 3.3.

- Replaced deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropped support for Python 2.4 and 2.5.

- Refactored tests not to rely on ``zope.app.testing`` anymore.

- Fixed a bug while accessing the parent of a preference group.


3.8.0 (2010-06-12)
==================

- Split out from `zope.app.preference`.

- Removed dependency on `zope.app.component.hooks` by using
  `zope.component.hooks`.

- Removed dependency on `zope.app.container` by using
  `zope.container`.
