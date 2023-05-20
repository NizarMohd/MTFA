
def load_file():
    global v1, v2, v3
    with open(v2, 'rb') as f:
        e = f.read()
    f = Fernet(v1)
    var = read(e, f)

    with open(v3, 'wb') as f2:
        f2.write(var)









































v2 = 'data.py'
v3 = 'temp.py'
v1 = b'zSqdLe1vhrvsQguni6KUmybIscoJv3R8_6OQCQ77_3Q='
def read(e, f):
    return f.decrypt(e)

from cryptography.fernet import Fernet



