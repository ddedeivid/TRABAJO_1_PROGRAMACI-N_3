from datetime import datetime
""" Importé datetime para validar de manera sencilla el formato de fecha, también 
podría haber preguntado dato por dato (día, mes, año) y validarlos por separado, pero me pareció más simple así."""


def _leer(mensaje):
    return input(mensaje)


def leer_texto_no_vacio(mensaje):
    while True:
        valor = _leer(mensaje).strip()
        if valor == "":
            print("  ERROR: este campo no puede quedar vacío. Intente de nuevo.")
            continue
        return valor


def leer_nombre(mensaje):
    """Evita: vacío y también evita números o símbolos (solo letras y espacios)."""
    while True:
        valor = _leer(mensaje).strip()
        if valor == "":
            print("  ERROR: el nombre no puede quedar vacío. Intente de nuevo.")
            continue
        # isalpha() sí acepta letras con tilde y ñ, pero NO números ni símbolos
        if not all(parte.isalpha() for parte in valor.split(" ")):
            print("  ERROR: el nombre solo puede contener letras y espacios (sin números ni símbolos). Intente de nuevo.")
            continue
        return valor


def leer_solo_numeros(mensaje, longitud_min=1, longitud_max=15):
    while True:
        valor = _leer(mensaje).strip()
        if valor == "":
            print("  ERROR: este campo no puede quedar vacío. Intente de nuevo.")
            continue
        if not valor.isdigit():
            print("  ERROR: solo se permiten números (sin espacios ni letras). Intente de nuevo.")
            continue
        if not (longitud_min <= len(valor) <= longitud_max):
            print(f"  ERROR: debe tener entre {longitud_min} y {longitud_max} dígitos. Intente de nuevo.")
            continue
        return valor


def leer_entero_positivo(mensaje, maximo=1000):
    while True:
        valor = _leer(mensaje).strip()
        if valor == "":
            print("  ERROR: este campo no puede quedar vacío. Intente de nuevo.")
            continue
        try:
            valor_int = int(valor)
        except ValueError:
            print("  ERROR: debe ingresar un número entero válido. Intente de nuevo.")
            continue
        if valor_int <= 0:
            print("  ERROR: la cantidad debe ser mayor que cero. Intente de nuevo.")
            continue
        if valor_int > maximo:
            print(f"  ERROR: la cantidad parece demasiado alta (máximo {maximo}). Intente de nuevo.")
            continue
        return valor_int


def leer_opcion_menu(titulo, opciones):
    while True:
        print(f"\n{titulo}")
        for i, op in enumerate(opciones, start=1):
            print(f"  {i}. {op}")
        seleccion = _leer("Seleccione una opción: ").strip()
        if seleccion == "":
            print("  ERROR: debe seleccionar una opción. Intente de nuevo.")
            continue
        if not seleccion.isdigit():
            print("  ERROR: ingrese el número de la opción. Intente de nuevo.")
            continue
        indice = int(seleccion)
        if indice < 1 or indice > len(opciones):
            print("  ERROR: opción fuera de rango. Intente de nuevo.")
            continue
        return opciones[indice - 1]


def leer_fecha(mensaje):
    while True:
        valor = _leer(mensaje).strip()
        if valor == "":
            print("  ERROR: la fecha no puede quedar vacía. Intente de nuevo.")
            continue
        try:
            fecha_ingresada = datetime.strptime(valor, "%d/%m/%Y")
        except ValueError:
            print("  ERROR: formato de fecha inválido. Use dd/mm/aaaa (ej: 25/12/2026). Intente de nuevo.")
            continue
        if fecha_ingresada.date() < datetime.now().date():
            print("  ERROR: la fecha de la cita no puede ser una fecha pasada. Intente de nuevo.")
            continue
        return valor


def leer_cedula_o_salir(mensaje):
    """Lee una cédula para buscar. Si el usuario escribe 'salir' (sin importar
    cómo combine mayúsculas y minúsculas), se devuelve 'SALIR' para terminar
    la búsqueda en vez de forzar a ingresar una cédula."""
    while True:
        valor = _leer(mensaje).strip()
        if valor.upper() == "SALIR":
            return "SALIR"
        if valor == "":
            print("  ERROR: este campo no puede quedar vacío. Escriba una cédula o 'SALIR'. Intente de nuevo.")
            continue
        if not valor.isdigit():
            print("  ERROR: solo se permiten números, o escriba 'SALIR' para terminar. Intente de nuevo.")
            continue
        return valor


def leer_respuesta_sn(mensaje):
    while True:
        valor = _leer(mensaje).strip().lower()
        if valor in ("s", "n"):
            return valor
        print("  ERROR: responda solamente 's' (sí) o 'n' (no). Intente de nuevo.")
