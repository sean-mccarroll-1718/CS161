# For Part 1
x = 31
print(x)
print(bin(x))
print(hex(x))

# For Part 2
# error for 1.825 TypeError: 'float' object cannot be interpreted as an integer
x = 18
print(x)
print(bin(x))
print(hex(x))

# For Part 3
y = 0b1011
z = 0xA3
print(y,z)

# For Part 4
w = x + y + z
print(f'the sum is {w}')

# For Compression secton
original_size = 240
dictionary_size = 25
compressed_text_size = 148
total_compressed_size = dictionary_size + compressed_text_size
compression_percentage = 1-(compressed_text_size/original_size)
compression_percentage = compression_percentage * 100
print(f'  compressed text size is: {compressed_text_size} characters')
print(f'       dictionary size is: {dictionary_size} characters')
print(f' total compressed size is: {total_compressed_size} characters')
print(f'    original text size is: {original_size} characters')
print(f'compression percentage is: {compression_percentage}%')



