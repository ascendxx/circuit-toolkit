"""引脚定义页：选接口，显示针号-信号表。"""
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QTableWidget,
    QTableWidgetItem, QHeaderView,
)
from ..data import PINOUTS


class PinoutsPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(24, 24, 24, 24)

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
        lay.addWidget(self.table)

        self.cat.currentTextChanged.connect(self._reload_dev)
        self.dev.currentTextChanged.connect(self._reload_table)
        self._reload_dev()

    def _reload_dev(self):
        cat = self.cat.currentText()
        self.dev.blockSignals(True)
        self.dev.clear()
        # 所有分类都是 {分类: {接口名: {针号: 信号}}}
        self.dev.addItems(list(PINOUTS[cat].keys()))
        self.dev.blockSignals(False)
        self._reload_table()

    def _reload_table(self):
        cat = self.cat.currentText()
        dev_name = self.dev.currentText()
        if not dev_name:
            return
        pins = PINOUTS[cat][dev_name]
        self.table.setRowCount(len(pins))
        for r, (pin, sig) in enumerate(pins.items()):
            self.table.setItem(r, 0, QTableWidgetItem(str(pin)))
            self.table.setItem(r, 1, QTableWidgetItem(str(sig)))
