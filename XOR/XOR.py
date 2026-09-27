import base64, subprocess, sys

# ====================== Funciones ======================

def limpiar():
    """Limpia la terminal"""
    if sys.platform.startswith("win"):
        subprocess.run("cls", shell=True)
    else:
        subprocess.run(["clear"])

def mostrar_datos(datos_planos: str, clave: str, datos_cifrados: bytes, descifrado=False):
    """Esta funcion permite mostrar los datos de una forma limpia y explicativa"""

    # Preparaciones
    desglose_binario_datos = ' '.join(format(ord(char), '08b') for char in datos_planos)
    desglose_binario_clave = ' '.join(format(ord(char), '08b') for char in clave)
    clave_repetida = (clave * (len(datos_planos) // len(clave) + 1))[:len(datos_planos)]

    # Mostrado de datos
    print(f"""
========= Explicación =========

[i] Datos introducidos [i]
Texto: {repr(datos_planos)}
- Desglose decimal:     {[ord(char) for char in datos_planos]}
- Desglose hexadecimal: {datos_planos.encode().hex()}
- Desglose binario:     {desglose_binario_datos}

Clave: {repr(clave)}
- Desglose decimal:     {[ord(char) for char in clave]}
- Desglose hexadecimal: {clave.encode().hex()}
- Desglose binario:     {desglose_binario_clave}

[!] {"CIFRADO" if descifrado == False else "DESCIFRADO"} [!]
- Texto:      {desglose_binario_datos}
- Clave:      {' '.join(format(ord(char), '08b') for char in clave_repetida)}
              {'-' * len(desglose_binario_datos)}
- Resultado:  {' '.join(format(ord(char), '08b') for char in datos_cifrados.decode())}
- Resultado hexadecimal: {datos_cifrados.hex()}
- Resultado decimal: {[ord(char) for char in datos_cifrados.decode()]}
- Resultado en Base64: {base64.b64encode(datos_cifrados).decode()}
- Resultado ASCII: {repr(datos_cifrados.decode())}
""")

def cifrar_descifrar_xor(datos: bytes, clave: bytes) -> bytes:
        """Cifrado y Descifrado XOR"""
        # Comenzamos el cifrado
        resultado = bytearray()

        for i in range(len(datos)):
            byte_dato = datos[i]
            byte_clave = clave[i % len(clave)]

            resultado.append(byte_dato ^ byte_clave)

        return bytes(resultado)

def cifrado():
    """Flujo de cifrado de la herramienta"""

    # Solicitamos los datos y la clave de cifrado
    texto_plano = input("Introduce el texto a cifrar: ").strip()
    clave = input(f"Introduce la clave de cifrado (es recomendable que sea de {len(texto_plano)} caracteres de longitud): ")

    bytes_cifrados = cifrar_descifrar_xor(datos=texto_plano.encode(), clave=clave.encode())

    mostrar_datos(texto_plano, clave, bytes_cifrados)

    archivo = input("Deséa crear un archivo?[y/N]: ")

    if archivo.lower() in ["y", "yes"]:
        ruta = input("Introduzca la ruta al archivo: ")
        try:
            with open(ruta, 'wb') as f:
                f.write(bytes_cifrados)
        except Exception as e:
            print("[!] Error al crear el archivo: " + str(e))


def descifrado():
    """Flujo de descifrado"""

    menu = input(f"""
Base64  ->  (1)
Archivo ->  (2)

> """)

    print()

    if menu == "1":
        texto_cifrado = base64.b64decode(input("Introduce el código en Base64: "))  # bytes
        clave = input("Introduce la clave de descifrado: ")  # str

        resultado = cifrar_descifrar_xor(texto_cifrado, clave.encode())

        mostrar_datos(texto_cifrado.decode(), clave, resultado, descifrado=True)

    elif menu == "2":
        import os
        ruta = input("Introduce la ruta al archivo a descifrar: ")
        if not os.path.exists(ruta):
            print(f"[!] ERROR: No existe el archivo {os.path.basename(ruta)} en la ruta {ruta}")
            sys.exit(-1)

        with open(ruta, 'rb') as f:
            datos = f.read()

        clave = input("Introduce la clave de descifrado: ")
        resultado = cifrar_descifrar_xor(datos, clave.encode())

        mostrar_datos(datos.decode(), clave, resultado, descifrado=True)


# ====================== Flujo ejecución ======================

def main():
    """FLujo principal del programa"""

    limpiar()
    cifrar_descifrar = input(f"""MENÚ DE OPCIONES
Cifrar     ->  (1)
Descifrar  ->  (2)

> """)

    print()

    if cifrar_descifrar == '1':
        cifrado()
    elif cifrar_descifrar == '2':
        descifrado()

if __name__ == "__main__":
    main()