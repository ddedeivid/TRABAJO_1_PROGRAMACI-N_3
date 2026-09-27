class Cliente:
    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion,
                 cantidad, prioridad, fecha_cita, valor_atencion_unitario, valor_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita
        self.valor_atencion_unitario = valor_atencion_unitario
        self.valor_cita = valor_cita

    def calcular_valor_a_pagar(self):
        # Valor a pagar = valor de la cita + (valor de la atención * cantidad)
        return self.valor_cita + (self.valor_atencion_unitario * self.cantidad)

    def __repr__(self):
        return (
            f"Cliente(cedula={self.cedula}, nombre={self.nombre}, "
            f"tipo_cliente={self.tipo_cliente}, tipo_atencion={self.tipo_atencion}, "
            f"cantidad={self.cantidad}, valor_atencion_unitario={self.valor_atencion_unitario}, "
            f"valor_cita={self.valor_cita})"
        )
