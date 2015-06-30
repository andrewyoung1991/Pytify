from __future__ import absolute_import

import sys

if 'linux' in sys.platform:
    from .linuxpytify import LinuxPytify as strategy
elif 'darwin' in sys.platform:
    from .darwinpytify import DarwinPytify as strategy
else:
    raise SystemError('%s is not supported.' % sys.platform)


def get_pytify_class_by_platform():
    return strategy
