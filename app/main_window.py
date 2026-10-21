"""主窗口：侧栏导航 + 内容区。"""
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
    ("🏠", "主页", "home"),
    ("🔄", "转换", "convert"),
    ("📚", "资源", "resources"),
    ("🔌", "引脚定义", "pinouts"),
    ("📐", "公式集", "formulas"),
    ("⭐", "收藏", "favorites"),
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("电路计算工具箱 · Circuit Toolkit")
        self.resize(1280, 800)
        self.setMinimumSize(960, 640)

        root = QWidget()
        root.setObjectName("central")
        h = QHBoxLayout(root)
        h.setContentsMargins(0, 0, 0, 0)
        h.setSpacing(0)

        # 侧栏
        side = QFrame()
        side.setObjectName("sidebar")
        side.setFixedWidth(200)
        sv = QVBoxLayout(side)
        sv.setContentsMargins(12, 20, 12, 16)
        sv.setSpacing(2)

        logo = QLabel("⚡ Circuit Toolkit")
        logo.setObjectName("logo")
        sub = QLabel("电气计算综合软件")
        sub.setObjectName("subtitle")
        sv.addWidget(logo)
        sv.addWidget(sub)
        sv.addSpacing(8)

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

        for icon, label, key in NAV:
            b = QPushButton(f"  {icon}  {label}")
            b.setObjectName("navBtn")
            b.setCheckable(True)
            b.setCursor(Qt.CursorShape.PointingHandCursor)
            b.clicked.connect(lambda _, k=key: self._nav(k))
            self.buttons[key] = b
            sv.addWidget(b)
        sv.addStretch()
        ver = QLabel("v1.0 · 离线版")
        ver.setObjectName("subtitle")
        ver.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sv.addWidget(ver)

        h.addWidget(side)
        h.addWidget(self.stack, 1)
        self.setCentralWidget(root)
        self._nav("home")

    def _nav(self, key):
        idx = [k for _, _, k in NAV].index(key)
        self.stack.setCurrentIndex(idx)
        for k, b in self.buttons.items():
            b.setChecked(k == key)
