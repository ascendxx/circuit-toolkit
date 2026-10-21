"""常用铜芯电缆载流量速查（30℃ 空气敷设参考值）。"""
from __future__ import annotations

from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from .base import CalculatorBase

# 数据来源：GB/T 16895 与电工手册常用参考值（铜芯、聚氯乙烯绝缘、空气中 30℃）
# 仅供现场快速估算，实际选型需按敷设方式、环境温度、穿管系数修正。
TABLE = [
    ("1.5", 18, 15),
    ("2.5", 26, 22),
    ("4",   35, 30),
    ("6",   45, 39),
    ("10",  63, 52),
    ("16",  85, 70),
    ("25",  113, 95),
    ("35",  138, 117),
    ("50",  170, 145),
    ("70",  215, 185),
    ("95",  260, 225),
    ("120", 300, 260),
]


class CableAmpacityWidget(CalculatorBase):
    title = "铜芯电缆载流量速查"
    subtitle = (
        "铜芯聚氯乙烯绝缘电缆、空气中 30℃ 敷设的参考载流量（A）。"
        "现场实际选型请按穿管、环境温度、并排系数修正，本表仅作快速估算。"
    )

    def __init__(self) -> None:
        super().__init__()
        table_host = QWidget()
        layout = QVBoxLayout(table_host)
        layout.setContentsMargins(0, 0, 0, 0)

        self.table = QTableWidget(len(TABLE), 3)
        self.table.setHorizontalHeaderLabels(
            ["标称截面 mm²", "明敷载流量 A", "穿管载流量 A"]
        )
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setColumnWidth(0, 140)
        self.table.setColumnWidth(1, 160)
        self.table.setColumnWidth(2, 160)
        for row, (mm2, air, conduit) in enumerate(TABLE):
            for col, val in enumerate((mm2, air, conduit)):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))

        layout.addWidget(self.table)
        # 把表格插在副标题和结果框之间
        self.layout().insertWidget(2, table_host)

        self.set_result(
            "提示：环境温度每升高 5℃，载流量约下降 5%；多根并排敷设需再乘 0.7~0.9 系数。"
        )
