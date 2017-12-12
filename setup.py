from distutils.core import setup
from distutils.extension import Extension

extensions = [Extension("mem", ["_mem.c", "mem.c"])]

setup(name='mem',
    version='.1',
    ext_modules=extensions
    )
