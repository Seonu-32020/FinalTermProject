from bangtal import *
from mod2 import *

class Picked:
    book = 0
    assignment = 0
    key = 0
    engine = 0


class Item(Object):
    def __init__(self, file, item_scene, x, y, name="None", show=1):
        super().__init__(file)
        if name != "None":
            self.name = name
        else:
            self.name = "None"
        self.image = file
        self.scene = item_scene
        self.x = x
        self.y = y

        self.locate(self.scene, self.x, self.y)
        if show == 1:
            self.show()
        self.btn_y = Button_y("./Images/buttons/button_yes.png", self.scene, self, 100, 300)
        self.btn_n = Button_n("./Images/buttons/button_no.png", self.scene, self, 100, 250)

    def onMouseAction(self, x, y, action):
        if self.name != "None":
            txt = self.name + "을(를) 줍는다"
            showMessage(txt)
            if self.name == "물리학 서적":
                Picked.book = 1
            elif self.name == "미리 해놓은 과제":
                Picked.assignment = 1
            elif self.name == "의문의 열쇠":
                Picked.key = 1

        self.btn_y.show()
        self.btn_n.show()


class Enemy(Object):
    choices = []
    mob = []

    def __init__(self, file, file_big, name, enemy_scene, x, y, ans, show=1, bgm="None", Loop=False):
        super().__init__(file)
        self.image = file
        self.fightimg = file_big
        self.big = file_big
        self.scene = enemy_scene
        self.x, self.y = x, y
        self.loop = Loop
        self.name = name
        self.picks = ""
        self.atsound = ""
        self.attxt = ""
        self.ans = 0
        self.correctans = ans

        self.locate(self.scene, self.x, self.y)
        self.dead = 0

        if bgm != "None":
            self.bgm = Sound(bgm)

        if show == 1:
            self.show()

        self.btn1 = Button1(self)
        self.btn2 = Button2(self)
        self.btn3 = Button3(self)

    def __str__(self):
        return str(self.name)

    def onMouseAction(self, x, y, action):
        if self.bgm != "None":
            self.bgm.play(loop=self.loop)
        self.setImage(self.fightimg)
        self.locate(self.scene, 640, 0)
        self.picks.locate(self.scene, 0, 320)
        self.picks.show()
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()

        txt = self.name + " 등장!\n어떻게 행동해야하지?"
        showMessage(txt)

    def battle_end(self):
        self.picks.hide()
        self.hide()
        showMessage("옳은 선택이었다!")

    def attack(self):
        if self.ans == 1 and self.ans == self.correctans:
            self.battle_end()

        elif self.ans == 2 and self.ans == self.correctans:
            if Picked.assignment == 1:
                self.battle_end()
            else:
                txt = "미리 과제를 하지 않았다...\n" + self.attxt
                showMessage(txt)
                self.atsound.play(loop=False)

        elif self.ans == 3 and self.ans == self.correctans:
            if Picked.book == 1:
                self.battle_end()
            else:
                txt = "물리학 책이 없다...\n" + self.attxt
                showMessage(txt)
                self.atsound.play(loop=False)

        else:
            txt = "틀린 선택이었다...\n"+self.attxt
            showMessage(txt)
            self.atsound.play(loop=False)

class Button_y(Object):
    buttons = []

    def __init__(self, file, button_scene, pick_item, x=100, y=100, show=0):
        super().__init__(file)
        Button_y.buttons.append(self)
        self.scene = button_scene
        self.x = x
        self.y = y
        self.sound = Sound("./Sounds/Effect/button_basic.wav")
        self.locate(self.scene, self.x, self.y)
        self.item = pick_item
        if show == 1:
            self.show()

    def onMouseAction(self, x, y, action):
        self.sound.play(loop=False)
        self.item.pick()
        for i in range(len(Button_n.buttons)):
            Button_n.buttons[i].hide()
        for i in range(len(Button_y.buttons)):
            Button_y.buttons[i].hide()


class Button_n(Object):
    buttons = []

    def __init__(self, file, button_scene, pick_item, x=100, y=100, show=0):
        super().__init__(file)
        Button_y.buttons.append(self)
        self.scene = button_scene
        self.x = x
        self.y = y
        self.sound = Sound("./Sounds/Effect/button_basic.wav")
        self.locate(self.scene, self.x, self.y)
        if show == 1:
            self.show()

    def onMouseAction(self, x, y, action):
        self.sound.play(loop=False)
        for i in range(len(Button_n.buttons)):
            Button_n.buttons[i].hide()
        for i in range(len(Button_y.buttons)):
            Button_y.buttons[i].hide()


class Button_act(Object):
    def __init__(self, file, scene, nextscene="None", x=100, y=100, show=1):
        super().__init__(file)
        self.image = file
        if file == "None":
            print("can't find img file")

        self.scene = scene
        self.nextscene = nextscene
        self.x = x
        self.y = y
        self.sound = Sound("./Sounds/Effect/button_basic.wav")
        self.locate(scene, x, y)
        if show == 1:
            self.show()

    def onMouseAction(self, x, y, action):
        self.sound.play(loop=False)
        if self.nextscene == "end":
            endGame()
        elif self.nextscene == "None":
            pass
        else:
            self.nextscene.enter()

class Button_Move(Object):
    def __init__(self, direction, scene_now, scene_next, x=0, y=0, show=1):
        self.image = "./Images/a"+str(direction)+".png"
        super().__init__(self.image)

        self.dir = direction
        self.scene = scene_now
        self.next = scene_next

        if direction == 8:
            self.locate(self.scene, 590, 610)
        elif direction == 6:
            self.locate(self.scene, 1170, 310)
        elif direction == 2:
            self.locate(self.scene, 590, 0)
        elif direction == 4:
            self.locate(self.scene, 0, 310)

        if show == 1:
            self.show()

    def onMouseAction(self, x, y, action):
        if self.dir == 8 and self.scene.image == "./Images/scene_forest.jpg":
            if Picked.engine == 1:
                self.next.enter()
            else:
                showMessage("시동을 걸 수 없다!")

        else:
            self.next.enter()




#def Default_onMouseAction(object, x, y, action):

