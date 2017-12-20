import os
import glob

from plugins import *


def do_import(mud_name):
    globals()[mud_name] = __import__(mud_name)


modules = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = \
    [
        os.path.basename(f)[:-3]
        for f in modules
        if os.path.isfile(f) and not f.endswith('__init__.py')
        ] + \
    [
        name
        for name in os.listdir(os.path.dirname(__file__))
        if os.path.isdir(os.path.join(os.path.dirname(__file__), name)) and not name.startswith("__")
    ]

[do_import('plugins.' + name) for name in __all__]
