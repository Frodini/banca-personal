import sqlite3


def crear_base_de_datos():
    conexion = sqlite3.connect("data/banca_personal.db")

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cuenta TEXT NOT NULL,
            fecha_operacion TEXT NOT NULL,
            fecha_valor TEXT NOT NULL,
            concepto TEXT NOT NULL,
            descripcion TEXT,
            referencia TEXT,
            importe REAL NOT NULL,
            saldo REAL NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


crear_base_de_datos()
