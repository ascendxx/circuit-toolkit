"""公式集页：左侧分类，中间公式表，点选后下方出计算表单。"""
import math
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QLineEdit,
    QPushButton, QFormLayout, QGroupBox,
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

        # 左：分类
        self.cat = QListWidget()
        self.cat.setMaximumWidth(160)
        for k in FORMULAS.keys():
            QListWidgetItem(k, self.cat)
        self.cat.setCurrentRow(0)
        self.cat.currentRowChanged.connect(self._load_table)
        root.addWidget(self.cat)

        # 右：上=表格，下=计算
        right = QVBoxLayout()
        self.title = QLabel()
        self.title.setStyleSheet("font-size:16px;font-weight:600;")
        right.addWidget(self.title)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["公式名称", "表达式", "说明"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setMaximumHeight(280)
        self.table.itemSelectionChanged.connect(self._on_select)
        right.addWidget(self.table)

        # 计算区
        self.calc_box = QGroupBox("计算")
        self.calc_layout = QFormLayout(self.calc_box)
        self.calc_inputs: dict[str, QLineEdit] = {}
        self.calc_btn = QPushButton("计算")
        self.calc_btn.clicked.connect(self._compute)
        self.calc_layout.addRow("", self.calc_btn)
        self.calc_result = QLabel("—")
        self.calc_result.setStyleSheet("font-size:16px;font-weight:600;color:#0071e3;")
        self.calc_layout.addRow("结果", self.calc_result)
        right.addWidget(self.calc_box)
        root.addLayout(right, 1)

        self._load_table()

    def _current_formulas(self):
        cat = self.cat.currentItem().text() if self.cat.currentItem() else list(FORMULAS.keys())[0]
        return FORMULAS[cat]

    def _load_table(self):
        rows = self._current_formulas()
        self.title.setText(f"{self.cat.currentItem().text() if self.cat.currentItem() else ''}（{len(rows)} 条）")
        self.table.setRowCount(len(rows))
        for r, f in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(f["name"]))
            self.table.setItem(r, 1, QTableWidgetItem(f["expr"]))
            self.table.setItem(r, 2, QTableWidgetItem(f["note"]))
        self.table.clearSelection()
        self.calc_result.setText("—")

    def _on_select(self):
        rows = self.table.selectedItems()
        if not rows:
            return
        r = rows[0].row()
        f = self._current_formulas()[r]
        # 清旧输入
        while self.calc_layout.rowCount() > 2:
            item = self.calc_layout.takeRow(0)
        self.calc_inputs.clear()
        # 加新输入（插在按钮前）
        for i, (name, unit, default) in enumerate(f["inputs"]):
            le = QLineEdit(str(default))
            label = f"{name} ({unit})"
            self.calc_layout.insertRow(i, label, le)
            self.calc_inputs[name] = le
        self.calc_result.setText("—")
        self._current = f

    def _compute(self):
        f = getattr(self, "_current", None)
        if not f:
            self.calc_result.setText("先选一条公式")
            return
        env = dict(_SAFE)
        try:
            for name, le in self.calc_inputs.items():
                env[name] = float(le.text())
            val = eval(f["compute"], {"__builtins__": {}}, env)
            self.calc_result.setText(f"{f['output']} = {val:.6g}")
        except Exception as e:
            self.calc_result.setText(f"⚠️ 错误: {e}")
