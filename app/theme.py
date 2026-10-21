"""Mac 风格浅色 QSS。"""

APP_QSS = """
QWidget {
    background: #ffffff;
    color: #1d1d1f;
    font-family: "Segoe UI", "Microsoft YaHei", "PingFang SC", sans-serif;
    font-size: 13px;
}
QMainWindow, QDialog { background: #ffffff; }
QGroupBox {
    border: 1px solid #e5e5ea;
    border-radius: 10px;
    margin-top: 12px;
    padding-top: 10px;
    font-weight: 600;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
    color: #0071e3;
}
QLineEdit, QComboBox {
    border: 1px solid #d2d2d7;
    border-radius: 6px;
    padding: 5px 8px;
    background: #fff;
    min-height: 20px;
}
QLineEdit:focus, QComboBox:focus { border-color: #0071e3; }
QPushButton {
    background: #0071e3;
    color: #fff;
    border: none;
    border-radius: 8px;
    padding: 7px 16px;
    font-weight: 500;
}
QPushButton:hover { background: #0077ed; }
QPushButton:pressed { background: #0066d6; }
QTableWidget {
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    gridline-color: #f0f0f3;
    selection-background-color: #e8f0fe;
    selection-color: #1d1d1f;
}
QHeaderView::section {
    background: #f5f5f7;
    border: none;
    border-bottom: 1px solid #e5e5ea;
    padding: 6px;
    font-weight: 600;
}
QListWidget {
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    padding: 4px;
}
QListWidget::item { padding: 6px 8px; border-radius: 6px; }
QListWidget::item:selected { background: #e8f0fe; color: #0071e3; }
QTabWidget::pane { border: 1px solid #e5e5ea; border-radius: 8px; }
QTabBar::tab {
    padding: 7px 14px;
    border: 1px solid #e5e5ea;
    border-bottom: none;
    background: #f5f5f7;
}
QTabBar::tab:selected { background: #fff; }
"""
