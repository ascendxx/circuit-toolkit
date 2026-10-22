"""主页：欢迎 + 统计 + 常用计算快捷入口。"""
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


COMMON = [
    ("欧姆定律", "U=IR"),
    ("串并联电阻", "R1+R2+…"),
    ("感抗/容抗", "X=2πfL / 1/(2πfC)"),
    ("三相功率", "P=√3·U·I·cosφ"),
    ("功率因数补偿", "Qc=P(tanφ1-tanφ2)"),
    ("短路电流", "Ik=c·Un/(√3·Z)"),
    ("接地电阻", "R=ρ/(2πL)·ln(4L/d)"),
    ("电机转速", "n0=60f/p"),
]


class HomePage(QWidget):
    def __init__(self, navigator=None):
        super().__init__()
        self.nav = navigator
        lay = QVBoxLayout(self)
        lay.setContentsMargins(32, 28, 32, 24)
        lay.setSpacing(20)

        title = QLabel("电路计算工具箱")
        title.setObjectName("h1")
        sub = QLabel("离线电气计算 · 无需联网 · 即开即用")
        sub.setObjectName("muted")
        lay.addWidget(title)
        lay.addWidget(sub)

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

        lay.addWidget(self._section_label("常用计算（考试高频）"))
        common = QGridLayout()
        common.setSpacing(10)
        for i, (name, expr) in enumerate(COMMON):
            common.addWidget(self._common_card(name, expr), i // 2, i % 2)
        lay.addLayout(common)

        lay.addWidget(self._section_label("功能模块"))
        nav = QGridLayout()
        nav.setSpacing(10)
        items = [
            ("🔄 转换", "温度 / 电压波形 / 欧姆定律 / 功率因数 / 色环电阻", "convert"),
            ("📚 资源", "色环电阻 / 载流量 / 空开选型 / 接地电阻", "resources"),
            ("🔌 引脚定义", "USB / HDMI / RJ45 / RS232 / VGA / 树莓派", "pinouts"),
            ("📐 公式集", f"{_count_formulas()} 条公式，支持搜索", "formulas"),
            ("⭐ 收藏", "常用公式与计算入口", "favorites"),
        ]
        for i, (name, desc, key) in enumerate(items):
            nav.addWidget(self._nav_card(name, desc, key), i // 3, i % 3)
        lay.addLayout(nav)

        lay.addStretch()

    def _section_label(self, text):
        l = QLabel(text)
        l.setObjectName("h2")
        return l

    def _stat_card(self, num, label):
        f = QFrame()
        f.setObjectName("card")
        f.setMinimumHeight(90)
        v = QVBoxLayout(f)
        v.setContentsMargins(18, 16, 18, 16)
        v.setSpacing(6)
        n = QLabel(num)
        n.setObjectName("statNum")
        l = QLabel(label)
        l.setObjectName("muted")
        v.addWidget(n)
        v.addWidget(l)
        return f

    def _common_card(self, name, expr):
        f = QFrame()
        f.setObjectName("card")
        f.setMinimumHeight(64)
        f.setCursor(Qt.CursorShape.PointingHandCursor)
        v = QVBoxLayout(f)
        v.setContentsMargins(16, 12, 16, 12)
        v.setSpacing(4)
        n = QLabel(name)
        n.setStyleSheet("font-size:14px;font-weight:600;")
        e = QLabel(expr)
        e.setObjectName("muted")
        v.addWidget(n)
        v.addWidget(e)
        f.mousePressEvent = lambda e: self._jump("formulas")
        return f

    def _nav_card(self, name, desc, key):
        f = QFrame()
        f.setObjectName("card")
        f.setMinimumHeight(72)
        f.setCursor(Qt.CursorShape.PointingHandCursor)
        v = QVBoxLayout(f)
        v.setContentsMargins(16, 14, 16, 14)
        v.setSpacing(4)
        n = QLabel(name)
        n.setStyleSheet("font-size:14px;font-weight:600;")
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
