from models.factura import Factura


class FacturaService:

    def __init__(self, repository):
        self.repository = repository

    def registrar(self, numero, nit_cliente, fecha, subtotal, iva_total, total, estado):

        factura = Factura(
            numero,
            nit_cliente,
            fecha,
            subtotal,
            iva_total,
            total,
            estado
        )

        self.repository.guardar(factura)

    def listar(self):
        return self.repository.listar()