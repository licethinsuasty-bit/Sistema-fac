from models.producto import Producto


class ProductoService:

    def __init__(self, repository):
        self.repository = repository

    def registrar(self, codigo, descripcion, precio_unitario, stock, iva):

        producto = Producto(
            codigo,
            descripcion,
            precio_unitario,
            stock,
            iva
        )

        self.repository.guardar(producto)

    def listar(self):
        return self.repository.listar()