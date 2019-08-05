from io import BytesIO


def writeBytes():
    f = BytesIO()
    f.write("你好！".encode("utf-8"))
    print(f.getvalue())

writeBytes()



def readBytes():
    f = BytesIO(b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x81')
    print(f.read())

readBytes()