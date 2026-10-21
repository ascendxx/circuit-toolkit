"""所有接口引脚定义数据。按接口分组，每项 {针号: 信号名}。"""

# IEEE 1394 FireWire
FIREWIRE = {
    "4针 Plug": {1: "B-", 2: "B+", 3: "A-", 4: "A+"},
    "6针 Plug": {1: "未稳压DC(空载30V)", 2: "电源/内屏蔽地", 3: "B-", 4: "B+", 5: "A-", 6: "A+"},
    "9针 Plug": {1: "B-", 2: "B+", 3: "A-", 4: "A+", 5: "A屏蔽", 6: "电源/内屏蔽地", 7: "空", 8: "未稳压DC(空载30V)", 9: "B屏蔽"},
}

# RJ 系列
RJ = {
    "RJ-9 (4P4C 话筒)": {1: "R1", 2: "T1", 3: "T2", 4: "R2"},
    "RJ-11 (6P2C)": {1: "TIP1", 2: "RING1", 3: "TIP2", 4: "RING2", 5: "空", 6: "空"},
    "RJ-14 (6P4C)": {1: "TIP1", 2: "RING1", 3: "TIP2", 4: "RING2", 5: "空", 6: "空"},
    "RJ-25 (6P6C)": {1: "TIP1", 2: "RING1", 3: "TIP2", 4: "RING2", 5: "TIP3", 6: "RING3"},
    "RJ-48 (E1/T1)": {1: "TX+", 2: "TX-", 3: "RX+", 4: "RX-", 5: "空", 6: "空", 7: "空", 8: "空"},
}

# RJ-45 EIA/TIA-568B
RJ45_568B = {1: "TX+ (白橙)", 2: "TX- (橙)", 3: "RX+ (白绿)", 4: "蓝", 5: "白蓝", 6: "RX- (绿)", 7: "白棕", 8: "棕"}

# PoE IEEE 802.3af
POE_MODE_A = {1: "DC+", 2: "DC+", 3: "DC-", 4: "-", 5: "-", 6: "DC-", 7: "-", 8: "-"}
POE_MODE_B = {1: "-", 2: "-", 3: "-", 4: "DC+", 5: "DC+", 6: "-", 7: "DC-", 8: "DC-"}

# RS-232
RS232_DE9 = {
    1: "DCD 数据载波检测", 2: "RXD 接收数据", 3: "TXD 发送数据",
    4: "DTR 数据终端就绪", 5: "GND 信号地", 6: "DSR 数据设备就绪",
    7: "RTS 请求发送", 8: "CTS 清除发送", 9: "RI 振铃指示",
}
RS232_DB25 = {
    1: "PG 保护地", 2: "TXD", 3: "RXD", 4: "RTS", 5: "CTS", 6: "DSR",
    7: "GND", 8: "DCD", 9: "RI", 10: "空", 11: "空", 12: "DCD(辅助)",
    13: "CTS(辅助)", 14: "TXD(辅助)", 15: "TXD 时钟", 16: "RXD(辅助)",
    17: "RXD 时钟", 18: "空", 19: "RTS(辅助)", 20: "DTR", 21: "空",
    22: "RI", 23: "空", 24: "TXD 时钟", 25: "DCD",
}

# SCART (21针)
SCART = {
    1: "音频右出", 2: "音频右入", 3: "音频左出", 4: "音频地", 5: "RGB地",
    6: "音频左入", 7: "蓝色", 8: "AV 开/识别", 9: "RGB地", 10: "串行数据",
    11: "绿色", 12: "串行时钟", 13: "RGB地", 14: "空", 15: "红色",
    16: "RGB 切换", 17: "复合视频地", 18: "复合视频地", 19: "复合视频出",
    20: "复合视频入", 21: "屏蔽地",
}

# DVI (DVI-I 母座)
DVI = {
    1: "TMDS Data2-", 2: "TMDS Data2+", 3: "TMDS Data2/4 GND",
    4: "TMDS Data4-", 5: "TMDS Data4+", 6: "DDC Clock", 7: "DDC Data",
    8: "Analog VSync", 9: "TMDS Data1-", 10: "TMDS Data1+", 11: "TMDS Data1/3 GND",
    12: "TMDS Data3-", 13: "TMDS Data3+", 14: "+5V", 15: "GND", 16: "Hot Plug",
    17: "TMDS Data0-", 18: "TMDS Data0+", 19: "TMDS Data0/5 GND",
    20: "TMDS Data5-", 21: "TMDS Data5+", 22: "TMDS Clock GND", 23: "TMDS Clock+",
    24: "TMDS Clock-",
    "C1": "Analog Red", "C2": "Analog Green", "C3": "Analog Blue",
    "C4": "Analog HSync", "C5": "Analog GND",
}

# HDMI Type A (19针)
HDMI = {
    1: "TMDS Data2+", 2: "TMDS Data2 Shield", 3: "TMDS Data2-",
    4: "TMDS Data1+", 5: "TMDS Data1 Shield", 6: "TMDS Data1-",
    7: "TMDS Data0+", 8: "TMDS Data0 Shield", 9: "TMDS Data0-",
    10: "TMDS Clock+", 11: "TMDS Clock Shield", 12: "TMDS Clock-",
    13: "CEC", 14: "HEC Data-", 15: "SCL", 16: "SDA",
    17: "DDC/CEC GND", 18: "+5V Power", 19: "Hot Plug Detect",
}

