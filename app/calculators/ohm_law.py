"""欧姆定律与功率计算。"""
from __future__ import annotations

from PyQt6.QtWidgets import QPushButton

from .base import CalculatorBase, make_number_input


class OhmLawWidget(CalculatorBase):
    title = "欧姆定律与功率"
    subtitle = "输入任意两个已知量（单位：V、A、Ω、W），自动算出另外两个。"

    def __init__(self) -> None:
        super().__init__()
        self.v = make_number_input()
        self.i = make_number_input()
        self.r = make_number_input()
        self.p = make_number_input()

        self.add_field("电压 V（伏特）", self.v)
        self.add_field("电流 I（安培）", self.i)
        self.add_field("电阻 R（欧姆）", self.r)
        self.add_field("功率 P（瓦特）", self.p)

        btn = QPushButton("计算")
        btn.clicked.connect(self.calculate)
        self.add_field("", btn)

    def calculate(self) -> None:
        v, i, r, p = (w.value() for w in (self.v, self.i, self.r, self.p))
        filled = [x for x in (v, i, r, p) if x not in (0.0,)]
        if len(filled) < 2:
            self.set_result("⚠️ 请至少填入两个非零已知量。")
            return

        # 用前两个非零量推算，简单可靠
        try:
            if v and i:
                r, p = v / i, v * i
            elif v and r:
                i, p = v / r, v * i
            elif v and p:
                i, r = p / v, v * v / p
            elif i and r:
                v, p = i * r, i * i * r
            elif i and p:
                v, r = p / i, p / i / i
            elif r and p:
                i = (p / r) ** 0.5
                v = i * r
            else:
                self.set_result("⚠️ 无法求解，请检查输入。")
                return
        except ZeroDivisionError:
            self.set_result("⚠️ 出现除零，请检查输入。")
            return

        self.set_result(
            f"结果：  V = {self.fmt(v, 'V')}   "
            f"I = {self.fmt(i, 'A')}   "
            f"R = {self.fmt(r, 'Ω')}   "
            f"P = {self.fmt(p, 'W')}"
        )
