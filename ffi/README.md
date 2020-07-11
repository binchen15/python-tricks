https://dbader.org/blog/python-cffi
https://dbader.org/blog/python-ctypes-tutorial

ctypes:
	python string immutable,
	ctypes.string_buffer is mutable, -- char*

	function signature

	cfun = clib.func
	cfun.restype = ctypes.POINTER(ctypes.c_char)
	cfun.argtypes = [ctypes.POINTER(ctypes.c_char), ]

	cross-language marshalling
	 the language that allocates the memory also needs to free the memory

