"""收藏页：本地持久化。"""
import json
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

FAV_FILE = Path.home() / ".circuit_toolkit_favs.json"


def load_favs():
    try:
        return json.loads(FAV_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


class FavoritesPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 20, 20, 20)
        title = QLabel("我的收藏")
        title.setObjectName("h2")
        lay.addWidget(title)
        self.list = QListWidget()
        items = load_favs()
        if not items:
            self.list.addItem("（暂无收藏）")
        else:
            for it in items:
                self.list.addItem(it)
        lay.addWidget(self.list)
