"""主页：欢迎 + 常用入口。"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QFrame,
)
from PyQt6.QtCore import Qt


class HomePage(QWidget):
    def __init__(self, navigator=None):
        super().__init__()
        self.nav = navigator
        lay = QVBoxLayout(self)
        lay.setContentsMargins(32, 32, 32, 32)
        lay.setSpacing(20)

        title = QLabel("电路计算工具箱")
        title.setStyleSheet("font-size:28px;font-weight:600;color:#1d1d1f;")
        sub = QLabel("Circuit Toolkit · 电气计算综合软件")
        sub.setStyleSheet("font-size:14px;color:#6e6e73;")
        lay.addWidget(title)
        lay.addWidget(sub)

        grid = QGridLayout()
        grid.setSpacing(12)
        cards = [
            ("转换", "温度 / 电压波形 / 角度 / 转速", "convert"),
            ("资源", "色环电阻 / 电线颜色 / AWG / 传感器", "resources"),
            ("引脚定义", "USB / HDMI / RJ45 / RS232 / VGA 等", "pinouts"),
            ("公式集", "电路基础 / 电机 / 变压器 / 功率因数", "formulas"),
            ("收藏", "常用公式与计算入口", "favorites"),
        ]
        for i, (name, desc, key) in enumerate(cards):
            card = self._card(name, desc, key)
            grid.addWidget(card, i // 2, i % 2)
        lay.addLayout(grid)
        lay.addStretch()

    def _card(self, name, desc, key):
        f = QFrame()
        f.setStyleSheet("""
            QFrame { background:#fff;border:1px solid #e5e5ea;border-radius:10px;}
            QFrame:hover { border-color:#0071e3; }
        """)
        v = QVBoxLayout(f)
        v.setContentsMargins(16, 14, 16, 14)
        n = QLabel(name)
        n.setStyleSheet("font-size:16px;font-weight:600;color:#1d1d1f;")
        d = QLabel(desc)
        d.setStyleSheet("font-size:12px;color:#6e6e73;")
        v.addWidget(n)
        v.addWidget(d)
        f.mousePressEvent = lambda e, k=key: self._jump(k)
        return f

    def _jump(self, key):
        if self.nav:
            self.nav(key)
