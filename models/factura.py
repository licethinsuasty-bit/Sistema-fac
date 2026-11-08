class Factura:

    def __init__(self, numero, nit_cliente, fecha, subtotal, iva_total, total, estado):
        self.numero = numero
        self.nit_cliente = nit_cliente
        self.fecha = fecha
        self.subtotal = subtotal
        self.iva_total = iva_total
        self.total = total
        self.estado = estado