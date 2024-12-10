# **Game Documentation for 3D Shooting Game**

## **1. Game Overview**

**Title**: Kill The Monster I

**Platform**: PC (Windows, macOS, Linux)

**Engine**: Ursina Game Engine

**Genre**: First-Person Shooter (FPS)

**Description**:
This game is a fast-paced 3D first-person shooter where players can engage in combat with enemies while navigating through a dynamic 3D environment. The game includes realistic shooting mechanics, dynamic AI enemies, environmental features such as fog, day/night cycles, and interactive terrain. The game also includes sound effects, including gunshots and background music, to enhance the gaming experience.

---

## **2. Setup and Installation**

### **Prerequisites**:

- Python 3.12 or later
- Ursina Game Engine
- Basic understanding of Python programming

### **Installation Steps**:

1. **Install Python**: Ensure Python 3.12 or later is installed on your system. You can download Python from [here](https://www.python.org/downloads/).
2. **Install Ursina**: Use pip to install the Ursina engine.

   ```bash
   pip install ursina
   ```

3. **Download or Clone the Game**:

   - Clone the repository or download the game files from the source.
   - Clone via Git:

   ```bash
   git clone https://github.com/usmonovshohruxmirzo/kill-the-monsters-3d.git
   cd kill-the-monsters-3d
   ```

4. **Run the Game**:
   Run the main game script with Python.

   ```bash
   python game.py
   ```

---

## **3. Game Controls**

- **Movement**:

  - `W` = Move Forward
  - `S` = Move Backward
  - `A` = Move Left
  - `D` = Move Right
  - `Space` = Jump

- **Mouse**:
  - `Left Mouse Click` = Shoot
  - `Right Mouse Click` = Aim Down Sights (optional)
- **Camera Control**:

  - Use the mouse to look around.

- **Reloading**:

  - `R` = Reload weapon

- **Pause Menu**:
  - `Esc` = Pause the game

---

## **4. Game Features**

### **Shooting**:

- Players can shoot bullets by clicking the left mouse button.
- Bullets are created at the player's current position and travel in the direction the player is facing.

### **Enemy AI**:

- The game includes basic AI for enemies that move randomly across the terrain.
- AI uses a simple algorithm to choose a destination point and move toward it.

### **Sound Effects**:

- Each time the player shoots, a gunshot sound is played.
- Ambient sounds are used to enhance the atmosphere of the game.

### **Fog**:

- A dynamic fog system reduces visibility at longer distances, making the environment more immersive.

### **Bullet and Collision Handling**:

- Bullets are instantiated and move toward their target.
- If a bullet intersects with an enemy or object, it gets destroyed or the enemy takes damage.

---

## **5. Game Assets**

### **Textures**:

- **Ground Texture**: `ground.png` (Diffuse texture)
- **Weapon Model**: `gun.glb`
- **Bullet Model**: `sphere`
- **Enemy Models**: Placeholder models or custom 3D models for enemies.

### **Sounds**:

- **Gunshot Sound**: `gunshot.wav`
- **Ambient Sound**: `ambient_music.mp3`
- **Hit Sound**: `hit_sound.wav`

---

## **6. Code Overview**

### **Game Loop**:

The game operates in a continuous loop that updates player movements, AI actions, and interactions with the environment.

- **Player Movement**: Captures input from the keyboard and moves the player accordingly.
- **Enemy AI**: The AI moves randomly, changes direction when it reaches its destination, and occasionally reacts to the player.
- **Shooting**: A bullet is instantiated when the player clicks the mouse, and it moves in the direction the player is facing.

### **Shooting Mechanism**:

```python
def shoot():
    new_bullet = Entity(model="sphere", color=color.lime, scale=0.3, visible=True, collider="sphere", speed=bullet_speed)
    new_bullet.position = player.position + Vec3(0, 1.5, 0)
    new_bullet.rotation = player.rotation
    new_bullet.collider = "sphere"
    bullets.append(new_bullet)
```

### **Movement and Rotation of Opponent AI**:

```python
def move_opponent(opponent):
    x, y, z = random.randint(-100, 100), 0, random.randint(-100, 100)
    direction = (Vec3(x, y, z) - opponent.position).normalized()
    opponent.rotation_y = math.atan2(direction.z, direction.x) * (180 / math.pi)
    opponent.animate("position", (x, y, z), duration=20, curve=curve.linear)
    invoke(move_opponent, opponent, delay=2)
```

---

## **7. Known Issues and Limitations**

- **Enemy AI**: Currently basic and can get stuck in certain areas.
- **Gun Reload**: The reload mechanic is not fully functional, and ammo count is not yet implemented.
- **Fog Performance**: On lower-end systems, the dynamic fog effect may cause slight performance issues.
- **Collision Detection**: Some minor issues in collision detection for fast-moving bullets and small objects.

---

## **8. Future Updates**

- **Improved Enemy AI**: The AI will be enhanced with better pathfinding and more complex behaviors.
- **Multiplayer Mode**: The game will include support for local multiplayer.
- **Advanced Graphics**: More advanced lighting, shading, and particle effects will be implemented to improve visual quality.
- **Customization**: The player will be able to customize their weapons and character.

---

## **9. Troubleshooting**

### **Common Issues**:

- **No Sound**:

  - Make sure the sound files are correctly loaded and paths are correct.
  - Check if the sound volume is turned up in the system settings.

- **Lag/Performance Issues**:
  - Lower the graphical settings in the game options menu.
  - Ensure your system meets the minimum requirements for the game.

---

## **10. Contributors**

- **Lead Developer**: Usmonov Shoxruxmirzo
- **Sound Designer**: Usmonov Shoxruxmirzo
- **3D Artist**: Usmonov Shoxruxmirzo
- **Tester**: Usmonov Shoxruxmirzo

---

## **11. License**

This game is released under the MIT [License](/LICENSE).

---

### **Notes**:

- **Gameplay Tweaks**: The controls and mechanics can be adjusted for a better user experience or if more features are added.
- **Performance Tuning**: Optimizations are ongoing for improving performance on lower-end machines, especially with fog and lighting effects.

---

### **Next Steps**:

1. **Expand Game Features**: Implement advanced AI, multiplayer support, and more interactive environments.
2. **Graphical Updates**: Improve textures, lighting, and visual effects.
3. **Sound Design**: Add more immersive sound effects, such as environmental noises and advanced weapon sounds.
