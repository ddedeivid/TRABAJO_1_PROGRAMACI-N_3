from tarifas import (
    TIPOS_CLIENTE, TIPOS_ATENCION, PRIORIDADES,
    obtener_valor_cita, obtener_valor_atencion, obtener_cantidad_fija
)
from validaciones import (
    leer_nombre, leer_solo_numeros, leer_entero_positivo,
    leer_opcion_menu, leer_fecha, leer_respuesta_sn, leer_cedula_o_salir
)

MAX_DIENTES = 32  # Nadie tiene más de 32 dientes: límite para Calzas y Extracción
from modelos import Cliente
from procesos import ordenar_por_valor_atencion_desc, buscar_por_cedula, mostrar_reportes, mostrar_lista


def capturar_cliente():
    """Pide y valida por teclado todos los datos de un cliente y arma un objeto Cliente."""
    print("\n--- Datos del cliente ---")
    cedula = leer_solo_numeros("Cédula: ", longitud_min=6, longitud_max=12)
    nombre = leer_nombre("Nombre: ")
    telefono = leer_solo_numeros("Teléfono: ", longitud_min=7, longitud_max=10)

    tipo_cliente = leer_opcion_menu("Tipo de Cliente:", TIPOS_CLIENTE)
    tipo_atencion = leer_opcion_menu("Tipo de Atención:", TIPOS_ATENCION)

    cantidad_fija = obtener_cantidad_fija(tipo_atencion)
    if cantidad_fija is not None:
        cantidad = cantidad_fija
        print(f"(La cantidad para {tipo_atencion} se fija automáticamente en {cantidad})")
    else:
        # Calzas y Extracción: la cantidad no puede superar 32 (total de dientes)
        cantidad = leer_entero_positivo(f"Cantidad de {tipo_atencion}: ", maximo=MAX_DIENTES)

    prioridad = leer_opcion_menu("Prioridad de Atención:", PRIORIDADES)
    fecha_cita = leer_fecha("Fecha de la cita (dd/mm/aaaa): ")

    valor_cita = obtener_valor_cita(tipo_cliente)
    valor_atencion_unitario = obtener_valor_atencion(tipo_cliente, tipo_atencion)

    cliente = Cliente(
        cedula=cedula,
        nombre=nombre,
        telefono=telefono,
        tipo_cliente=tipo_cliente,
        tipo_atencion=tipo_atencion,
        cantidad=cantidad,
        prioridad=prioridad,
        fecha_cita=fecha_cita,
        valor_atencion_unitario=valor_atencion_unitario,
        valor_cita=valor_cita
    )

    valor_fmt = f"${cliente.calcular_valor_a_pagar():,}".replace(",", ".")
    print(f"\n>> Valor a pagar por {nombre}: {valor_fmt}")
    return cliente


def main():
    arreglo_clientes = []  # Arreglo (lista) en memoria con todos los clientes

    print(" CONSULTORIO ODONTOLÓGICO - DR. XXX")

    try:
        seguir_registrando = True
        while seguir_registrando:
            cliente = capturar_cliente()
            arreglo_clientes.append(cliente)

            respuesta = leer_respuesta_sn("\n¿Desea registrar otro cliente? (s/n): ")
            if respuesta == "n":
                seguir_registrando = False

        # Reportes solicitados en el enunciado
        mostrar_reportes(arreglo_clientes)

        # Ordenamiento por valor de atención de mayor a menor
        clientes_ordenados = ordenar_por_valor_atencion_desc(arreglo_clientes)
        mostrar_lista(clientes_ordenados, "Clientes ordenados por valor de atención (mayor a menor)")

        # Búsqueda por cédula en la lista ordenada (se repite hasta que el usuario escriba SALIR)
        print("\n--- Búsqueda de cliente por cédula ---")
        print("(Escriba 'SALIR' en cualquier momento para terminar la búsqueda)")
        while True:
            cedula_buscar = leer_cedula_o_salir("Ingrese la cédula a buscar: ")
            if cedula_buscar == "SALIR":
                print("Búsqueda finalizada.")
                break

            encontrado, comparaciones = buscar_por_cedula(clientes_ordenados, cedula_buscar)
            if encontrado:
                valor_fmt = f"${encontrado.calcular_valor_a_pagar():,}".replace(",", ".")
                print(f"\nCliente encontrado: {encontrado.nombre} | Valor a pagar: {valor_fmt} | "
                      f"Comparaciones realizadas: {comparaciones}")
            else:
                print(f"\nNo se encontró ningún cliente con esa cédula. Comparaciones realizadas: {comparaciones}")

    except Exception as error:
        # Red de seguridad final: ningún error no previsto debe cerrar el programa de golpe con una traza de error para el usuario final. Esto lo conseguí en la documentación de python https://docs.python.org/es/3/tutorial/errors.html
        print(f"\nOcurrió un error inesperado: {error}")
        print("El programa se cerrará de forma segura.")


if __name__ == "__main__":
    main()
