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
    font-size: 15px;
    font-weight: 700;
    color: #1d1d1f;
    padding: 12px 8px 4px 8px;
}
QFrame#sidebar QLabel#subtitle {
    font-size: 11px;
    color: #86868b;
    padding: 0 8px 12px 8px;
}
QPushButton#navBtn {
    text-align: left;
    padding: 8px 12px;
    border: none;
    border-radius: 7px;
    background: transparent;
    color: #1d1d1f;
    font-size: 13px;
}
QPushButton#navBtn:hover {
    background: rgba(0,0,0,0.05);
}
QPushButton#navBtn:checked {
    background: #ffffff;
    color: #0071e3;
    font-weight: 600;
}

/* ---------- 内容区 ---------- */
QWidget#content {
    background: #ffffff;
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
    padding: 6px 10px;
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
    padding: 8px 18px;
    font-weight: 500;
    font-size: 13px;
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
    padding: 8px 10px;
    border-bottom: 1px solid #f0f0f3;
    min-height: 24px;
}
QTableWidget::item:selected {
    background: #e8f0fe;
}
QHeaderView::section {
    background: #f5f5f7;
    border: none;
    border-bottom: 1px solid #e5e5ea;
    border-right: 1px solid #f0f0f3;
    padding: 10px 8px;
    font-weight: 600;
    color: #1d1d1f;
}
QHeaderView::section:last {
    border-right: none;
}
QTableView {
    verticalScrollBarDefaultWidth: 10px;
}

/* ---------- 列表 ---------- */
QListWidget {
    border: none;
    background: transparent;
    padding: 4px;
}
QListWidget::item {
    padding: 7px 10px;
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

/* ---------- GroupBox ---------- */
QGroupBox {
    border: 1px solid #e5e5ea;
    border-radius: 10px;
    margin-top: 16px;
    padding-top: 14px;
    background: #ffffff;
    font-weight: 600;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
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
QLabel#h1 { font-size: 22px; font-weight: 700; color: #1d1d1f; }
QLabel#h2 { font-size: 15px; font-weight: 600; color: #1d1d1f; }
QLabel#muted { color: #86868b; font-size: 12px; }
QLabel#result { font-size: 18px; font-weight: 700; color: #0071e3; }
"""
