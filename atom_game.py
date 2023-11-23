from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import basic_lighting_shader
from direct.actor.Actor import Actor
import sys
app = Ursina()

class Voxel(Entity):
    def __init__(self, position=(0,0,0), scale=(0, 0, 0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='floor_V.png',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            scale=scale,
            collider='box', shader=basic_lighting_shader
        )

for x in range(-100, 100, 5):
    for z in range(-100, 0, 5):
        voxel = Voxel(position=(x, 0, z), scale=(5, 1, 5))

player = FirstPersonController(y=20, height=5)
player.jump_up_duration = 1.9
player.gravity = 0.5
player.mouse_sensitivity = (100, 100)
player.speed = 17
player.height = 5
player.y = 40
player.x = 50
player.jump_height = 6

blend = Entity(texture='Безымянный.png', model='untitled233', x=0, y=0, z=0, shader=lit_with_shadows_shader)

floor_for_player = Voxel(position=(0, 0, 0), scale=(3, 1, 3))
floor_for_player.y = 10

# floor_for_player.visible = False
lazer = Entity(model='cube', parent=camera, color=color.orange, scale=(0.5, 0.5, 200), position=(0, -0.5, 0), enabled=False, shader=lit_with_shadows_shader)
gun = Entity(visible=False, on_cooldown=False, y=100)

pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True)
e = Entity()

actor = Actor('untitled.glb')
print(actor.getAnimNames())
actor.reparentTo(Entity())

actor.play('aaa')
print(actor.getAnimNames())
def shoot():
    global lazer_fly
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
    if player.y < -40: sys.exit()

sky = Sky()

app.run()
