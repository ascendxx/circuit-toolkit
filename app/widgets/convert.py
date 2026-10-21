"""转换页：多 Tab 计算中心。"""
import math
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QPushButton,
    QGroupBox, QLabel, QTabWidget, QGridLayout,
)
from PyQt6.QtCore import Qt
from ..data import RESISTOR_COLOR


def _safe_float(text, default=0.0):
    try:
        v = float(text)
        return v
    except (TypeError, ValueError):
        return default


class _TempTab(QWidget):
    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        f = QFormLayout()
        self.t_in = QLineEdit("25")
        self.t_from = QComboBox(); self.t_from.addItems(["℃ 摄氏", "℉ 华氏", "K 开尔文"])
        self.t_to = QComboBox(); self.t_to.addItems(["℃ 摄氏", "℉ 华氏", "K 开尔文"])
        f.addRow("输入值", self.t_in)
        f.addRow("从", self.t_from)
        f.addRow("到", self.t_to)
        btn = QPushButton("转换"); btn.clicked.connect(self.run)
        f.addRow("", btn)
        self.out = QLabel("—"); self.out.setStyleSheet("font-size:18px;font-weight:600;color:#0071e3;")
        f.addRow("结果", self.out)
        v.addLayout(f); v.addStretch()

    def run(self):
        v = _safe_float(self.t_in.text())
        c = {0: v, 1: (v-32)*5/9, 2: v-273.15}[self.t_from.currentIndex()]
        out = {0: c, 1: c*9/5+32, 2: c+273.15}[self.t_to.currentIndex()]
        self.out.setText(f"{out:.4f}")


class _VoltTab(QWidget):
    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        f = QFormLayout()
        self.v_in = QLineEdit("220")
        self.v_from = QComboBox(); self.v_from.addItems(["有效值 U_rms", "峰值 U_peak", "峰峰值 U_pp"])
        self.v_to = QComboBox(); self.v_to.addItems(["有效值 U_rms", "峰值 U_peak", "峰峰值 U_pp"])
        f.addRow("输入值", self.v_in)
        f.addRow("从", self.v_from)
        f.addRow("到", self.v_to)
        btn = QPushButton("转换"); btn.clicked.connect(self.run)
        f.addRow("", btn)
        self.out = QLabel("—"); self.out.setStyleSheet("font-size:18px;font-weight:600;color:#0071e3;")
        f.addRow("结果", self.out)
        v.addLayout(f); v.addStretch()

    def run(self):
        v = _safe_float(self.v_in.text())
        rms = {0: v, 1: v/math.sqrt(2), 2: v/(2*math.sqrt(2))}[self.v_from.currentIndex()]
        out = {0: rms, 1: rms*math.sqrt(2), 2: rms*2*math.sqrt(2)}[self.v_to.currentIndex()]
        self.out.setText(f"{out:.4f} V")


class _AngleTab(QWidget):
    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        f = QFormLayout()
        self.a_in = QLineEdit("1500")
        self.a_from = QComboBox(); self.a_from.addItems(["转速 n (r/min)", "角度 (°)", "弧度 (rad)"])
        self.a_to = QComboBox(); self.a_to.addItems(["角速度 ω (rad/s)", "角度 (°)", "弧度 (rad)"])
        f.addRow("输入值", self.a_in)
        f.addRow("从", self.a_from)
        f.addRow("到", self.a_to)
        btn = QPushButton("转换"); btn.clicked.connect(self.run)
        f.addRow("", btn)
        self.out = QLabel("—"); self.out.setStyleSheet("font-size:18px;font-weight:600;color:#0071e3;")
        f.addRow("结果", self.out)
        v.addLayout(f); v.addStretch()

    def run(self):
        v = _safe_float(self.a_in.text())
        omega = {0: v*2*math.pi/60, 1: v*math.pi/180, 2: v}[self.a_from.currentIndex()]
        out = {0: omega, 1: omega*180/math.pi, 2: omega}[self.a_to.currentIndex()]
        self.out.setText(f"{out:.4f}")


class _OhmTab(QWidget):
    """欧姆定律：输入两个非零量求全部。"""
    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        f = QFormLayout()
        self.v = QLineEdit(); self.i = QLineEdit(); self.r = QLineEdit(); self.p = QLineEdit()
        f.addRow("电压 V (V)", self.v)
        f.addRow("电流 I (A)", self.i)
        f.addRow("电阻 R (Ω)", self.r)
        f.addRow("功率 P (W)", self.p)
        btn = QPushButton("计算（任意填两个）"); btn.clicked.connect(self.run)
        f.addRow("", btn)
        self.out = QLabel("—"); self.out.setStyleSheet("font-size:15px;font-weight:600;color:#0071e3;")
        f.addRow("结果", self.out)
        v.addLayout(f); v.addStretch()

    def run(self):
        v = _safe_float(self.v.text()); i = _safe_float(self.i.text())
        r = _safe_float(self.r.text()); p = _safe_float(self.p.text())
        if abs(v)>1e-9 and abs(i)>1e-9:
            r, p = v/i, v*i
        elif abs(v)>1e-9 and abs(r)>1e-9:
            i, p = v/r, v*i
        elif abs(v)>1e-9 and abs(p)>1e-9:
            i = p/v; r = v/i
        elif abs(i)>1e-9 and abs(r)>1e-9:
            v = i*r; p = i*r*i
        elif abs(i)>1e-9 and abs(p)>1e-9:
            v = p/i; r = v/i
        elif abs(r)>1e-9 and abs(p)>1e-9:
            i = math.sqrt(p/r); v = i*r
        else:
            self.out.setText("⚠️ 请至少填两个非零量"); return
        self.out.setText(f"V={v:.4g} V   I={i:.4g} A   R={r:.4g} Ω   P={p:.4g} W")


