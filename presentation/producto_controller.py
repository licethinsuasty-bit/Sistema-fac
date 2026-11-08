from business.producto_service import ProductoService


class ProductoController:

    def __init__(self, service):
        self.service = service

    def registrar(self):

        codigo = input("Código: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio unitario: "))
        stock = int(input("Stock disponible: "))
        iva = float(input("IVA (%): "))

        self.service.registrar(
            codigo,
            descripcion,
            precio,
            stock,
            iva
        )

        print("\nProducto registrado correctamente.\n")

    def listar(self):

        productos = self.service.listar()

        print("\n===== PRODUCTOS =====")

        for producto in productos:
            print(producto)