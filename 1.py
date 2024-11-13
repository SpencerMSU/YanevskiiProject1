from random import *
from typing import Match
click=True
type = True
def button_start(click1, click2, click3, count, count_of_construction, count_of_sostav, count_of_weigh):
    if click1 == -1 or click2 == -1 or click3 == -1:
        print("Нехватает элементов для кейса")
    elif click1 == 0 and click2 == 0 and click3 == 0:
        count_of_construction.remove(count_of_construction[click1])
        count_of_sostav.remove(count_of_sostav[click2])
        count_of_weigh.remove(count_of_weigh[click3])
    else:
        count -= 1
    return (count,count_of_construction,count_of_sostav,count_of_weigh)
def button_part():
    count_of_construction = [1, 2, 1]
    count_of_sostav = [1, 1, 1]
    count_of_weigh = [1, 1, 1]
    construction_name = ["1 модель","и тд"]
    sostav_name=["1 картина состава","и тд"]
    weigh_name=["мясо","и тд"]

    count = 10
    cnt=len(construction_name)+len(sostav_name)+len(weigh_name)
    while cnt>0:
        rand=randint(0,cnt)
        click1 = -1
        click2 = -1
        click3 = -1

        count,count_of_construction,count_of_sostav,count_of_weigh=button_start(click1, click2, click3, count, count_of_construction, count_of_sostav, count_of_weigh)
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

