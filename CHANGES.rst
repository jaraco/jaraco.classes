v3.1.1
======

Packaging refresh and associated cleanups, including fix
for #4 (failing black check).

v3.1.0
======

``classproperty`` decorator now supplies a
``classproperty.Meta`` class. Classes that wish to have
a class property should derive from that metaclass. This
approach solves the unintended behavior of the property
only being set on a given instance. For compatibility, the
old behavior is retained if the metaclass is not used.

v3.0.0
======

Project now requires Python 3.6 or later.

2.0
===

Switch to `pkgutil namespace technique
<https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages>`_
for the ``jaraco`` namespace.

1.5
===

Refresh packaging.

Use Python 3 syntax for new-style classes.

1.4.3
=====

Corrected namespace package declaration to match
``jaraco`` namespaced packages.

1.4.2
=====

#1: Added a project description.

1.4.1
=====

Refresh packaging.

1.4
===

Added documentation.

Project is now automatically released by Travis CI.

1.3
===

Move hosting to Github.

Use setuptools_scm for version detection.

1.2
===

Limit dependencies in setup_requires.

1.1
===

Added ``properties`` module from jaraco.util 10.8.

1.0
===

Initial release based on jaraco.util 10.8.
