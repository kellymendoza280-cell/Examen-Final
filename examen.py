ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mensajes_guardados = []

def desplazar(mensaje, n):
    """Desplaza cada letra A-Z n posiciones (n puede ser negativo)."""
    resultado = ""
    for caracter in mensaje.strip().upper():
        if caracter in ALFABETO:
            posicion = ALFABETO.index(caracter)
            
            resultado += ALFABETO[(posicion + n) % 26]
        else:
            resultado += caracter  
    return resultado


def encriptar(mensaje, n):
    """Avanza n posiciones cada letra del mensaje."""
    return desplazar(mensaje, n)


def desencriptar(mensaje, n):
    """Retrocede n posiciones cada letra del mensaje."""
    return desplazar(mensaje, -n)


def pedir_desplazamiento():
    """Solicita N y valida que sea un entero >= 0."""
    while True:
        try:
            n = int(input("Ingrese el desplazamiento N: "))
            if n < 0:
                raise ValueError("N debe ser mayor o igual a 0")
            return n
        except ValueError:
            print("Error: N debe ser un número entero mayor o igual a 0.")


def mostrar_menu():
    print("\nSISTEMA DE CIFRADO CÉSAR MODIFICADO")
    print("=" * 32)
    print("1. Encriptar mensaje (Opción de Guardar mensaje (S/N))")
    print("2. Desencriptar mensaje")
    print("3. Imprimir mensajes guardados")
    print("4. Salir")
    print("=" * 32)


def opcion_encriptar():
    mensaje = input("Ingrese el mensaje: ").strip()
    n = pedir_desplazamiento()
    cifrado = encriptar(mensaje, n)

    print(f"Mensaje original: {mensaje.upper()}")
    print(f"Mensaje encriptado: {cifrado}")

    while True:
        guardar = input("¿Desea guardar el mensaje? (S/N): ").strip().upper()
        if guardar == "S":
            mensajes_guardados.append(
                {"original": mensaje.upper(), "cifrado": cifrado, "n": n}
            )
            print("Mensaje guardado correctamente.")
            break
        elif guardar == "N":
            print("El mensaje no fue guardado.")
            break
        else:
            print("Error: responda S o N.")


def opcion_desencriptar():
    mensaje = input("Ingrese el mensaje encriptado: ").strip()
    n = pedir_desplazamiento()
    print(f"Mensaje desencriptado: {desencriptar(mensaje, n)}")


def opcion_imprimir():
    if len(mensajes_guardados) == 0:
        print("No hay mensajes guardados.")
        return
    print("MENSAJES GUARDADOS")
    for i, registro in enumerate(mensajes_guardados, start=1):
        print(f"{i}. Original: {registro['original']}")
        print(f"   Encriptado: {registro['cifrado']}")
        print(f"   Desplazamiento: {registro['n']}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            opcion_encriptar()
        elif opcion == "2":
            opcion_desencriptar()
        elif opcion == "3":
            opcion_imprimir()
        elif opcion == "4":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Error: opción inexistente. Elija un número del 1 al 4.")


if _name_ == "_main_":
    main()