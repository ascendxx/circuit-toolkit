"""主页：欢迎 + 统计 + 常用入口。"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QFrame
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
        lay.setContentsMargins(36, 36, 36, 24)
        lay.setSpacing(16)

        title = QLabel("电路计算工具箱")
        title.setStyleSheet("font-size:30px;font-weight:700;color:#1d1d1f;")
        sub = QLabel("Circuit Toolkit · 离线电气计算综合软件")
        sub.setStyleSheet("font-size:14px;color:#6e6e73;")
        lay.addWidget(title)
        lay.addWidget(sub)

        # 统计条
        stats = QGridLayout()
        stats.setSpacing(12)
        cards = [
            (f"{_count_formulas()}", "条计算公式"),
            (f"{len(FORMULAS)}", "个分类"),
            (f"{_count_pins()}", "个引脚定义"),
            (f"{len(PINOUTS)}", "类接口"),
        ]
        for i, (num, label) in enumerate(cards):
            stats.addWidget(self._stat(num, label), 0, i)
        lay.addLayout(stats)

        lay.addSpacing(8)
        grid = QGridLayout()
        grid.setSpacing(12)
        items = [
            ("转换", "温度 / 电压波形 / 欧姆定律 / 功率因数 / 色环电阻", "convert"),
            ("资源", "色环电阻 / 电线颜色 / AWG / 温度传感器", "resources"),
            ("引脚定义", "USB / HDMI / RJ45 / RS232 / VGA / 树莓派", "pinouts"),
            ("公式集", "电路基础 / 电机 / 变压器 / 功率因数 / 短路", "formulas"),
            ("收藏", "常用公式与计算入口", "favorites"),
        ]
        for i, (name, desc, key) in enumerate(items):
            grid.addWidget(self._card(name, desc, key), i // 2, i % 2)
        lay.addLayout(grid)
        lay.addStretch()

    def _stat(self, num, label):
        f = QFrame()
        f.setStyleSheet("background:#f5f5f7;border-radius:10px;padding:14px;")
        v = QVBoxLayout(f)
        n = QLabel(num); n.setStyleSheet("font-size:24px;font-weight:700;color:#0071e3;")
        l = QLabel(label); l.setStyleSheet("font-size:12px;color:#6e6e73;")
        v.addWidget(n); v.addWidget(l)
        return f

    def _card(self, name, desc, key):
        f = QFrame()
        f.setStyleSheet("""
            QFrame { background:#fff;border:1px solid #e5e5ea;border-radius:10px;}
            QFrame:hover { border-color:#0071e3; background:#fafbfd;}
        """)
        v = QVBoxLayout(f)
        v.setContentsMargins(16, 14, 16, 14)
        n = QLabel(name); n.setStyleSheet("font-size:16px;font-weight:600;color:#1d1d1f;")
        d = QLabel(desc); d.setStyleSheet("font-size:12px;color:#6e6e73;")
        v.addWidget(n); v.addWidget(d)
        f.mousePressEvent = lambda e, k=key: self._jump(k)
        return f

    def _jump(self, key):
        if self.nav:
            self.nav(key)
