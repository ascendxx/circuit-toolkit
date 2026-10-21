# 电路通 · Circuit Toolkit

> 给电气工程师、电工和注册电气工程师备考党的**离线电气计算综合软件**。
> 纯本地运行，不联网、不收集数据、不登录。

[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-2d74ee)](.)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776ab)](.)
[![Qt](https://img.shields.io/badge/PyQt6-6.5%2B-4CD696)](.)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## ✨ 这是什么

一个装在你电脑里的**袖珍电工计算台**。考试前不想翻公式书、现场布线不想查手册、调试电路不想开网页时，打开它直接算。

所有内容**完全离线**：没有云服务、没有埋点、没有网络请求。源码可读可改。

## 🧭 六大板块

| 板块 | 内容 |
| --- | --- |
| 🏠 **主页** | 快速入口、功能导航 |
| 🔄 **转换** | 温度换算、电压波形（峰值/峰峰值/有效值）、角度/角速度/转速互算 |
| 📚 **资源** | 色环电阻/电感代码、电线颜色标准（IEC 60446）、AWG 线规、温度传感器（PT100/Cu50/NTC/K型热电偶）、铜电阻率 |
| 🔌 **引脚定义** | USB 2.0/3.0/Type-C、HDMI、DVI、VGA、RS-232 DE9/DB25、RJ-9/11/14/25/45、PoE、FireWire、SCART、SD/SIM 卡、16x2 LCD、RGB LED、树莓派 40-pin GPIO |
| 📐 **公式集** | 电路基础、交流电路、三相、电机、变压器、功率因数、电缆线路、短路接地、单位换算、电池天线 共 10 类 80+ 公式 |
| ⭐ **收藏** | 常用公式本地收藏（JSON 持久化） |

## 📐 公式覆盖

- **电路基础**：欧姆定律、电阻/电容串并联、分压分流、KCL/KVL、RLC 谐振
- **交流/三相**：感抗容抗、阻抗、Y/Δ 变换、P/Q/S
- **电机**：同步转速、转差率、四量互算（P/U/cosφ/η）、启动电容、扭矩
- **变压器**：变比、电阻温度换算（铜/铝）、吸收比、极化指数、介损
- **功率因数**：有功/无功/视在、补偿电容（Y/Δ 接法）
- **电缆与短路**：电压降、最大长度、焦耳损耗、断路器校验、三相短路电流、接地电阻

## 🚀 快速开始

### 环境要求

- Windows 10 / 11（也支持 macOS、Linux）
- Python 3.9 及以上

### 从源码运行

```bash
git clone https://github.com/ascendxx/circuit-toolkit.git
cd circuit-toolkit
pip install -r requirements.txt
python main.py
```

### 打包成 exe（可选）

```bash
pip install pyinstaller
pyinstaller --noconfirm --windowed --name CircuitToolkit main.py
```

产物在 `dist/CircuitToolkit/`。

## 🗂️ 项目结构

```
circuit-toolkit/
├── main.py                  # 入口
├── app/
│   ├── main_window.py       # 主窗口 + 左侧导航
│   ├── theme.py             # Mac 浅色 QSS
│   ├── data/                # 数据层（纯 Python 字典）
│   │   ├── pinouts.py       # 所有接口引脚表
│   │   ├── formulas.py      # 所有公式分类
│   │   └── references.py    # 色环/AWG/温度传感器等参考表
│   └── widgets/             # 六大板块页面
│       ├── home.py
│       ├── convert.py
│       ├── resources.py
│       ├── pinouts.py
│       ├── formulas.py
│       └── favorites.py
```

## 🤝 贡献

欢迎提 Issue 报告 Bug 或建议新公式/引脚表。

## 📄 License

[MIT](LICENSE) — 随便用，改完别说是你原创就行。
