from database.conexion import Conexion


class FacturaRepository:

    def guardar(self, factura):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO facturas
        (numero, nit_cliente, fecha, subtotal, iva_total, total, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            factura.numero,
            factura.nit_cliente,
            factura.fecha,
            factura.subtotal,
            factura.iva_total,
            factura.total,
            factura.estado
        ))

        conexion.commit()
        conexion.close()

    def listar(self):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM facturas")

        facturas = cursor.fetchall()

        conexion.close()

        return facturas