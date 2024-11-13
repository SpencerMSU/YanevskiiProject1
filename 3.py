from random import *
from typing import Match

click = True
type = True
def button_part():
    construction_name = ["рамные рельсы", "остряки", "сердечник крестовины", "контррельсы", "усовики",
                         "переводной механизм","стрелка с переводным механизмом","соединительные пути",
                         "крестовина с контррельсами"]
    count = 10
    cnt=9
    while cnt>0:
        rand=randint(0,cnt)
        print("Найдите "+construction_name[rand])
        cnt-=1
        construction_name.remove(construction_name[rand])
        if click ==True:
            continue
        elif click == False:
            count-=1
        if type == True:
            print("10/"+count)

    if count>8:
        print("Ваша оценка 5")
    elif count>6:
        print("Ваша оценка 4")
    elif count>4:
        print("Ваша оценка 3")
    elif count>2:
        print("Ваша оценка 2")
    else:
        print("Ваша оценка 0")

def button_type(type):
    return not type
def button_start():
    print("кликните на режим игры: ")
    if click == True:
        button_part()
    if click == True:
        type=button_type(type)