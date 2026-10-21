"""引脚定义页：选接口，显示针号-信号表。"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QTableWidget,
    QTableWidgetItem, QHeaderView, QFrame,
)
from ..data import PINOUTS


class PinoutsPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 20, 20, 20)

        title = QLabel("引脚定义")
        title.setObjectName("h2")
        lay.addWidget(title)

        top = QHBoxLayout()
        top.addWidget(QLabel("分类："))
        self.cat = QComboBox()
        self.cat.addItems(list(PINOUTS.keys()))
        top.addWidget(self.cat)
        top.addWidget(QLabel("接口："))
        self.dev = QComboBox()
        top.addWidget(self.dev)
        top.addStretch()
        lay.addLayout(top)

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["针号", "信号 / 功能"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        lay.addWidget(self.table)

        self.cat.currentTextChanged.connect(self._reload_dev)
        self.dev.currentTextChanged.connect(self._reload_table)
        self._reload_dev()

    def _reload_dev(self):
        cat = self.cat.currentText()
        self.dev.blockSignals(True)
        self.dev.clear()
        self.dev.addItems(list(PINOUTS[cat].keys()))
        self.dev.blockSignals(False)
        self._reload_table()

    def _reload_table(self):
        cat = self.cat.currentText()
        dev = self.dev.currentText()
        if not dev:
            return
        pins = PINOUTS[cat][dev]
        self.table.setRowCount(len(pins))
        for r, (pin, sig) in enumerate(pins.items()):
            self.table.setItem(r, 0, QTableWidgetItem(str(pin)))
            self.table.setItem(r, 1, QTableWidgetItem(str(sig)))
