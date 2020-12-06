from bangtal import *
from mod1 import *

class Scene_m(Scene):
    def __init__(self, name, file, bgm="None", Loop=False):
        super().__init__(name, file)
        if bgm != "None":
            self.bgm = Sound(bgm)
        else:
            self.bgm = "None"

        self.image = file
        self.loop = Loop

    def onEnter(self):
        if self.bgm != "None":
            self.bgm.play(loop=self.loop)

    def onLeave(self):
        if self.bgm != "None":
            self.bgm.stop()


class Attack_sound(Sound):
    def __init__(self, file, ent_scene):
        super().__init__(file)
        self.sound = file
        self.scene = ent_scene

    def onCompleted(self):
        self.scene.enter()


class Button1(Object):
    buttons = []

    def __init__(self, enemy):
        super().__init__("./Images/buttons/button_1.png")
        self.enemy = enemy
        self.locate(enemy.scene, 100, 300)
        Button1.buttons.append(self)

    def onMouseAction(self, x, y, action):
        self.enemy.ans = 1
        for i in range(len(Button1.buttons)):
            Button1.buttons[i].hide()
            Button2.buttons[i].hide()
            Button3.buttons[i].hide()
        self.enemy.attack()


class Button2(Object):
    buttons = []

    def __init__(self, enemy):
        super().__init__("./Images/buttons/button_2.png")
        self.enemy = enemy
        self.locate(enemy.scene, 100, 250)
        Button2.buttons.append(self)

    def onMouseAction(self, x, y, action):
        self.enemy.ans = 2
        for i in range(len(Button1.buttons)):
            Button1.buttons[i].hide()
            Button2.buttons[i].hide()
            Button3.buttons[i].hide()
        self.enemy.attack()


class Button3(Object):
    buttons = []

    def __init__(self, enemy):
        super().__init__("./Images/buttons/button_3.png")
        self.enemy = enemy
        self.locate(enemy.scene, 100, 200)
        Button3.buttons.append(self)

    def onMouseAction(self, x, y, action):
        self.enemy.ans = 3
        for i in range(len(Button1.buttons)):
            Button1.buttons[i].hide()
            Button2.buttons[i].hide()
            Button3.buttons[i].hide()
        self.enemy.attack()