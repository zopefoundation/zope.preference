##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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
"""Setup for zope.preference package
"""
import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


tests_require = [
    'zope.security',
    'zope.site',
    'zope.testing',
    'zope.testrunner',
]

setup(name='zope.preference',
      version='5.0',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.dev',
      description='User Preferences Framework',
      long_description=(
          read('README.rst')
          + '\n\n' +
          '.. contents::\n\n' +
          read('src', 'zope', 'preference', 'README.rst')
          + '\n\n' +
          read('CHANGES.rst')
      ),
      keywords="bluebream zope zope3 user preference",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='http://github.com/zopefoundation/zope.preference',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope'],
      python_requires='>=3.7',
      extras_require={
          'test': tests_require,
          'zcml': [
              'zope.security',
          ],
      },
      install_requires=[
          'setuptools',
          'BTrees',
          'zope.annotation',
          'zope.component >= 3.8.0',
          'zope.container',
          'zope.schema',
          'zope.security',
          'zope.traversing',
      ],
      tests_require=tests_require,
      test_suite='zope.preference.tests.test_suite',
      include_package_data=True,
      zip_safe=False,
      )
