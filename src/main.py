from models.movimiento import Movimiento
from services.movimiento_service import guardar_movimiento, obtener_movimientos


def main():
    print("Iniciando Banca Personal...")

    movimientos = obtener_movimientos()

    for movimiento in movimientos:
        print(movimiento)


if __name__ == "__main__":
    main()
