"""主页：欢迎 + 统计卡片 + 快捷入口。"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QFrame,
    QSizePolicy,
)
from PyQt6.QtCore import Qt
from ..data import FORMULAS, PINOUTS


def _count_formulas():
    return sum(len(v) for v in FORMULAS.values())


def _count_pins():
    n = 0
    for devs in PINOUTS.values():
        for pins in devs.values():
            n += len(pins)
    return n


class HomePage(QWidget):
    def __init__(self, navigator=None):
        super().__init__()
        self.nav = navigator
        lay = QVBoxLayout(self)
        lay.setContentsMargins(32, 28, 32, 24)
        lay.setSpacing(18)

        title = QLabel("电路计算工具箱")
        title.setObjectName("h1")
        sub = QLabel("离线电气计算 · 无需联网 · 即开即用")
        sub.setObjectName("muted")
        lay.addWidget(title)
        lay.addWidget(sub)

        # 统计卡片
        stats = QGridLayout()
        stats.setSpacing(12)
        cards = [
            (str(_count_formulas()), "条计算公式"),
            (str(len(FORMULAS)), "个分类"),
            (str(_count_pins()), "个引脚定义"),
            (str(len(PINOUTS)), "类接口"),
        ]
        for i, (num, label) in enumerate(cards):
            stats.addWidget(self._stat_card(num, label), 0, i)
        lay.addLayout(stats)

        # 快捷入口
        lay.addWidget(self._section_label("快速入口"))
        grid = QGridLayout()
        grid.setSpacing(12)
        items = [
            ("🔄 转换", "温度 / 电压波形 / 欧姆定律 / 功率因数 / 色环电阻", "convert"),
            ("📚 资源", "色环电阻 / 电线颜色 / AWG / 温度传感器", "resources"),
            ("🔌 引脚定义", "USB / HDMI / RJ45 / RS232 / VGA / 树莓派", "pinouts"),
            ("📐 公式集", "电路基础 / 电机 / 变压器 / 功率因数 / 短路", "formulas"),
            ("⭐ 收藏", "常用公式与计算入口", "favorites"),
        ]
        for i, (name, desc, key) in enumerate(items):
            grid.addWidget(self._entry_card(name, desc, key), i // 2, i % 2)
        lay.addLayout(grid)
        lay.addStretch()

    def _section_label(self, text):
        l = QLabel(text)
        l.setObjectName("h2")
        return l

    def _stat_card(self, num, label):
        f = QFrame()
        f.setObjectName("card")
        f.setMinimumHeight(80)
        v = QVBoxLayout(f)
        v.setContentsMargins(16, 14, 16, 14)
        n = QLabel(num)
        n.setStyleSheet("font-size:26px;font-weight:700;color:#0071e3;")
        l = QLabel(label)
        l.setObjectName("muted")
        v.addWidget(n)
        v.addWidget(l)
        return f

    def _entry_card(self, name, desc, key):
        f = QFrame()
        f.setObjectName("card")
        f.setMinimumHeight(72)
        f.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        f.setCursor(Qt.CursorShape.PointingHandCursor)
        v = QVBoxLayout(f)
        v.setContentsMargins(16, 14, 16, 14)
        n = QLabel(name)
        n.setStyleSheet("font-size:15px;font-weight:600;")
        d = QLabel(desc)
        d.setObjectName("muted")
        d.setWordWrap(True)
        v.addWidget(n)
        v.addWidget(d)
        f.mousePressEvent = lambda e, k=key: self._jump(k)
        return f

    def _jump(self, key):
        if self.nav:
            self.nav(key)
