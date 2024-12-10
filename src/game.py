from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

window.fullscreen = True

sky = Sky()

light = DirectionalLight()
light.rotation = (45, 0, 0)  
light.intensity = 2.5
light.color = color.white

ambient_light = AmbientLight(color=color.white, intensity=0.1)

heightmap_texture = load_texture("/assets/textures/heightmap.png")
ground_size = 500
ground = Entity(
    model=Terrain(heightmap_texture, skip=15), 
    scale=(ground_size, 20, ground_size), 
    color=color.gray,
    texture="/assets/rocky_terrain_02_diff_2k.jpg",
    texture_scale=(200, 200),
    collider="mesh",
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
    scale=(3.5, 2.5, 2.5)  
)

opponent_speed = 30
def move_opponent(opponent):
    x, y, z = random.randint(-400, 400), 0, random.randint(-400, 400)
    direction = (Vec3(x, y, z) - opponent.position).normalized()
    opponent.rotation_y = -math.atan2(direction.x, direction.z) * (180 / math.pi)
    opponent.animate("position", (x, y, z), duration=opponent_speed, curve=curve.linear)
    invoke(move_opponent, opponent, delay=2)

all_opponents = []
opponents_length = 10
for _ in range(opponents_length):
    x, y, z = random.randint(-400, 400), 0, random.randint(-400, 400)
    opponent = Entity(
        model="/assets/models/monster.glb",
        scale=1,  
        position=(x, y, z),  
        collider="box",
    )

    move_opponent(opponent)
    
    all_opponents.append(opponent)

game_name = Text(
    text="Kill The Monster", 
    position=(-0.16, -0.40),
    scale=2,
    font="assets/fonts/Crused Marrie.ttf")

timer_text = Text(text="Time: 30", position=(-0.13, 0.45), scale=2)
time_left = 100

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

def timer():
    global time_left
    
    if time_left > 0:
        time_left -= time.dt
        timer_text.text = f"Time: {int(time_left)}"
    else:
        timer_text.text = "Game Over"
        quit()

def update():
    global time_left, score

    timer()

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

    bullets_to_destroy = []
    for bullet in bullets:
        if bullet.visible and (
                abs(bullet.position.x) > ground_size - 100 or
                abs(bullet.position.z) > ground_size - 100
            ):
            bullets_to_destroy.append(bullet)

    for bullet in bullets_to_destroy:
        bullet.visible = False
        destroy(bullet)
        bullets.remove(bullet)

    if held_keys["w"] and held_keys["shift"]:
        player.speed = 20
    else:
        player.speed = 5

tree_length = 50
for _ in range(tree_length):
    x, y, z = random.randint(-200, 200), 6, random.randint(-200, 200)
    tree = Entity(
        model="/assets/models/tree.glb",
        scale=1.5,  
        position=(x, y, z),
        rotation=(0, y, 0),
        collider="box",
    )

house_length = 10
for _ in range(house_length):
    x, y, z = random.randint(-200, 200), 0, random.randint(-200, 200)
    home = Entity(
        model="/assets/models/low_poly_house.glb",
        scale=2.5,  
        position=(x, y, z), 
        rotation=(0, y, 0),
        collider="box",
    )

app.run()