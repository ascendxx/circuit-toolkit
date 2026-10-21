"""主窗口：左侧导航 + 右侧堆叠页面。"""
from __future__ import annotations

from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from .calculators.cable import CableAmpacityWidget
from .calculators.divider import DividerWidget
from .calculators.ohm_law import OhmLawWidget
from .calculators.resistor import ResistorWidget
from .calculators.thevenin import TheveninWidget
from .calculators.three_phase import ThreePhaseWidget
from .calculators.units import UnitsWidget


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("电路通 · Circuit Toolkit")

        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # 侧边栏
        sidebar = QWidget()
        sidebar.setObjectName("Sidebar")
        side_layout = QVBoxLayout(sidebar)
        side_layout.setContentsMargins(0, 0, 0, 12)
        side_layout.setSpacing(0)

        title = QLabel("电路通")
        title.setObjectName("SidebarTitle")
        sub = QLabel("Circuit Toolkit · 离线计算")
        sub.setObjectName("SidebarSubtitle")

        self.nav = QListWidget()
        self.pages = QStackedWidget()

        modules = [
            ("⚡  欧姆定律与功率", OhmLawWidget),
            ("🔌  电阻串并联", ResistorWidget),
            ("🎚️  分压与分流", DividerWidget),
            ("🔄  戴维南等效", TheveninWidget),
            ("🔺  三相电路", ThreePhaseWidget),
            ("📏  单位换算", UnitsWidget),
            ("🧵  电缆载流量", CableAmpacityWidget),
        ]
        for label, cls in modules:
            item = QListWidgetItem(label)
            self.nav.addItem(item)
            self.pages.addWidget(cls())

        self.nav.currentRowChanged.connect(self.pages.setCurrentIndex)
        self.nav.setCurrentRow(0)

        side_layout.addWidget(title)
        side_layout.addWidget(sub)
        side_layout.addWidget(self.nav, stretch=1)

        # 内容卡片
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(20, 20, 20, 20)
        card = QWidget()
        card.setObjectName("ContentCard")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(0, 0, 0, 0)
        card_layout.addWidget(self.pages)
        content_layout.addWidget(card)

        root.addWidget(sidebar)
        root.addWidget(content, stretch=1)
