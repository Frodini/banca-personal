import sqlite3

from models.movimiento import Movimiento


def guardar_movimiento(movimiento):
    conexion = sqlite3.connect("data/banca_personal.db")

    conexion.execute(
        """
        INSERT INTO movimientos (
            cuenta,
            fecha_operacion,
            fecha_valor,
            concepto,
            descripcion,
            referencia,
            importe,
            saldo
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            "****5813",
            movimiento.fecha_operacion,
            movimiento.fecha_valor,
            movimiento.concepto,
            movimiento.descripcion,
            movimiento.referencia,
            movimiento.importe,
            movimiento.saldo,
        ),
    )

    conexion.commit()
    conexion.close()


def obtener_movimientos():
    conexion = sqlite3.connect("data/banca_personal.db")

    resultado = conexion.execute("""
        SELECT
            id,
            cuenta,
            fecha_operacion,
            fecha_valor,
            concepto,
            descripcion,
            referencia,
            importe,
            saldo
        FROM movimientos    
    """)

    movimientos = resultado.fetchall()

    conexion.close()

    return movimientos
