import math

m1 = int(input(), 16)
m2 = int(input(), 16)
m3 = int(input(), 16)

bobs_key = m1 ^ m2
plain = m3 ^ bobs_key 

bit_length = plain.bit_length()
byte_length = math.ceil(bit_length / 8)
plain_bytes = plain.to_bytes(byte_length, "big")
plain_text = str(plain_bytes, "ascii")

print(plain_text)