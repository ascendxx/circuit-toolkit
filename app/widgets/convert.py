"""转换页：多 Tab 计算中心，表单居中。"""
import math
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit, QComboBox, QPushButton,
    QLabel, QTabWidget, QHBoxLayout, QSizePolicy,
)
from PyQt6.QtCore import Qt
from ..data import RESISTOR_COLOR


def _f(text):
    try:
        return float(text)
    except (TypeError, ValueError):
        return 0.0


class _BaseTab(QWidget):
    """居中表单基类。"""
    def __init__(self):
        super().__init__()
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.addStretch(2)
        holder = QWidget()
        holder.setMaximumWidth(440)
        holder.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        self.form = QFormLayout(holder)
        self.form.setVerticalSpacing(10)
        self.form.setHorizontalSpacing(12)
        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(holder)
        h.addStretch()
        outer.addLayout(h)
        outer.addStretch(3)

    def add_row(self, label, widget):
        self.form.addRow(label, widget)

    def add_button(self, text, slot):
        b = QPushButton(text)
        b.clicked.connect(slot)
        self.form.addRow("", b)
        self.result = QLabel("—")
        self.result.setObjectName("result")
        self.form.addRow("结果", self.result)


class _TempTab(_BaseTab):
    def __init__(self):
        super().__init__()
        self.t_in = QLineEdit("25")
        self.t_from = QComboBox(); self.t_from.addItems(["℃ 摄氏", "℉ 华氏", "K 开尔文"])
        self.t_to = QComboBox(); self.t_to.addItems(["℃ 摄氏", "℉ 华氏", "K 开尔文"])
        self.add_row("输入值", self.t_in)
        self.add_row("从", self.t_from)
        self.add_row("到", self.t_to)
        self.add_button("转换", self.run)
    def run(self):
        v = _f(self.t_in.text())
        c = {0: v, 1: (v-32)*5/9, 2: v-273.15}[self.t_from.currentIndex()]
        out = {0: c, 1: c*9/5+32, 2: c+273.15}[self.t_to.currentIndex()]
        self.result.setText(f"{out:.4f}")


class _VoltTab(_BaseTab):
    def __init__(self):
        super().__init__()
        self.v_in = QLineEdit("220")
        self.v_from = QComboBox(); self.v_from.addItems(["有效值 U_rms", "峰值 U_peak", "峰峰值 U_pp"])
        self.v_to = QComboBox(); self.v_to.addItems(["有效值 U_rms", "峰值 U_peak", "峰峰值 U_pp"])
        self.add_row("输入值", self.v_in)
        self.add_row("从", self.v_from)
        self.add_row("到", self.v_to)
        self.add_button("转换", self.run)
    def run(self):
        v = _f(self.v_in.text())
        rms = {0: v, 1: v/math.sqrt(2), 2: v/(2*math.sqrt(2))}[self.v_from.currentIndex()]
        out = {0: rms, 1: rms*math.sqrt(2), 2: rms*2*math.sqrt(2)}[self.v_to.currentIndex()]
        self.result.setText(f"{out:.4f} V")


class _AngleTab(_BaseTab):
    def __init__(self):
        super().__init__()
        self.a_in = QLineEdit("1500")
        self.a_from = QComboBox(); self.a_from.addItems(["转速 n (r/min)", "角度 (°)", "弧度 (rad)"])
        self.a_to = QComboBox(); self.a_to.addItems(["角速度 ω (rad/s)", "角度 (°)", "弧度 (rad)"])
        self.add_row("输入值", self.a_in)
        self.add_row("从", self.a_from)
        self.add_row("到", self.a_to)
        self.add_button("转换", self.run)
    def run(self):
        v = _f(self.a_in.text())
        omega = {0: v*2*math.pi/60, 1: v*math.pi/180, 2: v}[self.a_from.currentIndex()]
        out = {0: omega, 1: omega*180/math.pi, 2: omega}[self.a_to.currentIndex()]
        self.result.setText(f"{out:.4f}")


