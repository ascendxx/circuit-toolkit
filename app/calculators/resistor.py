"""电阻串并联等效计算。"""
from __future__ import annotations

from PyQt6.QtWidgets import QComboBox, QLineEdit, QPushButton

from .base import CalculatorBase


class ResistorWidget(CalculatorBase):
    title = "电阻串并联"
    subtitle = "输入一串电阻值（用逗号分隔，单位 Ω），选择串联或并联，得到等效电阻。"

    def __init__(self) -> None:
        super().__init__()
        self.values = QLineEdit()
        self.values.setPlaceholderText("例如：100, 220, 470, 1k")
        self.mode = QComboBox()
        self.mode.addItems(["串联", "并联"])

        self.add_field("电阻列表", self.values)
        self.add_field("连接方式", self.mode)

        btn = QPushButton("计算等效电阻")
        btn.clicked.connect(self.calculate)
        self.add_field("", btn)

    @staticmethod
    def _parse(text: str) -> list[float]:
        out: list[float] = []
        for chunk in text.replace("，", ",").split(","):
            chunk = chunk.strip().lower().replace(" ", "")
            if not chunk:
                continue
            mult = 1.0
            if chunk.endswith("k"):
                mult, chunk = 1e3, chunk[:-1]
            elif chunk.endswith("m"):
                mult, chunk = 1e-3, chunk[:-1]
            elif chunk.endswith("meg") or chunk.endswith("mΩ"):
                mult, chunk = 1e6, chunk[:-3]
            out.append(float(chunk) * mult)
        return out

    def calculate(self) -> None:
        try:
            resistors = self._parse(self.values.text())
        except ValueError:
            self.set_result("⚠️ 输入格式有误，请用逗号分隔数字，如 100, 220, 1k。")
            return
        if not resistors:
            self.set_result("⚠️ 请至少输入一个电阻。")
            return

        if self.mode.currentText() == "串联":
            eq = sum(resistors)
            breakdown = " + ".join(f"{r:g}Ω" for r in resistors)
        else:
            eq = 1.0 / sum(1.0 / r for r in resistors)
            breakdown = " ∥ ".join(f"{r:g}Ω" for r in resistors)

        self.set_result(
            f"共 {len(resistors)} 个电阻：{breakdown}\n"
            f"等效电阻 R_eq = {self.fmt(eq, 'Ω')}"
        )
