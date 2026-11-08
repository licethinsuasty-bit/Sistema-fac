from database.conexion import Conexion


class ProductoRepository:

    def guardar(self, producto):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO productos
        (codigo, descripcion, precio_unitario, stock, iva)
        VALUES (?, ?, ?, ?, ?)
        """, (
            producto.codigo,
            producto.descripcion,
            producto.precio_unitario,
            producto.stock,
            producto.iva
        ))

        conexion.commit()
        conexion.close()

    def listar(self):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")

        productos = cursor.fetchall()

        conexion.close()

        return productos