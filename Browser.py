import locale
from PySide6.QtCore import QUrl, Signal, Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QProgressBar, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
from PySide6.QtGui import QShortcut, QKeySequence

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
        self.resize(1200, 800)

        # 添加进度条
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setFixedHeight(3)  # 使进度条更细
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: none;
                background-color: transparent;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;  /* 绿色 */
            }
        """)
        self.loadProgress.connect(self.update_progress)

        # 添加动画效果
        self.progress_animation = QPropertyAnimation(self.progress_bar, b"value")
        self.progress_animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.progress_animation.setDuration(300)  # 300毫秒

        # 添加快捷键
        self.reload_shortcut = QShortcut(QKeySequence("F5"), self)
        self.reload_shortcut.activated.connect(self.reload)

        self.back_shortcut = QShortcut(QKeySequence("Alt+Left"), self)
        self.back_shortcut.activated.connect(self.back)

        self.forward_shortcut = QShortcut(QKeySequence("Alt+Right"), self)
        self.forward_shortcut.activated.connect(self.forward)

        # 连接加载完成和错误信号
        self.loadFinished.connect(self.on_load_finished)

    def update_progress(self, progress):
        self.progress_animation.setStartValue(self.progress_bar.value())
        self.progress_animation.setEndValue(progress)
        self.progress_animation.start()

        if progress == 100:
            self.progress_bar.hide()
        else:
            self.progress_bar.show()

    def open_browser(self, url):
        self.load(QUrl(url))
        self.show()
        self.progress_bar.show()

    def on_load_finished(self, ok):
        if not ok:
            self.handle_load_error()

    def handle_load_error(self):
        error_message = "页面加载失败。请检查您的网络连接或尝试刷新页面。"
        QMessageBox.warning(self, "加载错误", error_message)

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.progress_bar.setGeometry(0, 0, self.width(), 3)

    # 可以根据需要添加更多自定义方法