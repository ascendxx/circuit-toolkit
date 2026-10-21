"""计算器通用基类与小部件。"""
from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)


def make_number_input(default: float = 0.0, minimum: float = -1e12,
                      maximum: float = 1e12, decimals: int = 6) -> QDoubleSpinBox:
    """生成一个数值输入框。"""
    box = QDoubleSpinBox()
    box.setRange(minimum, maximum)
    box.setDecimals(decimals)
    box.setValue(default)
    box.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.NoButtons)
    return box


class CalculatorBase(QWidget):
    """所有计算器的基类：提供标题、副标题、结果框和统一布局。"""

    title: str = ""
    subtitle: str = ""

    def __init__(self) -> None:
        super().__init__()
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(14)

        self._title = QLabel(self.title)
        self._title.setObjectName("h1")
        self._subtitle = QLabel(self.subtitle)
        self._subtitle.setObjectName("h2")
        self._subtitle.setWordWrap(True)

        self._form_host = QWidget()
        self._form = QFormLayout(self._form_host)
        self._form.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        self._form.setHorizontalSpacing(16)
        self._form.setVerticalSpacing(10)

        self._result = QLabel("")
        self._result.setObjectName("ResultBox")
        self._result.setWordWrap(True)
        self._result.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        root.addWidget(self._title)
        root.addWidget(self._subtitle)
        root.addWidget(self._form_host)
        root.addStretch(1)
        root.addWidget(self._result)

    def add_field(self, label: str, widget: QWidget) -> None:
        self._form.addRow(QLabel(label), widget)

    def set_result(self, text: str) -> None:
        self._result.setText(text)

    @staticmethod
    def fmt(value: float, unit: str = "", sig: int = 6) -> str:
        """把浮点数格式化成易读字符串，自动选量级。"""
        if value == 0:
            body = "0"
        else:
            abs_v = abs(value)
            if abs_v >= 1e6:
                body = f"{value / 1e6:.{sig}g} M"
            elif abs_v >= 1e3:
                body = f"{value / 1e3:.{sig}g} k"
            elif abs_v >= 1:
                body = f"{value:.{sig}g} "
            elif abs_v >= 1e-3:
                body = f"{value * 1e3:.{sig}g} m"
            elif abs_v >= 1e-6:
                body = f"{value * 1e6:.{sig}g} µ"
            else:
                body = f"{value:.{sig}g} "
        return body + unit
