import hashlib

nombre = "Jose Vicente"
nombre_bytes = nombre.encode('utf-8')
resultado = hashlib.md5(nombre_bytes)
print(resultado.hexdigest())

nombre2 = "Jose Vicente"
nombre_bytes2 = nombre2.encode('utf-8')
resultado2 = hashlib.sha1(nombre_bytes2)
print(resultado2.hexdigest())





