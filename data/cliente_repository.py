from database.conexion import Conexion


class ClienteRepository:

    def guardar(self, cliente):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO clientes
        (nit, nombre, correo, direccion, telefono, estado)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            cliente.nit,
            cliente.nombre,
            cliente.correo,
            cliente.direccion,
            cliente.telefono,
            cliente.estado
        ))

        conexion.commit()
        conexion.close()

    def listar(self):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM clientes")

        clientes = cursor.fetchall()

        conexion.close()

        return clientes