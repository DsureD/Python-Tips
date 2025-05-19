month = "5"
day = "19"

# .zfill(宽度数值)，如果字符串不足宽度数值，则会在前面补0
print(f"日期是：{month.zfill(5)}月{day.zfill(2)}日")  # 日期是：00005月19日
mon = 5
day_ = 6
print(f"您输入的是：{mon:02}月{day_:02}日")  # 数字需要这样 # 您输入的是：05月19日
