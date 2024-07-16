from pynput import mouse
import pyperclip
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QMenu
from PyQt6.QtCore import Qt

# 初始化全局变量，用于存储鼠标按下和释放的位置
start_position = None
end_position = None

def on_click(x, y, button, pressed):
    global start_position, end_position
    if pressed:
        # 鼠标按下时记录起始位置
        start_position = (x, y)
    else:
        # # 鼠标释放时记录结束位置
        # end_position = (x, y)
        # # 模拟按下Ctrl+C复制选中的内容
        # copy_selected_text()
        showContextMenu()

def showContextMenu(self, event):
        # 更新 end_position 为鼠标释放的位置
        end_position = event.pos()
        # 创建上下文菜单
        contextMenu = QMenu(self)
        # 添加一些动作到菜单
        contextMenu.addAction('复制', lambda: self.textEdit.copy())
        contextMenu.addAction('粘贴', lambda: self.textEdit.paste())
        # 在鼠标当前位置显示菜单
        contextMenu.exec(event.globalPos())
def copy_selected_text():
    # 等待一会儿确保复制操作完成
    time.sleep(0.5)
    # 获取剪贴板中的内容
    selected_text = pyperclip.paste()
    print(f"选中的文本内容: {selected_text}")

# 创建鼠标监听器
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