# VGA DE-15
VGA = {
    1: "RED", 2: "GREEN", 3: "BLUE", 4: "RSVD", 5: "GND",
    6: "RED GND", 7: "GREEN GND", 8: "BLUE GND", 9: "+5V", 10: "Sync GND",
    11: "RSVD", 12: "SDA", 13: "HSync", 14: "VSync", 15: "SCL",
}

# USB
USB2_A = {1: "Vbus (+5V)", 2: "D-", 3: "D+", 4: "GND"}
USB_MINI_B = {1: "Vbus", 2: "D-", 3: "D+", 4: "GND", 5: "ID"}
USB3_A = {
    1: "Vbus", 2: "D-", 3: "D+", 4: "GND", 5: "StdA_SSRX-",
    6: "StdA_SSRX+", 7: "GND_DRAIN", 8: "StdA_SSTX-", 9: "StdA_SSTX+",
}
USB3_TYPEC = {
    "A1": "GND", "A2": "TX1+", "A3": "TX1-", "A4": "VBUS", "A5": "CC1",
    "A6": "D+", "A7": "D-", "A8": "SBU1", "A9": "VBUS", "A10": "RX2-",
    "A11": "RX2+", "A12": "GND", "B1": "GND", "B2": "TX2+", "B3": "TX2-",
    "B4": "VBUS", "B5": "CC2", "B6": "D+", "B7": "D-", "B8": "SBU2",
    "B9": "VBUS", "B10": "RX1-", "B11": "RX1+", "B12": "GND",
}

# SD 卡
SD_SD_MODE = {1: "CS/DAT3", 2: "CMD", 3: "VDD", 4: "VSS1", 5: "CLK", 6: "VSS2", 7: "DAT0", 8: "DAT1", 9: "DAT2"}
SD_SPI_MODE = {1: "CS", 2: "DI", 3: "VDD", 4: "VSS", 5: "SCLK", 6: "VSS", 7: "DO", 8: "RSV", 9: "RSV"}

# SIM 卡 ISO 7816
SIM = {1: "VCC", 2: "RST", 3: "CLK", 4: "VSS", 5: "RST (备用)", 6: "VPP", 7: "IO", 8: "GND"}

# 16x2 LCD HD44780
LCD1602 = {
    1: "VSS (GND)", 2: "VDD (+5V)", 3: "VO (对比度)", 4: "RS",
    5: "R/W", 6: "EN", 7: "DB0", 8: "DB1", 9: "DB2", 10: "DB3",
    11: "DB4", 12: "DB5", 13: "DB6", 14: "DB7", 15: "LED+", 16: "LED-",
}

# 树莓派 40-pin GPIO
RPI_GPIO = {
    1: "3.3V", 2: "5V", 3: "GPIO2 (SDA1)", 4: "5V", 5: "GPIO3 (SCL1)", 6: "GND",
    7: "GPIO4 (GPCLK0)", 8: "GPIO14 (TXD0)", 9: "GND", 10: "GPIO15 (RXD0)",
    11: "GPIO17", 12: "GPIO18 (PCM_CLK)", 13: "GPIO27", 14: "GND", 15: "GPIO22",
    16: "GPIO23", 17: "3.3V", 18: "GPIO24", 19: "GPIO10 (MOSI)", 20: "GND",
    21: "GPIO9 (MISO)", 22: "GPIO25", 23: "GPIO11 (SCLK)", 24: "GPIO8 (CE0)",
    25: "GND", 26: "GPIO7 (CE1)", 27: "ID_SD", 28: "ID_SC", 29: "GPIO5",
    30: "GND", 31: "GPIO6", 32: "GPIO12 (PWM0)", 33: "GPIO13 (PWM1)", 34: "GND",
    35: "GPIO19 (PCM_FS)", 36: "GPIO16", 37: "GPIO26", 38: "GPIO20 (PCM_DIN)",
    39: "GND", 40: "GPIO21 (PCM_DOUT)",
}

# RGB LED 4脚
RGB_LED = {1: "RED", 2: "COMMON (公共端)", 3: "BLUE", 4: "GREEN"}

# 引脚表汇总：分类 -> {名称: 引脚字典}
PINOUTS = {
    "USB": {"USB 2.0 Type-A": USB2_A, "Mini/Micro USB 2.0": USB_MINI_B, "USB 3.0 Type-A": USB3_A, "USB 3.1 Type-C": USB3_TYPEC},
    "HDMI / DVI / VGA": {"HDMI Type A": HDMI, "DVI-I": DVI, "VGA DE-15": VGA},
    "RS-232": {"DE-9 (9针)": RS232_DE9, "DB-25 (25针)": RS232_DB25},
    "RJ 系列": {"RJ-9/11/14/25": RJ, "RJ-45 (568B)": {str(k): v for k, v in RJ45_568B.items()}, "PoE Mode A": {str(k): v for k, v in POE_MODE_A.items()}, "PoE Mode B": {str(k): v for k, v in POE_MODE_B.items()}},
    "FireWire IEEE1394": FIREWIRE,
    "SCART": {"SCART 21针": SCART},
    "SD / SIM": {"SD卡 (SD模式)": SD_SD_MODE, "SD卡 (SPI模式)": SD_SPI_MODE, "SIM卡 ISO7816": SIM},
    "LCD / LED": {"16x2 LCD HD44780": LCD1602, "RGB LED 4脚": RGB_LED},
    "树莓派 GPIO": {"40针 GPIO": RPI_GPIO},
}
