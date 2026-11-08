from models.detalle_factura import DetalleFactura


class DetalleFacturaService:

    def __init__(self, repository):
        self.repository = repository

    def registrar(self, numero_factura, codigo_producto, cantidad, precio_unitario, iva, subtotal):

        detalle = DetalleFactura(
            numero_factura,
            codigo_producto,
            cantidad,
            precio_unitario,
            iva,
            subtotal
        )

        self.repository.guardar(detalle)

    def listar(self):
        return self.repository.listar()