"""资源页：色环电阻、电线颜色、AWG、温度传感器查表。"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget, QTableWidget, QTableWidgetItem,
    QHeaderView, QLabel,
)
from ..data import (
    RESISTOR_COLOR, WIRING_COLOR, AWG, TEMP_SENSORS, COPPER_RESISTIVITY,
    WIRE_AMPACITY, MCB_SELECTION, GROUNDING_REQ,
)


class ResourcesPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 20, 20, 20)
        title = QLabel("资源参考")
        title.setObjectName("h2")
        lay.addWidget(title)
        tabs = QTabWidget()
        tabs.addTab(self._resistor_tab(), "色环电阻")
        tabs.addTab(self._wiring_tab(), "电线颜色")
        tabs.addTab(self._awg_tab(), "AWG 线规")
        tabs.addTab(self._wire_tab(), "导线载流量")
        tabs.addTab(self._mcb_tab(), "空开选型")
        tabs.addTab(self._ground_tab(), "接地电阻")
        tabs.addTab(self._sensor_tab(), "温度传感器")
        lay.addWidget(tabs)

    def _table(self, headers, rows):
        t = QTableWidget(len(rows), len(headers))
        t.setHorizontalHeaderLabels(headers)
        t.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        t.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        t.verticalHeader().setVisible(False)
        t.setAlternatingRowColors(True)
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
        rows = [(k, val) for k, val in WIRING_COLOR.items()]
        v.addWidget(self._table(["标识", "颜色"], rows))
        l = QLabel("标准：IEC 60446 / GB 7947")
        l.setObjectName("muted")
        v.addWidget(l)
        return w

    def _awg_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        rows = [(k, f"{val:.4f}") for k, val in AWG.items()]
        v.addWidget(self._table(["AWG", "截面积 mm²"], rows))
        return w

    def _sensor_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        rows = [(k, val) for k, val in TEMP_SENSORS.items()]
        v.addWidget(self._table(["传感器", "特性公式"], rows))
        l = QLabel(f"铜电阻率：20℃={COPPER_RESISTIVITY['20℃']} Ω·mm²/m，75℃={COPPER_RESISTIVITY['75℃']}")
        l.setObjectName("muted")
        v.addWidget(l)
        return w

    def _wire_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        v.addWidget(self._table(
            ["截面积 mm²", "明敷(A)", "二股穿管(A)", "三股以上穿管(A)"],
            WIRE_AMPACITY,
        ))
        l = QLabel("铜芯塑料绝缘线(BV)，环境温度 25℃，空气敷设；穿管敷设应乘以校正系数。")
        l.setObjectName("muted")
        v.addWidget(l)
        return w

    def _mcb_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        v.addWidget(self._table(
            ["额定电流(A)", "可带功率 220V(kW)", "适用负载"],
            MCB_SELECTION,
        ))
        l = QLabel("空开额定电流 ≈ 导线安全载流量的 80%；感性负载按 1.25 倍选。")
        l.setObjectName("muted")
        v.addWidget(l)
        return w

    def _ground_tab(self):
        w = QWidget(); v = QVBoxLayout(w)
        rows = [(k, val) for k, val in GROUNDING_REQ.items()]
        v.addWidget(self._table(["接地类型", "电阻要求"], rows))
        return w
