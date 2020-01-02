import os
import glob
from environs import Env
from cffi import FFI


env = Env()
env.read_env()
ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
# ffibuilder.cdef("""
#
# """)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".

here = os.path.dirname(os.path.abspath(__file__))

dist = env("GO_DIST", "./go_dist/")
go_src = env("GO_SRC_DIR", "./go/")

dist_path = dist

files = glob.glob(os.path.join(dist_path, "*.h"))

HEADERS = ""

for header in files:
    HEADERS += f'#include "{header}";\n'

LIB_NAME = env("LIB_NAME", "pygo")

ffibuilder.set_source(
    LIB_NAME,
    HEADERS,  # the C header of the library
    libraries=[]
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
