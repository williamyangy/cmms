import datetime
import hashlib

now = datetime.datetime.now()




text = "ls@" + str(now.day) + "3tP" + str(now.month - 1) + "kEy"

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.digest().hex()
print(text)

print(computeMD5hash(text).upper())

