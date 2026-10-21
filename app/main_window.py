"""主窗口：左侧导航 + 右侧内容区。"""
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton,
    QStackedWidget, QLabel, QFrame,
)
from PyQt6.QtCore import Qt
from .widgets.home import HomePage
from .widgets.convert import ConvertPage
from .widgets.resources import ResourcesPage
from .widgets.pinouts import PinoutsPage
from .widgets.formulas import FormulasPage
from .widgets.favorites import FavoritesPage


NAV = [
    ("主页", "home"),
    ("转换", "convert"),
    ("资源", "resources"),
    ("引脚定义", "pinouts"),
    ("公式集", "formulas"),
    ("收藏", "favorites"),
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("电路计算工具箱 Circuit Toolkit")
        self.resize(1200, 780)

        root = QWidget()
        h = QHBoxLayout(root)
        h.setContentsMargins(0, 0, 0, 0)
        h.setSpacing(0)

        # 侧栏
        side = QFrame()
        side.setFixedWidth(180)
        side.setStyleSheet("background:#f5f5f7;border-right:1px solid #e5e5ea;")
        sv = QVBoxLayout(side)
        sv.setContentsMargins(12, 20, 12, 12)
        sv.setSpacing(4)

        logo = QLabel("⚡ Circuit Toolkit")
        logo.setStyleSheet("font-size:15px;font-weight:600;color:#1d1d1f;padding:8px;")
        sv.addWidget(logo)
        sv.addSpacing(12)

        self.buttons = {}
        self.stack = QStackedWidget()
        pages = {
            "home": HomePage(self._nav),
            "convert": ConvertPage(),
            "resources": ResourcesPage(),
            "pinouts": PinoutsPage(),
            "formulas": FormulasPage(),
            "favorites": FavoritesPage(),
        }
        for key, page in pages.items():
            self.stack.addWidget(page)

        for label, key in NAV:
            b = QPushButton(label)
            b.setCheckable(True)
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.setStyleSheet("""
                QPushButton { text-align:left;padding:8px 12px;border:none;border-radius:8px;
                             background:transparent;color:#1d1d1f;font-size:13px;}
                QPushButton:hover { background:#e8e8ed; }
                QPushButton:checked { background:#fff;color:#0071e3;font-weight:600; }
            """)
            b.clicked.connect(lambda _, k=key: self._nav(k))
            self.buttons[key] = b
            sv.addWidget(b)
        sv.addStretch()

        h.addWidget(side)
        h.addWidget(self.stack, 1)
        self.setCentralWidget(root)
        self._nav("home")

    def _nav(self, key):
        idx = [k for _, k in NAV].index(key)
        self.stack.setCurrentIndex(idx)
        for k, b in self.buttons.items():
            b.setChecked(k == key)
