import rodi
import time


walle = rodi.RoDI()
while True:
    direccion = (input("escrb"))
    if direccion == "f":
        walle.move_forward()
    elif direccion == "s":
        walle.move_stop()
    elif direccion == "l":
        walle.move_left()
        time.sleep(0.5)
    elif direccion == "r":
        walle.move_right()
        time.sleep(0.5)
    elif direccion == "end":
        walle.move_stop()
        print("Adios, hasta la proxima")
    else:
        print("sin ordenes jefe")
        walle.move_stop()