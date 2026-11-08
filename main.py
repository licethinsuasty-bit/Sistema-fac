from data.cliente_repository import ClienteRepository
from data.producto_repository import ProductoRepository
from data.factura_repository import FacturaRepository
from data.detalle_factura_repository import DetalleFacturaRepository

from business.cliente_service import ClienteService
from business.producto_service import ProductoService
from business.factura_service import FacturaService
from business.detalle_factura_service import DetalleFacturaService

from presentation.cliente_controller import ClienteController
from presentation.producto_controller import ProductoController
from presentation.factura_controller import FacturaController
from presentation.consulta_controller import ConsultaController

# Crear repositorios
cliente_repository = ClienteRepository()
producto_repository = ProductoRepository()
factura_repository = FacturaRepository()
detalle_repository = DetalleFacturaRepository()

# Crear servicios
cliente_service = ClienteService(cliente_repository)
producto_service = ProductoService(producto_repository)
factura_service = FacturaService(factura_repository)
detalle_service = DetalleFacturaService(detalle_repository)

# Crear controladores
cliente_controller = ClienteController(cliente_service)
producto_controller = ProductoController(producto_service)
factura_controller = FacturaController(factura_service)
consulta_controller = ConsultaController(factura_service)

while True:

    print("\n===============================")
    print(" SISTEMA DE FACTURACIÓN")
    print("===============================")
    print("1. Registrar cliente")
    print("2. Registrar producto")
    print("3. Registrar factura")
    print("4. Listar clientes")
    print("5. Listar productos")
    print("6. Listar facturas")
    print("7. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        cliente_controller.registrar()

    elif opcion == "2":
        producto_controller.registrar()

    elif opcion == "3":
        factura_controller.registrar()

    elif opcion == "4":
        cliente_controller.listar()

    elif opcion == "5":
        producto_controller.listar()

    elif opcion == "6":
        consulta_controller.listar_facturas()

    elif opcion == "7":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción no válida.")