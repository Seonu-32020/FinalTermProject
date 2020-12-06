from bangtal import *
from mod1 import *
from mod2 import *

# setGameOption(GameOption.INVENTORY_BUTTON, False)
# setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)
setGameOption(GameOption.ROOM_TITLE, False)

# scene
scene_start = Scene_m("start", "./Images/scene_start.png", bgm="./Sounds/bgm/약탈의_춤사위.mp3", Loop=True)
scene_rule = Scene_m("rule", "./Images/BG_white720.png")

scene_space = Scene_m("space", "./Images/scene_space.png", bgm="./Sounds/UIsounds/Upper01.mp3")
scene_yard = Scene_m("yard", "./Images/scene_yard.jpg", bgm="./Sounds/Effect/step.mp3")
scene_lab = Scene_m("lab", "./Images/scene_lab.png", bgm="./Sounds/Effect/step.mp3")
scene_lib = Scene_m("lib", "./Images/scene_lib.jpg", bgm="./Sounds/Effect/step.mp3")
scene_forest = Scene_m("forest", "./Images/scene_forest.jpg", bgm="./Sounds/Effect/step.mp3")

# else
rocket = Object("./Images/rocket.png")
rocket.locate(scene_forest, 560, 100)
rocket.show()

endlight = Item("./Images/light.png", scene_space, 200, 360, "학사모")


# ending scene
scene_end_graduate = Scene_m("graduate end", "./Images/scene_graduate.png", bgm="./Sounds/bgm/graduate.mp3", Loop=True)
scene_end_bad = Scene_m("bad end", "./Images/scene_bad_end.png", bgm="./Sounds/bgm/end_8bit.mp3")
scene_end_army = Scene_m("military end", "./Images/scene_army.png", bgm="./Sounds/bgm/팔도사나이.mp3", Loop=True)

# button_act
button_start = Button_act("./Images/buttons/button_play.png", scene_start, scene_yard, 590, 300)
button_rule = Button_act("./Images/buttons/button_rule.png", scene_start, scene_rule, 590, 250)
button_exit = Button_act("./Images/buttons/button_exit.png", scene_start, scene_end_bad, 590, 200)
rule = Button_act("./Images/buttons/rule.png", scene_rule, scene_start, 340, 60)

button_end1 = Button_act("./Images/buttons/button_end.png", scene_end_bad, "end", 590, 100)
button_end2 = Button_act("./Images/buttons/button_end.png", scene_end_army, "end", 590, 100)
button_end3 = Button_act("./Images/buttons/button_end.png", scene_end_graduate, "end", 590, 100)

# button_move
yard_goLEFT = Button_Move(4, scene_yard, scene_lab)
yard_goRIGHT = Button_Move(6, scene_yard, scene_lib)
yard_goFORWARD = Button_Move(8, scene_yard, scene_forest)

lab_goRIGHT = Button_Move(6, scene_lab, scene_yard)

lib_goLEFT = Button_Move(4, scene_lib, scene_yard)

forest_goFORWARD = Button_Move(8, scene_forest, scene_space)
forest_goBACK = Button_Move(2, scene_forest, scene_yard)

space_goBACK = Button_Move(2, scene_space, scene_forest)

# item
book_I = Item("./Images/book.png", scene_lib, 590, 260, "물리학 서적")
assignment_I = Item("./Images/light.png", scene_lab, 850, 100, "미리 한 과제")
key_I = Item("./Images/light.png", scene_forest, 800, 100, "의문의 열쇠")

# enemy
dragon = Enemy("./Images/dragon_blue_s.png", "./Images/event_dragon.png", "prof: Dragon", scene_space, 200, 200, 2,
               bgm="./Sounds/UIsounds/Upper01.mp3")
dragon.picks = Object("./Images/pick_dragon.png")
dragon.atsound = Attack_sound("./Sounds/Effect/3hits.mp3", scene_end_bad)
dragon.attxt = "교수님의 거꾸로수업 + 기말과제 + 기말고사\n삼연격!"

english = Enemy("./Images/prof_enga.png", "./Images/event_prof_enga.png", "prof: (영어A)", scene_forest, 800, -100, 1,
                bgm="./Sounds/UIsounds/Rise03.mp3")
english.picks = Object("./Images/pick_enga.png")
english.atsound = Attack_sound("./Sounds/Effect/bookflip.mp3", scene_end_bad)
english.attxt = "영어A 공학수업 연격!"

scientist = Enemy("./Images/scientist.png", "./Images/event_scientist.png", "물리학 광신도", scene_lab, 800, -100, 3,
                  bgm="./Sounds/Effect/scientist.wav")
scientist.picks = Object("./Images/pick_scientist.png")
scientist.atsound = Attack_sound("./Sounds/Effect/physic_beam.mp3", scene_end_bad)
scientist.attxt = "물리학 광신도의 상대성 이론 빔!"

# special
light = Item("./Images/light.png", scene_yard, 0, 0, "의문의 물건")
military = Button_act("./Images/입영통지서.png", scene_yard, scene_end_army, 0, 0, show=0)

grhat = Button_act("./Images/grhat.png", scene_space, scene_end_graduate, 0, 0, show=0)

def item_pick_default(object):
    if object == light:
        military.show()

    if object == book_I:
        Picked.book = 1

    if object == assignment_I:
        Picked.assignment = 1

    if object == endlight:
        grhat.show()


def rocket_onMouseAction(x, y, action):
    if Picked.key == 1:
        Picked.engine = 1
        showMessage("로켓이 작동하기 시작했다!")

    else:
        showMessage("로켓이 미동조차 하지 않는다\n열쇠가 필요하다")


Object.onPickDefault = item_pick_default
rocket.onMouseAction = rocket_onMouseAction

startGame(scene_start)
