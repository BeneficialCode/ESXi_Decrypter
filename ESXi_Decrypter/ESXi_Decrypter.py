# -*- coding:utf-8 -*-
import base64
from Crypto.Cipher import AES

# Windows: C:\ProgramData\VMware\vCenterServer\cfg\vmware-vpx\vcdb.properties 
# Linux: /etc/vmware-vpx/vcdb.properties
# VCDB vc 
# select user_name,passord FROM vc.vpx_host;
pharse = '*nPFAKmpoTxGg/RuQC9Fqqzo8qpw5dg6bawtPGmhrF/VHCyKXAKCy2ZWd+Xvl/eoKgYjqof7g/jgtIVkKxIz3eA=='
# Windows：C:\ProgramData\VMware\vCenterServer\cfg\vmware-vpx\ssl\symkey.dat
# Linux：/etc/vmware-vpx/ssl/symkey.dat
keyStr = 'adb342060c77481fb9f11be21d8e9d721a7cdd57fc3fe387f00d81d4bd871e41'

def pkcs7unpadding(text):
    length = len(text)
    padding_length = ord(text[-1])
    return text[0:length-padding_length]

def decrypt(decryptBytes,key,iv):
    cipher = AES.new(key,AES.MODE_CBC,iv)
    msg = cipher.decrypt(decryptBytes)
    pwd = str(msg,encoding='utf-8')
    pwd = pkcs7unpadding(pwd)
    return pwd

bytes = base64.b64decode(pharse)
iv = bytes[0:16]
key = bytes.fromhex(keyStr)
pwd = decrypt(bytes[16:],key,iv)
print(pwd)
