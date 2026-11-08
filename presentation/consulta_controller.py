class ConsultaController:

    def __init__(self, factura_service):
        self.factura_service = factura_service

    def listar_facturas(self):

        facturas = self.factura_service.listar()

        print("\n========== HISTORIAL DE FACTURAS ==========\n")

        if len(facturas) == 0:
            print("No existen facturas registradas.")
        else:
            for factura in facturas:
                print(factura)