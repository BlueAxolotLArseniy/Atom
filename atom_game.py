from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import sys
app = Ursina()

# ground = Entity(model='plane', texture='grass', scale=(10, 30), position=(0, 0, -20))
class Voxel(Entity):
    def __init__(self, position=(0,0,0), scale=(0, 0, 0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='floor_V.png',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            scale=scale,
            collider='box',
            texture_scale=(300, 300), shader=lit_with_shadows_shader
        )

voxel = Voxel(position=(37.5,0,0), scale=(75, 1, 150))
# voxel2 = Voxel(position=())

player = FirstPersonController(y=20, height=5)
player.jump_up_duration = 1.9
player.gravity = 0.5
player.mouse_sensitivity = (100, 100)
player.speed = 17
player.height = 5
player.y = 40
player.jump_height = 6
# mouse = Entity(model=Quad(scale=(3,1), thickness=3, segments=3, mode='line'), scale=(0.2, 0.3), parent=camera, position=(0, -0.5))
mouse_D = Entity(model=Quad(scale=(3,1), thickness=3, segments=3, mode='line'), scale=(0.2, 0.3), parent=camera, position=(0, -0.5))

camera.z -= 5


floor_for_player = Voxel(position=(0, 0, 0), scale=(1, 1, 1))
floor_for_player.y = 10
# floor_for_player.visible = False
lazer = Entity(model='cube', parent=camera, color=color.yellow, scale=(0.5, 0.5, 200), position=(0, -0.5, 0), enabled=False)
gun = Entity(visible=False, on_cooldown=False, y=100)

def shoot():
    if not gun.on_cooldown:
        gun.on_cooldown = True
        lazer.enabled = True
        invoke(lazer.disable, delay=.5)
        invoke(setattr, gun, 'on_cooldown', False, delay=.5)

def input(key):
    if key == 'q':
        sys.exit()
    if key == 'left mouse down':
        print('shoot')
        shoot()
    if key == 'z':
        print(camera)

def update():
    floor_for_player.x = player.x
    floor_for_player.z = player.z
    pass
sky = Sky()

app.run()
