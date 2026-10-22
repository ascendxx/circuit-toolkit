"""macOS 风格浅色主题 QSS。"""

APP_QSS = """
* {
    font-family: -apple-system, "SF Pro Text", "Segoe UI", "Microsoft YaHei", "PingFang SC", sans-serif;
    font-size: 13px;
    color: #1d1d1f;
}

QMainWindow, QDialog, QWidget#central {
    background: #f5f5f7;
}

/* ---------- 侧栏 ---------- */
QFrame#sidebar {
    background: #f5f5f7;
    border-right: 1px solid #e5e5ea;
}
QFrame#sidebar QLabel#logo {
    font-size: 14px;
    font-weight: 700;
    color: #1d1d1f;
    padding: 16px 12px 2px 12px;
}
QFrame#sidebar QLabel#subtitle {
    font-size: 11px;
    color: #86868b;
    padding: 0 12px 16px 12px;
}
QPushButton#navBtn {
    text-align: left;
    padding: 9px 12px;
    border: none;
    border-radius: 7px;
    background: transparent;
    color: #1d1d1f;
    font-size: 13px;
    margin: 1px 6px;
}
QPushButton#navBtn:hover {
    background: rgba(0,0,0,0.05);
}
QPushButton#navBtn:checked {
    background: #ffffff;
    color: #0071e3;
    font-weight: 600;
}

/* ---------- 卡片 ---------- */
QFrame#card {
    background: #ffffff;
    border: 1px solid #e5e5ea;
    border-radius: 10px;
}

/* ---------- 输入 ---------- */
QLineEdit, QComboBox {
    border: 1px solid #d2d2d7;
    border-radius: 6px;
    padding: 7px 10px;
    background: #ffffff;
    min-height: 20px;
    selection-background-color: #0071e3;
}
QLineEdit:focus, QComboBox:focus {
    border: 1.5px solid #0071e3;
}
QLineEdit:disabled {
    background: #f5f5f7;
    color: #86868b;
}

/* ---------- 按钮 ---------- */
QPushButton {
    background: #0071e3;
    color: #ffffff;
    border: none;
    border-radius: 7px;
    padding: 8px 20px;
    font-weight: 500;
    font-size: 13px;
    min-height: 20px;
}
QPushButton:hover { background: #147cec; }
QPushButton:pressed { background: #0066d6; }
QPushButton:disabled { background: #99bfe8; }

QPushButton#secondary {
    background: #e8e8ed;
    color: #1d1d1f;
}
QPushButton#secondary:hover { background: #dcdce0; }

/* ---------- 表格 ---------- */
QTableWidget {
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    background: #ffffff;
    gridline-color: #f0f0f3;
    selection-background-color: #e8f0fe;
    selection-color: #1d1d1f;
    outline: none;
}
QTableWidget::item {
    padding: 10px 12px;
    border-bottom: 1px solid #f0f0f3;
}
QTableWidget::item:selected {
    background: #e8f0fe;
}
QHeaderView::section {
    background: #f5f5f7;
    border: none;
    border-bottom: 1px solid #e5e5ea;
    border-right: 1px solid #f0f0f3;
    padding: 12px 10px;
    font-weight: 600;
    color: #1d1d1f;
    font-size: 12px;
}
QHeaderView::section:last {
    border-right: none;
}

/* ---------- 列表 ---------- */
QListWidget {
    border: none;
    background: transparent;
    padding: 4px;
}
QListWidget::item {
    padding: 8px 10px;
    border-radius: 6px;
}
QListWidget::item:hover {
    background: rgba(0,0,0,0.04);
}
QListWidget::item:selected {
    background: #e8f0fe;
    color: #0071e3;
}

/* ---------- Tab ---------- */
QTabWidget::pane {
    border: 1px solid #e5e5ea;
    border-radius: 8px;
    background: #ffffff;
    top: -1px;
}
QTabBar::tab {
    padding: 8px 16px;
    border: 1px solid #e5e5ea;
    border-bottom: none;
    background: #f5f5f7;
    margin-right: 2px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}
QTabBar::tab:selected {
    background: #ffffff;
    color: #0071e3;
}

/* ---------- 滚动条 ---------- */
QScrollBar:vertical {
    background: transparent;
    width: 10px;
    margin: 2px;
}
QScrollBar::handle:vertical {
    background: #c1c1c6;
    border-radius: 5px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover {
    background: #a1a1a6;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

/* ---------- Label ---------- */
QLabel { background: transparent; }
QLabel#h1 { font-size: 24px; font-weight: 700; color: #1d1d1f; }
QLabel#h2 { font-size: 16px; font-weight: 600; color: #1d1d1f; }
QLabel#muted { color: #86868b; font-size: 12px; }
QLabel#result { font-size: 20px; font-weight: 700; color: #0071e3; }
QLabel#statNum { font-size: 28px; font-weight: 700; color: #0071e3; }
"""
