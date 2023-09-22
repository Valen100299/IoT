# Define el mensaje encriptado y la clave
mensaje_encriptado = (
    "EF AC 9B 60 03 36 C8 A4 8A 6F 57 2C D8 B9 CF 29 "
    "4D 6B 82 F7 CF 51 46 37 D8 A2 81 21 54 2D C4 ED 86 72 03 "
    "27 CE B9 9B 64 51 65 CA B9 CF 72 57 24 DF A4 9C 75 4A 26 "
    "D8 ED 9B 69 42 2B 8B AC 81 78 03 36 C4 AB 9B 76 42 37 CE "
    "ED 8A 6F 44 2C C5 A8 8A 73 03 24 C5 A9 CF 63 46 31 DF A8 "
    "9D 21 42 31 8B BE 80 67 57 32 CA BF 8A 21 46 2B CC A4 81 "
    "64 46 37 C2 A3 88 21 57 2D CA A3 CF 60 4D 3C 8B BE 9B 60 "
    "57 2C D8 B9 86 62 4A 24 C5 E3"
)
clave = "AB CD EF 01 23 45"

# Convierte el mensaje encriptado y la clave a listas de bytes
partes_mensaje = [int(parte, 16) for parte in mensaje_encriptado.split()]
partes_clave = [int(parte, 16) for parte in clave.split()]

# Desencripta el mensaje
mensaje_desencriptado = ''.join(
    chr(partes_mensaje[i] ^ partes_clave[i % len(partes_clave)]) for i in range(len(partes_mensaje))
)

print("Mensaje Desencriptado:", mensaje_desencriptado)