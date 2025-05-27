import time
from winsound import Beep
from winsound import MessageBeep
from winsound import PlaySound
# import winsound


# Beep(1500, 1000)  # Beep(频率，持续时间(毫秒)1000=1秒)
# time.sleep(1)
# MessageBeep(10)  # 系统自带,10自带不可操作音，20叮咚

for j in range(2):
    for i in [800, 1600]:
        Beep(i, 100)  # 长短音调


# PlaySound('test.wav', 10)  # 好像只可播放wav音频，10是音量
