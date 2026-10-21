"""戴维南等效电路：负载计算。"""
from __future__ import annotations

from PyQt6.QtWidgets import QPushButton

from .base import CalculatorBase, make_number_input


class TheveninWidget(CalculatorBase):
    title = "戴维南等效电路"
    subtitle = "已知开路电压 Voc、等效内阻 Rth，接上负载 RL，求负载电压、电流、功率。"

    def __init__(self) -> None:
        super().__init__()
        self.voc = make_number_input(default=12.0)
        self.rth = make_number_input(default=50.0)
        self.rl = make_number_input(default=100.0)

        self.add_field("开路电压 Voc（V）", self.voc)
        self.add_field("等效内阻 Rth（Ω）", self.rth)
        self.add_field("负载电阻 RL（Ω）", self.rl)

        btn = QPushButton("计算负载")
        btn.clicked.connect(self.calculate)
        self.add_field("", btn)

    def calculate(self) -> None:
        voc, rth, rl = (w.value() for w in (self.voc, self.rth, self.rl))
        if rth <= 0 or rl <= 0:
            self.set_result("⚠️ Rth、RL 必须大于 0。")
            return
        i_l = voc / (rth + rl)
        v_l = i_l * rl
        p_l = v_l * i_l
        p_max = voc * voc / (4 * rth)
        self.set_result(
            f"负载电流 I_L = {self.fmt(i_l, 'A')}\n"
            f"负载电压 V_L = {self.fmt(v_l, 'V')}\n"
            f"负载功率 P_L = {self.fmt(p_l, 'W')}\n"
            f"（理论最大功率传输条件：当 RL = Rth = {self.fmt(rth, 'Ω')} 时，"
            f"P_max = {self.fmt(p_max, 'W')}）"
        )
