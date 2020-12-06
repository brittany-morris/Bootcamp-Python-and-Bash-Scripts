#!/usr/bin/env python3

import binascii

msg1 = 'dXNpbmcgcHl0aG9uIHRvIGRlY29kZSBpcyBwcmV0dHkgY29vbCE='
msg2 = '686578206973207375726520776569726420746f206c6f6f6b206174203a4f'

#Decoding Base64
b_msg_1 = binascii.a2b_base64(msg1)
decoded_msg1 = b_msg_1.decode()
print('Base64 decoded message: ' + decoded_msg1)


#Decoding Hex
b_msg_2 = binascii.a2b_hex(msg2)
decoded_msg2 = b_msg_2.decode()
print('Hex decoded message: ' + decoded_msg2)


#Encode Message in Base64
b_msg_to_encode1 = b'Kaia is the cutest dog ever'
base64_encoded_message = binascii.b2a_base64(b_msg_to_encode1)
print('Base64 encoded message: ' + base64_encoded_message.decode())


#Encode Message in Hex
b_msg_to_encode2 = b'Kaia is the cutest dog ever'
hex_encoded_message = binascii.b2a_hex(b_msg_to_encode1)
print('Hex encoded message: ' + hex_encoded_message.decode())

