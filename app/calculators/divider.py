"""分压 / 分流快速估算。"""
from __future__ import annotations

from PyQt6.QtWidgets import QPushButton

from .base import CalculatorBase, make_number_input


class DividerWidget(CalculatorBase):
    title = "分压与分流"
    subtitle = "分压器：输入 V_in、R1、R2，求输出电压；分流器：输入 I_total、R1、R2，求两支路电流。"

    def __init__(self) -> None:
        super().__init__()
        self.vin = make_number_input(default=5.0)
        self.iin = make_number_input()
        self.r1 = make_number_input(default=1000.0)
        self.r2 = make_number_input(default=1000.0)

        self.add_field("输入电压 V_in（分压用）", self.vin)
        self.add_field("总电流 I_total（分流用，A）", self.iin)
        self.add_field("R1（Ω）", self.r1)
        self.add_field("R2（Ω）", self.r2)

        btn = QPushButton("计算")
        btn.clicked.connect(self.calculate)
        self.add_field("", btn)

    def calculate(self) -> None:
        v_in, i_in, r1, r2 = (
            w.value() for w in (self.vin, self.iin, self.r1, self.r2)
        )
        if r1 <= 0 or r2 <= 0:
            self.set_result("⚠️ R1、R2 必须大于 0。")
            return

        v_out = v_in * r2 / (r1 + r2)
        i1 = i_in * r2 / (r1 + r2)
        i2 = i_in * r1 / (r1 + r2)

        self.set_result(
            f"分压：V_out = V_in × R2/(R1+R2) = {self.fmt(v_out, 'V')}\n"
            f"分流：I₁（过 R1）= {self.fmt(i1, 'A')}     "
            f"I₂（过 R2）= {self.fmt(i2, 'A')}"
        )
