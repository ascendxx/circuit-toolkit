"""公式集页：搜索 + 分类 + 表格 + 计算卡片。"""
import math
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QTableWidget, QTableWidgetItem, QHeaderView, QLabel, QLineEdit,
    QPushButton, QFormLayout, QFrame, QSizePolicy,
)
from PyQt6.QtCore import Qt
from ..data import FORMULAS
from .favorites import load_favs, save_favs

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
        self.cat.addItem("全部")
        for k in FORMULAS.keys():
            QListWidgetItem(k, self.cat)
        self.cat.setCurrentRow(0)
        self.cat.currentRowChanged.connect(self._load_table)
        lv.addWidget(self.cat)
        root.addWidget(left)

        right = QVBoxLayout()
        right.setSpacing(10)

        search_row = QHBoxLayout()
        self.search = QLineEdit()
        self.search.setPlaceholderText("搜索公式名称或关键词…")
        self.search.textChanged.connect(self._filter)
        search_row.addWidget(self.search, 1)
        self.fav_btn = QPushButton("☆ 收藏此公式")
        self.fav_btn.setObjectName("secondary")
        self.fav_btn.clicked.connect(self._toggle_fav)
        self.fav_btn.setEnabled(False)
        search_row.addWidget(self.fav_btn)
        right.addLayout(search_row)

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
        self.table.itemDoubleClicked.connect(self._compute)
        right.addWidget(self.table, 3)

        calc = QFrame()
        calc.setObjectName("card")
        cv = QVBoxLayout(calc)
        cv.setContentsMargins(16, 14, 16, 14)
        cv.setSpacing(10)
        calc_title = QLabel("计算（双击表格行或按回车）")
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
        self._all_rows = []
        self._input_edits = []
        self._load_table()

    def _current_category(self):
        item = self.cat.currentItem()
        if not item or item.text() == "全部":
            return None
        return item.text()

    def _rows_for_category(self, cat):
        if cat is None:
            return [(c, f) for c, fs in FORMULAS.items() for f in fs]
        return [(cat, f) for f in FORMULAS[cat]]

    def _load_table(self):
        self._all_rows = self._rows_for_category(self._current_category())
        cat_name = "全部" if self._current_category() is None else self._current_category()
        self.title.setText(f"{cat_name}（{len(self._all_rows)} 条公式）")
        self._filter()

    def _filter(self):
        kw = self.search.text().strip().lower()
        rows = self._all_rows
        if kw:
            rows = [(c, f) for c, f in rows
                    if kw in f["name"].lower() or kw in f["expr"].lower() or kw in f["note"].lower()]
        self.table.setRowCount(len(rows))
        for r, (cat, f) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(f["name"]))
            self.table.setItem(r, 1, QTableWidgetItem(f["expr"]))
            self.table.setItem(r, 2, QTableWidgetItem(f"{cat} · {f['note']}"))
        self.table.clearSelection()
        self._clear_form()
        self.calc_result.setText("← 从上方选择一条公式开始")
        self._current = None
        self.fav_btn.setEnabled(False)

    def _clear_form(self):
        while self.calc_form.rowCount() > 0:
            self.calc_form.removeRow(0)
        self._input_edits = []

    def _selected_row_data(self):
        rows = self.table.selectedItems()
        if not rows:
            return None
        r = rows[0].row()
        kw = self.search.text().strip().lower()
        all_rows = self._all_rows
        if kw:
            all_rows = [(c, f) for c, f in all_rows
                        if kw in f["name"].lower() or kw in f["expr"].lower() or kw in f["note"].lower()]
        if r < len(all_rows):
            return all_rows[r]
        return None

    def _on_select(self):
        data = self._selected_row_data()
        if not data:
            return
        cat, f = data
        self._current = f
        self.fav_btn.setEnabled(True)
        self._update_fav_btn()
        self._clear_form()
        self._input_edits = []
        for name, unit, default in f["inputs"]:
            le = QLineEdit(str(default))
            le.setMinimumWidth(140)
            le.returnPressed.connect(self._compute)
            lab = QLabel(name)
            lab.setMinimumWidth(70)
            unit_lab = QLabel(unit)
            unit_lab.setStyleSheet("color:#86868b;font-weight:400;")
            row = QHBoxLayout()
            row.addWidget(lab)
            row.addWidget(le, 1)
            row.addWidget(unit_lab)
            self.calc_form.addRow("", row)
            self._input_edits.append(le)
        self.calc_result.setText("填好参数，点「计算」或按回车")
        if self._input_edits:
            self._input_edits[0].setFocus()
            self._input_edits[0].selectAll()

    def _compute(self):
        f = self._current
        if not f:
            self.calc_result.setText("先选一条公式")
            return
        env = dict(_SAFE)
        try:
            nums = []
            for i, (name, _, default) in enumerate(f["inputs"]):
                txt = self._input_edits[i].text().strip()
                if not txt:
                    continue
                try:
                    nums.append(float(txt))
                except ValueError:
                    raise ValueError(f"参数 {name} 不是有效数字：{txt}")
            if not nums:
                raise ValueError("至少填一个参数")

            combine = f.get("combine")
            if combine == "series":
                val = sum(nums)
            elif combine == "parallel":
                val = 1.0 / sum(1.0 / x for x in nums)
            else:
                env = dict(_SAFE)
                for i, (name, _, _) in enumerate(f["inputs"]):
                    txt = self._input_edits[i].text().strip()
                    if txt:
                        env[name] = float(txt)
                val = eval(f["compute"], {"__builtins__": {}}, env)

            if math.isnan(val) or math.isinf(val):
                raise ValueError("结果异常（除零或超出范围）")
            self.calc_result.setText(f"{f['output']} = {val:.6g}")
        except ValueError as e:
            self.calc_result.setText(f"⚠️ {e}")
        except ZeroDivisionError:
            self.calc_result.setText("⚠️ 分母不能为零")
        except Exception as e:
            self.calc_result.setText(f"⚠️ 计算错误：{type(e).__name__}")

    def _toggle_fav(self):
        if not self._current:
            return
        items = load_favs()
        key = f"{self._current['name']}  （{self._current['expr']}）"
        if key in items:
            items.remove(key)
        else:
            items.append(key)
        save_favs(items)
        self._update_fav_btn()

    def _update_fav_btn(self):
        if not self._current:
            return
        items = load_favs()
        key = f"{self._current['name']}  （{self._current['expr']}）"
        self.fav_btn.setText("★ 已收藏" if key in items else "☆ 收藏此公式")
