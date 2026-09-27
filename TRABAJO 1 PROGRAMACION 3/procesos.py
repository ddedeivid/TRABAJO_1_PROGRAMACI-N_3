def calcular_total_clientes(arreglo_clientes):
    return len(arreglo_clientes)


def calcular_ingresos_totales(arreglo_clientes):
    return sum(cliente.calcular_valor_a_pagar() for cliente in arreglo_clientes)


def contar_por_tipo_atencion(arreglo_clientes, tipo_atencion):
    return sum(1 for cliente in arreglo_clientes if cliente.tipo_atencion == tipo_atencion)


def ordenar_por_valor_atencion_desc(arreglo_clientes):
    """Ordenamiento burbuja (manual) sobre una copia del arreglo, de mayor a menor."""
    arreglo = arreglo_clientes.copy()
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arreglo[j].valor_atencion_unitario < arreglo[j + 1].valor_atencion_unitario:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo


def buscar_por_cedula(arreglo_clientes, cedula_buscada):
    """Búsqueda lineal, igual que buscar_producto_lineal en busqueda.py.
    Devuelve el cliente encontrado (o None) y el número de comparaciones realizadas."""
    comparaciones = 0
    for cliente in arreglo_clientes:
        comparaciones += 1
        if cliente.cedula == cedula_buscada:
            return cliente, comparaciones
    return None, comparaciones


def mostrar_reportes(arreglo_clientes):
    print("           REPORTE GENERAL")
    print(f"1. Total de clientes atendidos: {calcular_total_clientes(arreglo_clientes)}")
    print(f"2. Ingresos totales recibidos: ${calcular_ingresos_totales(arreglo_clientes):,}".replace(",", "."))
    print(f"3. Clientes que van para extracción de dientes: {contar_por_tipo_atencion(arreglo_clientes, 'Extracción')}")


def mostrar_lista(arreglo_clientes, titulo="Listado de clientes"):
    print(f"\n--- {titulo} ---")
    if not arreglo_clientes:
        print("No hay clientes registrados.")
        return
    for cliente in arreglo_clientes:
        valor_atencion_fmt = f"${cliente.valor_atencion_unitario:,}".replace(",", ".")
        valor_pagar_fmt = f"${cliente.calcular_valor_a_pagar():,}".replace(",", ".")
        print(f"Cédula: {cliente.cedula} | {cliente.nombre} | {cliente.tipo_cliente} | "
              f"{cliente.tipo_atencion} x{cliente.cantidad} | Valor atención: {valor_atencion_fmt} | "
              f"Total a pagar: {valor_pagar_fmt}")
