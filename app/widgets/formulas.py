"""公式集页：左侧分类树，右侧公式列表。"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QTableWidget, QTableWidgetItem, QHeaderView, QLabel,
)
from ..data import FORMULAS


class FormulasPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QHBoxLayout(self)
        lay.setContentsMargins(24, 24, 24, 24)

        self.cat = QListWidget()
        self.cat.setMaximumWidth(180)
        for k in FORMULAS.keys():
            QListWidgetItem(k, self.cat)
        self.cat.setCurrentRow(0)
        self.cat.currentRowChanged.connect(self._reload)
        lay.addWidget(self.cat)

        right = QVBoxLayout()
        self.title = QLabel()
        self.title.setStyleSheet("font-size:16px;font-weight:600;")
        right.addWidget(self.title)
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["公式名称", "表达式", "变量说明"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        right.addWidget(self.table)
        lay.addLayout(right, 1)
        self._reload()

    def _reload(self):
        cat = self.cat.currentItem().text() if self.cat.currentItem() else list(FORMULAS.keys())[0]
        self.title.setText(cat)
        rows = FORMULAS[cat]
        self.table.setRowCount(len(rows))
        for r, (name, expr, note) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(name))
            self.table.setItem(r, 1, QTableWidgetItem(expr))
            self.table.setItem(r, 2, QTableWidgetItem(note))
