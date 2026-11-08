from conexion import Conexion

conexion = Conexion.conectar()
cursor = conexion.cursor()

# Tabla de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    nit TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL,
    direccion TEXT NOT NULL,
    telefono TEXT NOT NULL,
    estado TEXT NOT NULL
)
""")

# Tabla de productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    codigo TEXT PRIMARY KEY,
    descripcion TEXT NOT NULL,
    precio_unitario REAL NOT NULL,
    stock INTEGER NOT NULL,
    iva REAL NOT NULL
)
""")

# Tabla de facturas
cursor.execute("""
CREATE TABLE IF NOT EXISTS facturas (
    numero INTEGER PRIMARY KEY,
    nit_cliente TEXT NOT NULL,
    fecha TEXT NOT NULL,
    subtotal REAL NOT NULL,
    iva_total REAL NOT NULL,
    total REAL NOT NULL,
    estado TEXT NOT NULL,
    FOREIGN KEY (nit_cliente) REFERENCES clientes(nit)
)
""")

# Tabla de detalle de factura
cursor.execute("""
CREATE TABLE IF NOT EXISTS detalle_factura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_factura INTEGER NOT NULL,
    codigo_producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    iva REAL NOT NULL,
    subtotal REAL NOT NULL,
    FOREIGN KEY (numero_factura) REFERENCES facturas(numero),
    FOREIGN KEY (codigo_producto) REFERENCES productos(codigo)
)
""")

conexion.commit()
conexion.close()

print("Tablas creadas correctamente.")