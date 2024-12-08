from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

sky = Sky()

light = DirectionalLight()
light.rotation = (45, 0, 0)

ground = Entity(model="plane", scale=50, color=color.gray, texture="/assets/ground.png", collider="box")

player = FirstPersonController()
player.speed = 5
player.jump_height = 2

def move_opponent(opponent):
    x, y, z = random.randint(-20, 20), 0, random.randint(-20, 20)
    opponent.animate("position", (x, y, z), duration=5, curve=curve.linear)
    invoke(move_opponent, opponent, delay=2)

all_opponents = []
opponents_length = 10
for _ in range(opponents_length):
    x, y, z = random.randint(-20, 20), 0, random.randint(-20, 20)
    opponent = Entity(
        model="/assets/models/monster.glb",
        scale=80,  
        position=(x, y, z),  
        collider="box",
        color=color.gray
    )

    move_opponent(opponent)
    
    all_opponents.append(opponent)

game_name = Text(
    text="Kill The Monster", 
    position=(-0.16, -0.40),
    scale=2,
    font="assets/fonts/Crused Marrie.ttf")

timer_text = Text(text="Time: 30", position=(-0.13, 0.45), scale=2)
time_left = 30

score = 0
score_text = Text(f"Score: {score}", position=(-0.10, 0.40), scale=1.5, color=color.red)

bullet = Entity(model="sphere", color=color.lime, scale=0.3, visible=False, collider="sphere", speed=100)
bullets = []

def shoot():
    new_bullet = Entity(model="sphere", color=color.lime, scale=0.3, visible=True, collider="sphere", speed=100)
    new_bullet.position = player.position + Vec3(0, 1.5, 0)
    new_bullet.rotation = player.rotation
    new_bullet.collider = "sphere"
    bullets.append(new_bullet)

def update():
    for bullet in bullets:
        bullet.position += bullet.forward * bullet.speed * time.dt  
        
    if mouse.left:
        shoot()

app.run()