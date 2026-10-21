"""浅色 Mac 风格 QSS 主题。"""

# 配色参考 macOS Sonoma 浅色外观
BG_WINDOW = "#f5f5f7"
BG_CARD = "#ffffff"
TEXT_PRIMARY = "#1d1d1f"
TEXT_SECONDARY = "#6e6e73"
ACCENT = "#0a84ff"
BORDER = "#d2d2d7"
RESULT_BG = "#eef5ff"
RESULT_TEXT = "#003c99"

APP_QSS = f"""
QWidget {{
    background-color: {BG_WINDOW};
    color: {TEXT_PRIMARY};
    font-family: "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
    font-size: 14px;
}}

#Sidebar {{
    background-color: {BG_WINDOW};
    border-right: 1px solid {BORDER};
    min-width: 220px;
    max-width: 260px;
}}

#SidebarTitle {{
    font-size: 18px;
    font-weight: 600;
    padding: 20px 18px 8px 18px;
    color: {TEXT_PRIMARY};
}}

#SidebarSubtitle {{
    font-size: 12px;
    color: {TEXT_SECONDARY};
    padding: 0 18px 16px 18px;
}}

QListWidget {{
    background-color: transparent;
    border: none;
    outline: none;
    padding: 4px 8px;
}}

QListWidget::item {{
    padding: 10px 12px;
    border-radius: 8px;
    color: {TEXT_PRIMARY};
}}

QListWidget::item:hover {{
    background-color: rgba(0, 0, 0, 0.04);
}}

QListWidget::item:selected {{
    background-color: {ACCENT};
    color: white;
}}

#ContentCard {{
    background-color: {BG_CARD};
    border: 1px solid {BORDER};
    border-radius: 12px;
}}

QLineEdit, QComboBox, QDoubleSpinBox {{
    background-color: white;
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 6px 10px;
    min-height: 20px;
    selection-background-color: {ACCENT};
}}

QLineEdit:focus, QComboBox:focus, QDoubleSpinBox:focus {{
    border: 1px solid {ACCENT};
}}

QPushButton {{
    background-color: {ACCENT};
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 18px;
    font-weight: 500;
    min-height: 20px;
}}

QPushButton:hover {{
    background-color: #339bff;
}}

QPushButton:pressed {{
    background-color: #0066d6;
}}

QPushButton#secondary {{
    background-color: #e8e8ed;
    color: {TEXT_PRIMARY};
}}

QPushButton#secondary:hover {{
    background-color: #dedee3;
}}

#ResultBox {{
    background-color: {RESULT_BG};
    border: 1px solid #cfe2ff;
    border-radius: 10px;
    padding: 14px 16px;
    color: {RESULT_TEXT};
    font-size: 15px;
}}

QLabel#h1 {{
    font-size: 22px;
    font-weight: 600;
    color: {TEXT_PRIMARY};
}}

QLabel#h2 {{
    font-size: 14px;
    color: {TEXT_SECONDARY};
}}

QLabel#fieldLabel {{
    color: {TEXT_SECONDARY};
}}
"""
