import rodi
import time 

robot = rodi.RoDI()   # Instancia/crear el objeto RoDI

# Solución de Ara
def cuadrado (direcciones1, direcciones2):
    robot.move_forward()
    time.sleep(direcciones1)
    robot.move_stop()
    robot.move_left()
    time.sleep(direcciones2)
    robot.move_stop()

i = 0
while i != 4:
    cuadrado(4.3,0.5)
    i = i + 1

for movimiento in range(4):
    robot.move(20,100)
    #robot.move_forward()
    time.sleep(3)
    robot.move_right()
    time.sleep(0.5)
robot.move_stop()

robot.pixel(255,0,50)
time.sleep(5)
robot.pixel(0,0,0)

'''PEDIR AL USUARIO QUE INGRESE EL COLOR A ENCENDER
EJEMPLO
MENU 1 ---- ROJO
MENU 2 ---- AZUL 
MENU 3 ---- VERDE'''

# Solución de Edu
color1 = input("ELIJA UN COLOR: ROJO (1), VERDE(2), AZUL(3)")
if color1 == "1":
    robot.pixel(255,0,0)
    time.sleep(1)
    robot.pixel(0,0,0)
elif color1 == "2":
    robot.pixel(0,255,0)
    time.sleep(1)
    robot.pixel(0,0,0)
elif color1 == "3":
    robot.pixel(0,0,255)
    time.sleep(1)
    robot.pixel(0,0,0)
else:
    robot.pixel(255,255,255)
    time.sleep(1)
    robot.pixel(0,0,0)


while True:
    print(robot.see())
    time.sleep(0.1)}

