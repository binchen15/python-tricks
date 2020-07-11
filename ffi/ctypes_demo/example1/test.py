import ctypes

libc = ctypes.CDLL("./libclib.so")

# python string is immutable
original_string = "starting string"
# ctypes string_buffer (bytes array) is mutable
mutable_string = ctypes.create_string_buffer(str.encode(original_string))

print("Before: original:", original_string)
libc.add_one_to_string(original_string)
print("After: original:", original_string)

print("Before: mutable: ", mutable_string.value)
libc.add_one_to_string(mutable_string)  # Works!
print("After: mutable: ", mutable_string.value)


alloc_func = libc.alloc_C_string
free_func = libc.free_C_string
alloc_func.restype = ctypes.POINTER(ctypes.c_char)
free_func.argtypes = [ctypes.POINTER(ctypes.c_char), ]

print("Allocating and freeing memory in C")
c_string_address = alloc_func()

# We should convert POINTER object to something we can use on the Python side
phrase = ctypes.c_char_p.from_buffer(c_string_address)
print("Bytes in Python {0}".format(phrase.value))

# let C free the memory
free_func(c_string_address)

