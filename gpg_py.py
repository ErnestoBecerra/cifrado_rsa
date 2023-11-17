import gnupg

# Ruta al directorio donde deseas guardar las claves
directorio_claves = r'C:\Users\ERNESTO\Documents\DANIEL'
ruta_gpg = r'C:\Program Files (x86)\GnuPG\bin\gpg.exe'

def generar_claves():
    gpg = gnupg.GPG(gpgbinary=ruta_gpg)

    # Generar el par de claves
    clave = gpg.gen_key_input(
        key_type="RSA",
        key_length=2048,
        passphrase="maythe4thwithu+"
    )
    clave = gpg.gen_key(clave)

    clave_publica = gpg.export_keys(clave.fingerprint)
    clave_privada = gpg.export_keys(clave.fingerprint, secret=True, passphrase="maythe4thwithu+")

    # Guardar la clave pública en un archivo de texto
    with open(f"{directorio_claves}/clave_publica.txt", "w") as archivo:
        archivo.write(clave_publica)

    # Guardar la clave privada en un archivo de texto
    with open(f"{directorio_claves}/clave_privada.txt", "w") as archivo:
        archivo.write(clave_privada)

    print("Se han generado y guardado las claves correctamente.")

generar_claves()
