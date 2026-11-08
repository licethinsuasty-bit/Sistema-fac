from business.cliente_service import ClienteService


class ClienteController:

    def __init__(self, service):
        self.service = service

    def registrar(self):

        nit = input("NIT: ")
        nombre = input("Nombre o razón social: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")

        self.service.registrar(
            nit,
            nombre,
            correo,
            direccion,
            telefono,
            "Activo"
        )

        print("\nCliente registrado correctamente.\n")

    def listar(self):

        clientes = self.service.listar()

        print("\n===== CLIENTES =====")

        for cliente in clientes:
            print(cliente)