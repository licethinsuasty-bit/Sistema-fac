class DetalleFactura:

    def __init__(self, numero_factura, codigo_producto, cantidad, precio_unitario, iva, subtotal):
        self.numero_factura = numero_factura
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.iva = iva
        self.subtotal = subtotal