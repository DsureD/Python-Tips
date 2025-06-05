class Color:
    """控制台颜色"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PINK = '\033[95m'
    CYAN = '\033[96m'
    NO = '\033[0m'


print(f"{Color.RED}RED 红色字符")
print(f"{Color.GREEN}GREEN 绿色字符")
print(f"{Color.YELLOW}YELLOW 黄色字符")
print(f"{Color.BLUE}BLUE 蓝色字符")
print(f"{Color.PINK}PINK 粉色字符")
print(f"{Color.CYAN}CYAN 青色字符")
print(f"{Color.NO}默认颜色字符")
