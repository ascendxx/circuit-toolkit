"""收藏页：本地持久化收藏的公式。"""
import json
from pathlib import Path
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem

FAV_FILE = Path.home() / ".circuit_toolkit_favs.json"


def load_favs():
    try:
        return json.loads(FAV_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def save_favs(items):
    FAV_FILE.write_text(json.dumps(items, ensure_ascii=False), encoding="utf-8")


class FavoritesPage(QWidget):
    def __init__(self):
        super().__init__()
        lay = QVBoxLayout(self)
        lay.setContentsMargins(24, 24, 24, 24)
        lay.addWidget(QLabel("<b>我的收藏</b>"))
        self.list = QListWidget()
        items = load_favs()
        if not items:
            self.list.addItem("（暂无收藏，后续版本支持从公式集收藏）")
        else:
            for it in items:
                self.list.addItem(it)
        lay.addWidget(self.list)
