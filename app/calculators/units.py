"""常用电工单位换算。"""
from __future__ import annotations

from PyQt6.QtWidgets import QComboBox, QPushButton

from .base import CalculatorBase, make_number_input

# 各物理量 → 单位列表（换算到 SI 基本单位的倍率）
UNITS: dict[str, dict[str, float]] = {
    "电压": {"V": 1.0, "mV": 1e-3, "kV": 1e3, "µV": 1e-6},
    "电流": {"A": 1.0, "mA": 1e-3, "kA": 1e3, "µA": 1e-6},
    "电阻": {"Ω": 1.0, "kΩ": 1e3, "MΩ": 1e6, "mΩ": 1e-3},
    "功率": {"W": 1.0, "kW": 1e3, "MW": 1e6, "mW": 1e-3},
    "电容": {"F": 1.0, "mF": 1e-3, "µF": 1e-6, "nF": 1e-9, "pF": 1e-12},
    "电感": {"H": 1.0, "mH": 1e-3, "µH": 1e-6},
    "频率": {"Hz": 1.0, "kHz": 1e3, "MHz": 1e6},
}


class UnitsWidget(CalculatorBase):
    title = "电工单位换算"
    subtitle = "选择物理量、输入数值和原单位，自动换算到其他常用单位。"

    def __init__(self) -> None:
        super().__init__()
        self.quantity = QComboBox()
        self.quantity.addItems(list(UNITS.keys()))
        self.value = make_number_input(default=1.0)
        self.from_unit = QComboBox()

        self.quantity.currentTextChanged.connect(self._refresh_units)
        self._refresh_units(self.quantity.currentText())

        self.add_field("物理量", self.quantity)
        self.add_field("数值", self.value)
        self.add_field("原单位", self.from_unit)

        btn = QPushButton("换算")
        btn.clicked.connect(self.calculate)
        self.add_field("", btn)

    def _refresh_units(self, name: str) -> None:
        self.from_unit.blockSignals(True)
        self.from_unit.clear()
        self.from_unit.addItems(list(UNITS.get(name, {}).keys()))
        self.from_unit.blockSignals(False)

    def calculate(self) -> None:
        q = self.quantity.currentText()
        units = UNITS[q]
        raw = self.value.value()
        src = self.from_unit.currentText()
        si = raw * units[src]

        lines = [f"{raw:g} {src} ="]
        for name, factor in units.items():
            if name == src:
                continue
            lines.append(f"    {si / factor:g} {name}")
        self.set_result("\n".join(lines))
