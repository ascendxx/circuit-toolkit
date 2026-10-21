# 电路通 · Circuit Toolkit

> 给电气工程师、电工和注册电气工程师备考党的**离线电路计算工具箱**。
> 纯本地运行，不联网、不收集数据、不登录。

[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-2d74ee)](.)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776ab)](.)
[![Qt](https://img.shields.io/badge/PyQt6-6.5%2B-4CD696)](.)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## ✨ 这是什么

一个装在你电脑里的**袖珍电工计算台**。考试前不想翻公式书、现场布线不想查手册、调试电路不想开网页时，打开它直接算。

所有计算**完全离线**：没有云服务、没有埋点、没有网络请求。源码可读可改，适合拿来做二次开发。

## 🧰 内置计算器

| 模块 | 解决什么问题 |
| --- | --- |
| ⚡ 欧姆定律与功率 | V / I / R / P 四量互算，交直流通用 |
| 🔌 电阻串并联 | 任意数量电阻的串、并混联等效 |
| 🎚️ 分压与分流 | 快速估算分压器输出、分流电阻 |
| 🔄 戴维南等效 | 由开路电压与内阻算任意负载电流/电压 |
| 🔺 三相电路 | 线/相电压电流换算、功率因数、P/Q/S |
| 📏 单位换算 | Ω / V / A / W / F / H 全量级换算 |
| 🧵 电缆载流量 | 常用铜芯线安全载流量速查（布线参考） |

## 📸 界面预览

<!-- 截图放这里：把截图存到 assets/screenshot.png 后取消下一行注释 -->
<!-- ![界面预览](assets/screenshot.png) -->

浅色 Mac 风格 UI，启动即最大化，自适应窗口大小。

## 🚀 快速开始

### 环境要求

- Windows 10 / 11（也支持 macOS、Linux）
- Python 3.9 及以上

### 从源码运行

```bash
git clone https://github.com/<你的用户名>/circuit-toolkit.git
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

## 🗺️ 路线图

- [ ] 节点电压法 / 网孔电流法求解器（发输电考点）
- [ ] 运放电路反相/同相放大计算
- [ ] 简单 RLC 暂态过程计算
- [ ] 自定义常用参数收藏
- [ ] 更多电缆规格与敷设方式修正系数

欢迎提 Issue 告诉我你最想要哪个计算器。

## 🤝 贡献

这个项目由一个人在业余时间维护，但欢迎任何人：

- 提 Issue 报告 Bug 或建议新计算器
- 提 PR 新增模块（每个计算器就是一个独立 QWidget，照 `app/calculators/` 下现有文件抄一个改即可）
- 把它推荐给你身边备考电气工程师、做弱电布线的朋友

## 📄 License

[MIT](LICENSE) — 随便用，改完别说是你原创就行。
