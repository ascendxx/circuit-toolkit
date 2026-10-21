"""资源页：色环电阻、电线颜色、AWG、温度传感器查表。"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget, QTableWidget, QTableWidgetItem,
    QHeaderView, QGroupBox, QFormLayout, QComboBox, QLineEdit, QPushButton, QLabel,
)
from PyQt6.QtCore import Qt
from ..data import RESISTOR_COLOR, WIRING_COLOR, AWG, TEMP_SENSORS, COPPER_RESISTIVITY


class ResourcesPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(24, 24, 24, 24)
        tabs = QTabWidget()
        tabs.addTab(self._resistor_tab(), "色环电阻")
        tabs.addTab(self._wiring_tab(), "电线颜色")
        tabs.addTab(self._awg_tab(), "AWG 线规")
        tabs.addTab(self._sensor_tab(), "温度传感器")
        lay.addWidget(tabs)

    def _table(self, headers, rows):
        t = QTableWidget(len(rows), len(headers))
        t.setHorizontalHeaderLabels(headers)
        t.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        t.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                t.setItem(r, c, QTableWidgetItem(str(val)))
        return t

    def _resistor_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        rows = [(k, v[0], v[1], v[2]) for k, v in RESISTOR_COLOR.items()]
        v.addWidget(self._table(["颜色", "有效数字", "倍率", "误差"], rows))
        return w

    def _wiring_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        rows = [(k, v) for k, v in WIRING_COLOR.items()]
        v.addWidget(self._table(["标识", "颜色"], rows))
        v.addWidget(QLabel("标准：IEC 60446 / GB 7947"))
        return w

    def _awg_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        rows = [(k, f"{v:.4f}") for k, v in AWG.items()]
        v.addWidget(self._table(["AWG", "截面积 mm²"], rows))
        return w

    def _sensor_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        rows = [(k, v) for k, v in TEMP_SENSORS.items()]
        v.addWidget(self._table(["传感器", "特性公式"], rows))
        v.addWidget(QLabel(f"铜电阻率：20℃={COPPER_RESISTIVITY['20℃']} Ω·mm²/m，75℃={COPPER_RESISTIVITY['75℃']}"))
        return w
