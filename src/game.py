from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

sky = Sky()

light = DirectionalLight()
light.rotation = (45, 0, 0)  
light.intensity = 2.5
light.color = color.white


ground = Entity(
    model="plane", 
    scale=500,
    color=color.gray,
    texture="/assets/ground.png",
    texture_scale=(30, 30),
    collider="box",
    double_sided=True
)

player = FirstPersonController()
player.speed = 5
player.jump_height = 2

gun = Entity(
    model="/assets/models/gun.glb",
    parent=camera,
    position=(0.5, -0.6, 0.8),
    color=color.gray,  
    rotation=(5, 180, 0), 
    scale=2.5  
)

def move_opponent(opponent):
    x, y, z = random.randint(-100, 100), 0, random.randint(-100, 100)
    opponent.animate("position", (x, y, z), duration=5, curve=curve.linear)
    invoke(move_opponent, opponent, delay=2)

all_opponents = []
opponents_length = 10
for _ in range(opponents_length):
    x, y, z = random.randint(-30, 30), 0, random.randint(-30, 30)
    opponent = Entity(
        model="/assets/models/monster.glb",
        scale=80,  
        position=(x, y, z),  
        collider="box",
        color=color.red
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

bullet_speed = 1000
bullet = Entity(model="sphere", color=color.lime, scale=0.3, visible=False, collider="sphere", speed=bullet_speed)
bullets = []

def shoot():
    new_bullet = Entity(model="sphere", color=color.lime, scale=0.3, visible=True, collider="sphere", speed=bullet_speed)
    new_bullet.position = player.position + Vec3(0, 1.5, 0)
    new_bullet.rotation = player.rotation
    new_bullet.collider = "sphere"
    bullets.append(new_bullet)

def update():
    global time_left, score

    if time_left > 0:
        time_left -= time.dt
        timer_text.text = f"Time: {int(time_left)}"
    else:
        timer_text.text = "Game Over"
        quit()

    to_remove = [] 
    for oppenent in all_opponents:
        for bullet in bullets:
            if bullet.visible and bullet.intersects(oppenent).hit:
                oppenent.disable()
                to_remove.append(oppenent)
                score += 1
                score_text.text = f"Score: {score}"

    for oppenent in to_remove:
        if oppenent in all_opponents:
            all_opponents.remove(oppenent)
            
    for bullet in bullets:
        bullet.position += bullet.forward * bullet.speed * time.dt  
        
    if mouse.left:
        shoot()

    for bullet in bullets:
        if bullet.visible and (bullet.position.x > 50 or bullet.position.x < -50 or bullet.position.z > 50 or bullet.position.z < -50):
            bullet.visible = False

    if held_keys["w"] and held_keys["shift"]:
        player.speed = 20  # Increase speed when Sprinting
    else:
        player.speed = 5

app.run()