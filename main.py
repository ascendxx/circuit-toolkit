"""电路通 Circuit Toolkit - 离线电路计算工具箱入口。"""
from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from app.main_window import MainWindow
from app.theme import APP_QSS


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("Circuit Toolkit")
    app.setApplicationDisplayName("电路通 · Circuit Toolkit")
    app.setStyleSheet(APP_QSS)

    window = MainWindow()
    window.showMaximized()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
