from business.factura_service import FacturaService


class FacturaController:

    def __init__(self, service):
        self.service = service

    def registrar(self):

        numero = int(input("Número de factura: "))
        nit_cliente = input("NIT del cliente: ")
        fecha = input("Fecha (AAAA-MM-DD): ")
        subtotal = float(input("Subtotal: "))
        iva_total = float(input("IVA total: "))
        total = float(input("Total: "))
        estado = "Activa"

        self.service.registrar(
            numero,
            nit_cliente,
            fecha,
            subtotal,
            iva_total,
            total,
            estado
        )

        print("\nFactura registrada correctamente.\n")

    def listar(self):

        facturas = self.service.listar()

        print("\n===== FACTURAS =====")

        for factura in facturas:
            print(factura)