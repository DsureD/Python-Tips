import time

import pyautogui

def get_mouse_position():
    for i in range(100):
        x, y = pyautogui.position()
        # pix = pyautogui.screenshot().getpixel((x, y))  # 获取坐标位置的RGB色值
        R,G,B = pyautogui.screenshot().getpixel((x, y))  # 获取坐标位置的RGB色值
        print(f"\r{x,y},R:{R},G:{G},B:{B}",end='')

        time.sleep(0.1)
# get_mouse_position()
# exit()
# pyautogui.click(100, 200)  # 鼠标点击坐标（x=100像素，y=200）
# pyautogui.moveTo(30, 22)  # 鼠标移动到坐标（x，y）
# pyautogui.click()  # 当前位置点击
# pyautogui.hotkey('ctrl', 'v') # 组合按键（Ctrl+V），粘贴功能，按下并松开'ctrl'和'v'按键

pyautogui.moveRel(100, 0, duration=0.25)  # 鼠标从当前位置x右移100像素，y坐标0像素，持续时间0.25秒。xy可以是正负数决定向左或向右


# pyautogui.alert(text='', title='', button='OK')
b = pyautogui.alert(text='要开始程序么？', title='请求框', button='OK')
print(b)  # 输出结果为OK

# 显示一个简单的带文字、OK和Cancel按钮的消息弹窗，用户点击后返回被点击button的文字，支持自定义数字、文字的列表。
# pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])  # OK和Cancel按钮的消息弹窗
# pyautogui.confirm(text='', title='', buttons=range(10))  # 10个按键0-9的消息弹窗
a = pyautogui.confirm(text='', title='', buttons=range(10))
print(a)  # 输出结果为你选的数字

c = pyautogui.confirm(text="",title="",buttons=["ok","cancel"])  # 选择，点击后返回按钮的文字
print(c)

# 可以输入的消息弹窗，带OK和Cancel按钮。用户点击OK按钮返回输入的文字，点击Cancel按钮返回None。
d = pyautogui.prompt(text='文本输入框', title='文本输入框标题', default='123')
print(d)
# 样式同prompt()，用于输入密码，消息用*表示。带OK和Cancel按钮。用户点击OK按钮返回输入的文字，点击Cancel按钮返回None。
e = pyautogui.password(text='密码', title='密码标题', default='123456', mask='*')
print(e)
time.sleep(10)
pyautogui.typewrite('Hello world!')  # 输入Hello world!字符串
pyautogui.typewrite('Hello world!', interval=0.25)  # 每次输入间隔0.25秒，输入Hello world!

pyautogui.press('enter')  # 按下并松开（轻敲）回车键
# pyautogui.press(['left', 'left', 'left', 'left'])  # 按下并松开（轻敲）四下左方向键
# pyautogui.keyDown('shift')  # 按下`shift`键
# pyautogui.keyUp('shift')  # 松开`shift`键
#
# pyautogui.keyDown('shift')
# pyautogui.press('4')
# pyautogui.keyUp('shift')  # 输出 $ 符号的按键


# 按住鼠标左键，把鼠标拖拽到(100, 200)位置
pyautogui.dragTo(100, 200, button='left')
# 按住鼠标左键，用2秒钟把鼠标拖拽到(300, 400)位置
pyautogui.dragTo(300, 400, 2, button='left')
# 按住鼠标左键，用0.2秒钟把鼠标向上拖拽
pyautogui.dragRel(0, -60, duration=0.2)

# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# 其中，button属性可以设置成left，middle和right。
pyautogui.click(10, 20, 2, 0.25, button='left')
pyautogui.click(x=100, y=200, duration=2)  # 先移动到(100, 200)再单击
pyautogui.click()  # 鼠标当前位置点击一下
pyautogui.doubleClick()  # 鼠标当前位置左击两下
pyautogui.doubleClick(x=100, y=150, button="left")  # 鼠标在（100，150）位置左击两下，右击“right”
pyautogui.tripleClick()  # 鼠标当前位置左击三下

pyautogui.mouseDown()  # 鼠标左键按下再松开
pyautogui.mouseUp()
pyautogui.mouseDown(button='right')  # 按下鼠标右键
pyautogui.mouseUp(button='right', x=100, y=200)  # 移动到(100, 200)位置，然后松开鼠标右键

# scroll函数控制鼠标滚轮的滚动，amount_to_scroll参数表示滚动的格数。正数则页面向上滚动，负数则向下滚动
# pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
pyautogui.scroll(5, 20, 2)
pyautogui.scroll(10)  # 向上滚动10格
pyautogui.scroll(-10)  # 向下滚动10格
pyautogui.scroll(10, x=100, y=100)  # 移动到(100, 100)位置再向上滚动10格