class _PowerFactorTab(QWidget):
    """功率因数：P/U/I/cosφ 四量互算。"""
    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        f = QFormLayout()
        self.p = QLineEdit(); self.u = QLineEdit(); self.i = QLineEdit()
        self.cos = QLineEdit(); self.three = QComboBox(); self.three.addItems(["单相", "三相"])
        f.addRow("有功 P (W)", self.p)
        f.addRow("电压 U (V)", self.u)
        f.addRow("电流 I (A)", self.i)
        f.addRow("功率因数 cosφ (0~1)", self.cos)
        f.addRow("制式", self.three)
        btn = QPushButton("计算（填三个求第四个）"); btn.clicked.connect(self.run)
        f.addRow("", btn)
        self.out = QLabel("—"); self.out.setStyleSheet("font-size:14px;font-weight:600;color:#0071e3;")
        f.addRow("结果", self.out)
        v.addLayout(f); v.addStretch()

    def run(self):
        p = _safe_float(self.p.text()); u = _safe_float(self.u.text())
        i = _safe_float(self.i.text()); c = _safe_float(self.cos.text())
        k = math.sqrt(3) if self.three.currentIndex() == 1 else 1.0
        try:
            if p and u and i:
                c = p/(k*u*i)
            elif p and u and c:
                i = p/(k*u*c)
            elif p and i and c:
                u = p/(k*i*c)
            elif u and i and c:
                p = k*u*i*c
            else:
                self.out.setText("⚠️ 请填三个非零量"); return
        except ZeroDivisionError:
            self.out.setText("⚠️ 除零"); return
        s = k*u*i
        q = math.sqrt(max(s*s-p*p, 0))
        self.out.setText(f"P={p:.4g} W  I={i:.4g} A  U={u:.4g} V  cosφ={c:.4f}\nS={s:.4g} VA  Q={q:.4g} var")


class _ResistorColorTab(QWidget):
    """色环电阻：选 4 个颜色出阻值。"""
    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        colors = list(RESISTOR_COLOR.keys())
        f = QFormLayout()
        self.c1 = QComboBox(); self.c1.addItems(colors)
        self.c2 = QComboBox(); self.c2.addItems(colors)
        self.c3 = QComboBox(); self.c3.addItems(colors)
        self.c4 = QComboBox(); self.c4.addItems(["金","银","无色","棕","红","绿","蓝","紫"])
        f.addRow("第1环（十位）", self.c1)
        f.addRow("第2环（个位）", self.c2)
        f.addRow("第3环（倍率）", self.c3)
        f.addRow("第4环（误差）", self.c4)
        btn = QPushButton("计算阻值"); btn.clicked.connect(self.run)
        f.addRow("", btn)
        self.out = QLabel("—"); self.out.setStyleSheet("font-size:16px;font-weight:600;color:#0071e3;")
        f.addRow("阻值", self.out)
        v.addLayout(f); v.addStretch()

    def run(self):
        d1 = RESISTOR_COLOR[self.c1.currentText()][0]
        d2 = RESISTOR_COLOR[self.c2.currentText()][0]
        mult = RESISTOR_COLOR[self.c3.currentText()][1]
        if not isinstance(d1, int) or not isinstance(d2, int):
            self.out.setText("⚠️ 前两环不能选金/银/无色"); return
        r = (d1*10+d2) * mult
        tol_map = {"金":"±5%","银":"±10%","无色":"±20%","棕":"±1%","红":"±2%","绿":"±0.5%","蓝":"±0.25%","紫":"±0.1%"}
        self.out.setText(f"{r:.4g} Ω  {tol_map.get(self.c4.currentText(),'')}")


class ConvertPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 20, 20, 20)
        tabs = QTabWidget()
        tabs.addTab(_TempTab(), "温度")
        tabs.addTab(_VoltTab(), "电压波形")
        tabs.addTab(_AngleTab(), "角度/转速")
        tabs.addTab(_OhmTab(), "欧姆定律")
        tabs.addTab(_PowerFactorTab(), "功率因数")
        tabs.addTab(_ResistorColorTab(), "色环电阻")
        lay.addWidget(tabs)