class _OhmTab(_BaseTab):
    def __init__(self):
        super().__init__()
        self.v = QLineEdit(); self.i = QLineEdit(); self.r = QLineEdit(); self.p = QLineEdit()
        self.add_row("电压 V (V)", self.v)
        self.add_row("电流 I (A)", self.i)
        self.add_row("电阻 R (Ω)", self.r)
        self.add_row("功率 P (W)", self.p)
        self.add_button("计算（任意填两个）", self.run)
    def run(self):
        v = _f(self.v.text()); i = _f(self.i.text())
        r = _f(self.r.text()); p = _f(self.p.text())
        if abs(v)>1e-9 and abs(i)>1e-9: r, p = v/i, v*i
        elif abs(v)>1e-9 and abs(r)>1e-9: i, p = v/r, v*i
        elif abs(v)>1e-9 and abs(p)>1e-9: i = p/v; r = v/i
        elif abs(i)>1e-9 and abs(r)>1e-9: v = i*r; p = i*i*r
        elif abs(i)>1e-9 and abs(p)>1e-9: v = p/i; r = v/i
        elif abs(r)>1e-9 and abs(p)>1e-9: i = math.sqrt(p/r); v = i*r
        else:
            self.result.setText("⚠️ 请至少填两个非零量"); return
        self.result.setText(f"V={v:.4g}  I={i:.4g}  R={r:.4g}  P={p:.4g}")


class _PowerFactorTab(_BaseTab):
    def __init__(self):
        super().__init__()
        self.p = QLineEdit(); self.u = QLineEdit(); self.i = QLineEdit()
        self.cos = QLineEdit(); self.three = QComboBox(); self.three.addItems(["单相", "三相"])
        self.add_row("有功 P (W)", self.p)
        self.add_row("电压 U (V)", self.u)
        self.add_row("电流 I (A)", self.i)
        self.add_row("cosφ (0~1)", self.cos)
        self.add_row("制式", self.three)
        self.add_button("计算（填三个求第四个）", self.run)
    def run(self):
        p = _f(self.p.text()); u = _f(self.u.text())
        i = _f(self.i.text()); c = _f(self.cos.text())
        k = math.sqrt(3) if self.three.currentIndex() == 1 else 1.0
        try:
            if p and u and i: c = p/(k*u*i)
            elif p and u and c: i = p/(k*u*c)
            elif p and i and c: u = p/(k*i*c)
            elif u and i and c: p = k*u*i*c
            else:
                self.result.setText("⚠️ 请填三个非零量"); return
        except ZeroDivisionError:
            self.result.setText("⚠️ 除零"); return
        s = k*u*i; q = math.sqrt(max(s*s-p*p, 0))
        self.result.setText(f"P={p:.4g}W  I={i:.4g}A  cosφ={c:.4f}  S={s:.4g}VA")


class _ResistorColorTab(_BaseTab):
    def __init__(self):
        super().__init__()
        colors = list(RESISTOR_COLOR.keys())
        self.c1 = QComboBox(); self.c1.addItems(colors)
        self.c2 = QComboBox(); self.c2.addItems(colors)
        self.c3 = QComboBox(); self.c3.addItems(colors)
        self.c4 = QComboBox(); self.c4.addItems(["金","银","无色","棕","红","绿","蓝","紫"])
        self.add_row("第1环（十位）", self.c1)
        self.add_row("第2环（个位）", self.c2)
        self.add_row("第3环（倍率）", self.c3)
        self.add_row("第4环（误差）", self.c4)
        self.add_button("计算阻值", self.run)
    def run(self):
        d1 = RESISTOR_COLOR[self.c1.currentText()][0]
        d2 = RESISTOR_COLOR[self.c2.currentText()][0]
        mult = RESISTOR_COLOR[self.c3.currentText()][1]
        if not isinstance(d1, int) or not isinstance(d2, int):
            self.result.setText("⚠️ 前两环不能选金/银/无色"); return
        r = (d1*10+d2) * mult
        tol = {"金":"±5%","银":"±10%","无色":"±20%","棕":"±1%","红":"±2%","绿":"±0.5%","蓝":"±0.25%","紫":"±0.1%"}
        self.result.setText(f"{r:.4g} Ω  {tol.get(self.c4.currentText(),'')}")


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
