"""转换页：单位换算（温度、电压波形、角度、转速）。"""
import math
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit,
    QPushButton, QFormLayout, QGroupBox,
)


class ConvertPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(24, 24, 24, 24)
        lay.setSpacing(16)

        lay.addWidget(QLabel("<b>单位换算</b>"))

        # 温度
        g_temp = QGroupBox("温度换算")
        ft = QFormLayout(g_temp)
        self.t_in = QLineEdit("25")
        self.t_from = QComboBox(); self.t_from.addItems(["℃ 摄氏", "℉ 华氏", "K 开尔文"])
        self.t_to = QComboBox(); self.t_to.addItems(["℃ 摄氏", "℉ 华氏", "K 开尔文"])
        ft.addRow("输入", self.t_in)
        ft.addRow("从", self.t_from)
        ft.addRow("到", self.t_to)
        btn_t = QPushButton("转换"); btn_t.clicked.connect(self._conv_temp)
        ft.addRow("", btn_t)
        self.t_out = QLabel("—"); self.t_out.setStyleSheet("font-size:16px;color:#0071e3;font-weight:600;")
        ft.addRow("结果", self.t_out)
        lay.addWidget(g_temp)

        # 电压波形
        g_v = QGroupBox("电压波形（峰值 / 峰峰值 / 有效值）")
        fv = QFormLayout(g_v)
        self.v_in = QLineEdit("220")
        self.v_from = QComboBox(); self.v_from.addItems(["有效值 U_rms", "峰值 U_peak", "峰峰值 U_pp"])
        self.v_to = QComboBox(); self.v_to.addItems(["有效值 U_rms", "峰值 U_peak", "峰峰值 U_pp"])
        fv.addRow("输入", self.v_in)
        fv.addRow("从", self.v_from)
        fv.addRow("到", self.v_to)
        btn_v = QPushButton("转换"); btn_v.clicked.connect(self._conv_volt)
        fv.addRow("", btn_v)
        self.v_out = QLabel("—"); self.v_out.setStyleSheet("font-size:16px;color:#0071e3;font-weight:600;")
        fv.addRow("结果", self.v_out)
        lay.addWidget(g_v)

        # 角度 / 转速
        g_a = QGroupBox("角度 / 角速度 / 线速度")
        fa = QFormLayout(g_a)
        self.a_in = QLineEdit("1500")
        self.a_from = QComboBox(); self.a_from.addItems(["转速 n (r/min)", "角度 (°)", "弧度 (rad)"])
        self.a_to = QComboBox(); self.a_to.addItems(["角速度 ω (rad/s)", "角度 (°)", "弧度 (rad)"])
        fa.addRow("输入", self.a_in)
        fa.addRow("从", self.a_from)
        fa.addRow("到", self.a_to)
        btn_a = QPushButton("转换"); btn_a.clicked.connect(self._conv_angle)
        fa.addRow("", btn_a)
        self.a_out = QLabel("—"); self.a_out.setStyleSheet("font-size:16px;color:#0071e3;font-weight:600;")
        fa.addRow("结果", self.a_out)
        lay.addWidget(g_a)
        lay.addStretch()

    def _conv_temp(self):
        try:
            v = float(self.t_in.text())
            frm = self.t_from.currentIndex(); to = self.t_to.currentIndex()
            c = {0: v, 1: (v - 32) * 5/9, 2: v - 273.15}[frm]
            out = {0: c, 1: c*9/5+32, 2: c+273.15}[to]
            self.t_out.setText(f"{out:.4f}")
        except ValueError:
            self.t_out.setText("⚠️ 输入数字")

    def _conv_volt(self):
        try:
            v = float(self.v_in.text())
            frm = self.v_from.currentIndex(); to = self.v_to.currentIndex()
            rms = {0: v, 1: v/math.sqrt(2), 2: v/(2*math.sqrt(2))}[frm]
            out = {0: rms, 1: rms*math.sqrt(2), 2: rms*2*math.sqrt(2)}[to]
            self.v_out.setText(f"{out:.4f} V")
        except ValueError:
            self.v_out.setText("⚠️ 输入数字")

    def _conv_angle(self):
        try:
            v = float(self.a_in.text())
            frm = self.a_from.currentIndex(); to = self.a_to.currentIndex()
            omega = {0: v*2*math.pi/60, 1: v*math.pi/180, 2: v}[frm]
            out = {0: omega, 1: omega*180/math.pi, 2: omega}[to]
            self.a_out.setText(f"{out:.4f}")
        except ValueError:
            self.a_out.setText("⚠️ 输入数字")
