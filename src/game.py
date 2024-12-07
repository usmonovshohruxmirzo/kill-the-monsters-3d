from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

ground = Entity(model="plane", scale=50, color=color.green, texture="/assets/ground.png", collider="box")

player = FirstPersonController()
player.speed = 5
player.jump_height = 2

app.run()