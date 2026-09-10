class Movimiento:
    def __init__(
        self,
        fecha_operacion,
        fecha_valor,
        concepto,
        descripcion,
        referencia,
        importe,
        saldo,
    ):
        self.fecha_operacion = fecha_operacion
        self.fecha_valor = fecha_valor
        self.concepto = concepto
        self.descripcion = descripcion
        self.referencia = referencia
        self.importe = importe
        self.saldo = saldo
