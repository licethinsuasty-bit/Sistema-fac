from models.cliente import Cliente


class ClienteService:

    def __init__(self, repository):
        self.repository = repository

    def registrar(self, nit, nombre, correo, direccion, telefono, estado):

        cliente = Cliente(
            nit,
            nombre,
            correo,
            direccion,
            telefono,
            estado
        )

        self.repository.guardar(cliente)

    def listar(self):
        return self.repository.listar()