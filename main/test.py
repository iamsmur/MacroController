import pyautogui

from testf import *


#pyautogui.displayMousePosition()
#x, y = pyautogui.position()
#print(x,y)

def actionPerform(choose,param):
    x, y = int(param[0]), int(param[1]) # float(param[2])
    if choose == "moveTo":
        moveToPost(x,y)
    elif choose == "Button.left":
        clickBtn(x,y)
    elif choose == "doubleClick":
        doubleClickbtn(x,y)
    elif choose == "Button.right":
        rightClickbtn(x,y)
    else:
        print("Enter Correct Details again")
    return True


def moveToPost(x,y,duration=1):
    pyautogui.moveTo(x,y,duration=0.25)
    #print(f"moveToPost({x},{y})")

def clickBtn(x=None, y=None, clicks=1, interval=0.0,duration=0.0, pause=None, _pause=True):
    pyautogui.moveTo(x,y,duration=0.002)
    pyautogui.click(x,y,duration=1)
    #print(f"clickBtn({x},{y})")
def doubleClickbtn(x=None, y=None, clicks=1, interval=0.0,duration=0.0, pause=None, _pause=True):
    pyautogui.moveTo(x,y,duration=0.002)
    pyautogui.doubleClick(x,y)
    #print(f"doubleClickbtn({x},{y})")
def rightClickbtn(x=None, y=None, clicks=1, interval=0.0,duration=0.0, pause=None, _pause=True):
    pyautogui.moveTo(x,y,duration=0.002)
    pyautogui.rightClick(x,y,duration=1)
    #print(f"rightClickbtn({x},{y})")

if __name__ == "__main__":
    #choose = input("Enter Action: ")
    #param = [str(i) for i in input("Enter position and duration: ").split(" ")]

    print("Your wish",choose,param)

    result = actionPerform(choose,param)
    #pyautogui.displayMousePosition()
    print(result)
    print("WorkDone")