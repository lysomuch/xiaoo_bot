import locale
from PySide6.QtCore import QUrl, Signal
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
from PySide6.QtGui import QShortcut, QKeySequence, QGuiApplication
from PySide6.QtWidgets import QMessageBox

class Browser(QWebEngineView):
    closed = Signal()

    def __init__(self):
        super().__init__()
        self.setup_browser()

    def setup_browser(self):
        # 设置语言
        system_language = locale.getlocale()[0] or 'zh-CN'
        print(f"系统语言是：{system_language}")

        # 设置配置文件
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpAcceptLanguage(system_language)

        # 创建并设置页面
        page = QWebEnginePage(profile, self)
        self.setPage(page)

        # 设置窗口属性
        self.setWindowTitle("小O给自己一个更聪明的大脑")
        
        # 获取主屏幕
        screen = QGuiApplication.primaryScreen()
        screen_size = screen.availableGeometry().size()
        
        # 设置窗口大小为屏幕大小的80%
        window_width = int(screen_size.width() * 0.8)
        window_height = int(screen_size.height() * 0.8)
        self.resize(window_width, window_height)

        # 添加快捷键
        self.reload_shortcut = QShortcut(QKeySequence("F5"), self)
        self.reload_shortcut.activated.connect(self.reload)

        self.back_shortcut = QShortcut(QKeySequence("Alt+Left"), self)
        self.back_shortcut.activated.connect(self.back)

        self.forward_shortcut = QShortcut(QKeySequence("Alt+Right"), self)
        self.forward_shortcut.activated.connect(self.forward)

        # 连接加载完成和错误信号
        self.loadFinished.connect(self.on_load_finished)

    def open_browser(self, url):
        self.load(QUrl(url))
        self.showMaximized()  # 最大化显示窗口

    def on_load_finished(self, ok):
        if not ok:
            self.handle_load_error()

    def handle_load_error(self):
        error_message = "页面加载失败。请检查您的网络连接或尝试刷新页面。"
        QMessageBox.warning(self, "加载错误", error_message)

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

    # 可以根据需要添加更多自定义方法