"""三相电路：P/Q/S、线/相换算。"""
from __future__ import annotations

import math

from PyQt6.QtWidgets import QComboBox, QPushButton

from .base import CalculatorBase, make_number_input


class ThreePhaseWidget(CalculatorBase):
    title = "三相电路计算"
    subtitle = (
        "已知线电压、有功功率和功率因数，求线电流、视在功率、无功功率；"
        "或已知线电压和线电流反推 P/S/Q。支持星形 / 三角形接法。"
    )

    def __init__(self) -> None:
        super().__init__()
        self.vl = make_number_input(default=380.0)
        self.p = make_number_input()
        self.cos_phi = make_number_input(default=0.85, minimum=0.01, maximum=1.0)
        self.il = make_number_input()
        self.wiring = QComboBox()
        self.wiring.addItems(["星形 Y", "三角形 Δ"])

        self.add_field("线电压 V_L（V）", self.vl)
        self.add_field("有功功率 P（W，留空则由 V_L 和 I_L 反推）", self.p)
        self.add_field("功率因数 cos φ（0~1）", self.cos_phi)
        self.add_field("线电流 I_L（A，留空则由 P 反推）", self.il)
        self.add_field("接法", self.wiring)

        btn = QPushButton("计算")
        btn.clicked.connect(self.calculate)
        self.add_field("", btn)

    def calculate(self) -> None:
        vl = self.vl.value()
        p = self.p.value()
        cosphi = self.cos_phi.value()
        il = self.il.value()

        if vl <= 0:
            self.set_result("⚠️ 线电压必须大于 0。")
            return

        # √3 关系：P = √3 · V_L · I_L · cosφ（对称三相）
        if p > 0 and il == 0:
            il = p / (math.sqrt(3) * vl * cosphi)
        elif il > 0 and p == 0:
            p = math.sqrt(3) * vl * il * cosphi
        else:
            self.set_result("⚠️ 请在 P 和 I_L 中二选一填入。")
            return

        s = math.sqrt(3) * vl * il
        q = s * math.sin(math.acos(cosphi))
        vp = vl / math.sqrt(3) if self.wiring.currentText() == "星形 Y" else vl
        ip = il if self.wiring.currentText() == "星形 Y" else il / math.sqrt(3)

        self.set_result(
            f"线电流 I_L = {self.fmt(il, 'A')}\n"
            f"视在功率 S = {self.fmt(s, 'VA')}\n"
            f"有功功率 P = {self.fmt(p, 'W')}\n"
            f"无功功率 Q = {self.fmt(q, 'var')}\n"
            f"相电压 V_p = {self.fmt(vp, 'V')}    "
            f"相电流 I_p = {self.fmt(ip, 'A')}（{self.wiring.currentText()}）"
        )
