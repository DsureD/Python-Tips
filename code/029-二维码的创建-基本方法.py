# 需要安装 pip install qrcode
import qrcode

str1 = "123字符串什么都可以"
img = qrcode.make(str1, box_size=10)  # box_size控制二维码的大小，每个点（方块）中的像素个数
img.save("qr-img.png")  # 文件的保存路径
# img.show()  # 也可以打开图片，临时文件


'''
version: 一个整数，范围为1到40，表示二维码的大小（最小值是1，是个12×12的矩阵），如果想让程序自动生成，将值设置为 None 并使用 fit=True 参数即可。
error_correction: 二维码的纠错范围，可以选择4个常量：
ERROR_CORRECT_L 7%以下的错误会被纠正
ERROR_CORRECT_M (default) 15%以下的错误会被纠正
ERROR_CORRECT_Q 25 %以下的错误会被纠正
ERROR_CORRECT_H. 30%以下的错误会被纠正
box_size: 每个点（方块）中的像素个数
border: 二维码距图像外围边框距离，默认为4，而且相关规定最小为4

'''
