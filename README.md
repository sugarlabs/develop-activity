What is this?
=============

Develop allows you to edit existing Sugar activities or create new ones.

How to use?
===========

Develop is not part of the Sugar desktop, but can be added.  Please refer to;

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/),
* [How to use Sugar](https://help.sugarlabs.org/),
* [Download Develop using Browse](https://activities.sugarlabs.org/), search for `Develop`, then download, and;
* [How to use Develop](https://help.sugarlabs.org/develop.html)

How to develop?
===============

## Ninja-IDE
Ninja IDE is a direct dependency of `develop-activity`, Ninja IDE is
obtained from https://github.com/ninja-ide/ninja-ide Ninja releases
new introspection libraries which are used by develop activity to
check the code.

### Porting Ninja IDE
Ninja IDE comes bundled with its original GUI, its tests, installer
etc. However these are unnecessary.  Moreover, Ninja IDE Python3
branch is still in beta. So there are bugs in the code.  For temporary
fixes and removing code, there are patches on
https://github.com/srevinsaju/ninja-ide/tree/minima

The porting, or fixes are provided in patches, referred to in the
folder
https://github.com/srevinsaju/ninja-ide/tree/minima/patch-20191229
Apply each patch to the latest Ninja-IDE version, so that the app is
compatible, as well as we reduce the size of the develop-activity
without adding unused dependencies.

### Additional Notes
Ninja IDE is a very old repository with a lot of commits.  After
cloning the latest repository and applying the patches mentioned
above, consider removing `.git`, `.gitignore` to further reduce the
size and to prevent internal conflicts.
