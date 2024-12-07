from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

sky = Sky()

ground = Entity(model="plane", scale=50, color=color.gray, texture="/assets/ground.png", collider="box")

player = FirstPersonController()
player.speed = 5
player.jump_height = 2

all_opponents = []
opponents_length = 10
for _ in range(opponents_length):
    x, y, z = random.randint(-20, 20), 1, random.randint(-20, 20)
    opponent = Entity(model="sphere", color=color.yellow, scale=1, position=(x, y, z), collider="sphere")
    all_opponents.append(opponent)

timer_text = Text(text="Time: 30", position=(-0.10, 0.45), scale=2)
time_left = 30

app.run()