import ctypes


def wrap_function(lib, funcname, restype, argtypes):
    ''' Simplify wrapping ctypes functions '''
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func


# struct Point { }
class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)


if __name__ == '__main__':
    # load the shared library into c types.
    libc = ctypes.CDLL("./libpoint.so")
    show_point = wrap_function(libc, 'show_point', None, [Point])
    move_point = wrap_function(libc, 'move_point', None, [Point])
    move_point_by_ref = wrap_function(libc, 'move_point_by_ref', None,
                                      [ctypes.POINTER(Point)])

    ###########################################################################
    print("Pass a struct into C")
    a = Point(1, 2)
    print("Point in python is", a)
    show_point(a)
    print()

    ###########################################################################
    print("Pass by value")
    a = Point(5, 6)
    print("Point in python is", a)
    move_point(a)
    print("Point in python is", a)
    print()

    ###########################################################################
    print("Pass by reference")
    a = Point(5, 6)
    print("Point in python is", a)
    move_point_by_ref(a)
    print("Point in python is", a)
    print()
