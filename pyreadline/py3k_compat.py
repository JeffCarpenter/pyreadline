from __future__ import print_function, unicode_literals, absolute_import
import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

PY3 = sys.version_info[0] >= 3

if PY3:
    try:
        from collections.abc import Callable
    except ImportError:
        from collections import Callable

    def callable(x):
        return isinstance(x, Callable)
    
    def execfile(fname, glob, loc=None):
        loc = glob if loc is None else loc
        with open(fname) as fil:
            txt = fil.read()
        exec(compile(txt, fname, 'exec'), glob, loc)
    
    unicode = str
    bytes = bytes
else:
    callable = callable
    execfile = execfile
    bytes = str
    unicode = unicode
