"""公式集页：左侧分类，右侧表格 + 计算卡片。"""
import math
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QLineEdit,
    QPushButton, QFormLayout, QFrame, QSizePolicy,
)
from PyQt6.QtCore import Qt
from ..data import FORMULAS

_SAFE = {
    "pi": math.pi, "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,
    "tan": math.tan, "log": math.log, "exp": math.exp, "abs": abs,
}


class FormulasPage(QWidget):
    def __init__(self):
        super().__init__()
        root = QHBoxLayout(self)
        root.setContentsMargins(20, 20, 20, 20)
        root.setSpacing(16)

        # 左：分类
        left = QFrame()
        left.setObjectName("card")
        left.setFixedWidth(160)
        lv = QVBoxLayout(left)
        lv.setContentsMargins(8, 12, 8, 12)
        lv.setSpacing(4)
        cat_title = QLabel("分类")
        cat_title.setStyleSheet("font-weight:600;padding:4px 8px;")
        lv.addWidget(cat_title)
        self.cat = QListWidget()
        self.cat.setFrameShape(QFrame.Shape.NoFrame)
        self.cat.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        for k in FORMULAS.keys():
            QListWidgetItem(k, self.cat)
        self.cat.setCurrentRow(0)
        self.cat.currentRowChanged.connect(self._load_table)
        lv.addWidget(self.cat)
        root.addWidget(left)

        # 右：表格 + 计算卡片
        right = QVBoxLayout()
        right.setSpacing(12)

        self.title = QLabel()
        self.title.setObjectName("h2")
        right.addWidget(self.title)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["公式名称", "表达式", "说明"])
        hh = self.table.horizontalHeader()
        hh.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        hh.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        hh.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setDefaultSectionSize(34)
        self.table.itemSelectionChanged.connect(self._on_select)
        right.addWidget(self.table, 3)

        # 计算卡片
        calc = QFrame()
        calc.setObjectName("card")
        cv = QVBoxLayout(calc)
        cv.setContentsMargins(16, 14, 16, 14)
        cv.setSpacing(10)
        calc_title = QLabel("计算")
        calc_title.setStyleSheet("font-weight:600;color:#0071e3;")
        cv.addWidget(calc_title)

        self.calc_form = QFormLayout()
        self.calc_form.setHorizontalSpacing(12)
        self.calc_form.setVerticalSpacing(8)
        cv.addLayout(self.calc_form)

        btn_row = QHBoxLayout()
        self.calc_btn = QPushButton("计算")
        self.calc_btn.setMinimumWidth(110)
        self.calc_btn.clicked.connect(self._compute)
        self.calc_result = QLabel("← 从上方选择一条公式开始")
        self.calc_result.setObjectName("result")
        btn_row.addWidget(self.calc_btn)
        btn_row.addWidget(self.calc_result, 1)
        cv.addLayout(btn_row)
        cv.addStretch()

        right.addWidget(calc, 2)
        root.addLayout(right, 1)

        self._current = None
        self._load_table()

    def _current_formulas(self):
        cat = self.cat.currentItem().text() if self.cat.currentItem() else list(FORMULAS.keys())[0]
        return FORMULAS[cat]

    def _clear_form(self):
        while self.calc_form.rowCount() > 0:
            self.calc_form.removeRow(0)

    def _load_table(self):
        rows = self._current_formulas()
        cat_name = self.cat.currentItem().text() if self.cat.currentItem() else ""
        self.title.setText(f"{cat_name}（{len(rows)} 条公式）")
        self.table.setRowCount(len(rows))
        for r, f in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(f["name"]))
            self.table.setItem(r, 1, QTableWidgetItem(f["expr"]))
            self.table.setItem(r, 2, QTableWidgetItem(f["note"]))
        self.table.clearSelection()
        self._clear_form()
        self.calc_result.setText("← 从上方选择一条公式开始")
        self._current = None

    def _on_select(self):
        rows = self.table.selectedItems()
        if not rows:
            return
        r = rows[0].row()
        f = self._current_formulas()[r]
        self._current = f
        self._clear_form()
        for name, unit, default in f["inputs"]:
            le = QLineEdit(str(default))
            le.setMinimumWidth(140)
            lab = QLabel(name)
            lab.setMinimumWidth(70)
            unit_lab = QLabel(unit)
            unit_lab.setStyleSheet("color:#86868b;font-weight:400;")
            row = QHBoxLayout()
            row.addWidget(lab)
            row.addWidget(le, 1)
            row.addWidget(unit_lab)
            self.calc_form.addRow("", row)
        self.calc_result.setText("填好参数，点「计算」")

    def _compute(self):
        f = self._current
        if not f:
            self.calc_result.setText("先选一条公式")
            return
        env = dict(_SAFE)
        try:
            for i, (name, _, _) in enumerate(f["inputs"]):
                item = self.calc_form.itemAt(i, QFormLayout.ItemRole.FieldRole)
                if item:
                    w = item.widget()
                    if isinstance(w, QLineEdit):
                        env[name] = float(w.text())
                    else:
                        le = w.findChildren(QLineEdit)[0]
                        env[name] = float(le.text())
            val = eval(f["compute"], {"__builtins__": {}}, env)
            self.calc_result.setText(f"{f['output']} = {val:.6g}")
        except Exception as e:
            self.calc_result.setText(f"⚠️ {e}")
