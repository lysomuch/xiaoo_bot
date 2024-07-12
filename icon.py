from PIL import Image

# 打开原始 .ico 文件
img = Image.open('xiaoo.ico')

# 保存为 .icns 文件
img.save('xiaoo.icns')