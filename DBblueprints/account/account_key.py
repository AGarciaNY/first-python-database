import rsa

kep_pub, key_pri = rsa.newkeys(1024)
with open("keyPub2.pem","wb") as f:
    f.write(kep_pub.save_pkcs1("PEM"))

with open("keyPriv2.pem","wb") as f:
    f.write(key_pri.save_pkcs1("PEM"))