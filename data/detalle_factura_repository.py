from database.conexion import Conexion


class DetalleFacturaRepository:

    def guardar(self, detalle):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO detalle_factura
        (numero_factura, codigo_producto, cantidad, precio_unitario, iva, subtotal)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            detalle.numero_factura,
            detalle.codigo_producto,
            detalle.cantidad,
            detalle.precio_unitario,
            detalle.iva,
            detalle.subtotal
        ))

        conexion.commit()
        conexion.close()

    def listar(self):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM detalle_factura")

        detalles = cursor.fetchall()

        conexion.close()

        return detalles