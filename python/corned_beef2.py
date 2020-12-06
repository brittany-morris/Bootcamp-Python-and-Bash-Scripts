#!/usr/bin/env python3
import hashlib

count = 0
hash = "a497453fe1eee3e0c4d44f2a74a1518744d247a1c6dd6c902a2b3367987f0e5d21fb1cbdd1af55ea78098be5a336ffaf06f19b8e5a5997e06d20ce00f9907424"
flag1 = "FS{hash-I_had_corned_beef_and_hash_xxx}"
for i in range(int('0', 16), int('FFF', 16)):
#i_filler = str(i).zfill(3)
#turns i into a hexadecimal
    i_hex = hex(i)
    #slices and keeps last 3 characters and applies upper string method
    hex_strip = i_hex[-3:].upper()
#creates hash object
    i_hash = hashlib.sha512(flag1.replace("xxx", hex_strip).encode())
    #digest hash object
    hashes = i_hash.hexdigest() 
#   print(flag1.replace("xxx", hex_strip))
#   print(hashes)
#   print(str(i).z))
    #compare hashes to knon hash
    if hashes == hash:
        print(hex_strip)
        print(flag1)
#        print(hashes)
