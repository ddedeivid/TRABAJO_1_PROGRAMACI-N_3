TIPOS_CLIENTE = ["Particular", "EPS", "Prepagada"]
TIPOS_ATENCION = ["Limpieza", "Calzas", "Extracción", "Diagnóstico"]
PRIORIDADES = ["Normal", "Urgente"]

# Cantidad automática (fija) para las atenciones que siempre son 1
CANTIDAD_FIJA = {"Limpieza": 1, "Diagnóstico": 1}

VALOR_CITA = {
    "Particular": 80000,
    "EPS": 5000,
    "Prepagada": 30000
}

VALOR_ATENCION = {
    "Particular": {"Limpieza": 60000, "Calzas": 80000, "Extracción": 100000, "Diagnóstico": 50000},
    "EPS":        {"Limpieza": 0,     "Calzas": 40000, "Extracción": 40000,  "Diagnóstico": 0},
    "Prepagada":  {"Limpieza": 0,     "Calzas": 10000, "Extracción": 10000,  "Diagnóstico": 0}
}


def obtener_valor_cita(tipo_cliente):
    return VALOR_CITA[tipo_cliente]


def obtener_valor_atencion(tipo_cliente, tipo_atencion):
    return VALOR_ATENCION[tipo_cliente][tipo_atencion]


def obtener_cantidad_fija(tipo_atencion):
    """Devuelve 1 si la atención tiene cantidad fija (Limpieza/Diagnóstico),
    o None si la cantidad debe ser preguntada al usuario (Calzas/Extracción)."""
    return CANTIDAD_FIJA.get(tipo_atencion)
