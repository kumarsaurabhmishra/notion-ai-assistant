# chr is used to convert the value in the corresponding string
# ord is used to check the unicode value of the string

val = 128522
print(chr(val)) # 😊

order = "😊"
print(ord(order)) # 128522

# String indexing

str = "String"
print(str[0]) # S (First index  -> forward way) -> positive indexing 
print(str[-1]) # g (last index) -> negative indexing
print(str[-2]) # n (last second) -> negative indexing