import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Assuming the data is in a CSV file named "stations.csv"
df = pd.read_csv("data/output_file.csv")
font_path = "/home/Amir/Desktop/Cairo/static/Cairo-Bold.ttf"  # Replace with the actual path to your font file

# Add the font to Matplotlib's font manager
font_manager.fontManager.addfont(font_path)
# Set the default font for Matplotlib
plt.rcParams["font.family"] = "Cairo"  # Replace with the name of your font

# Basic exploration
# print(df.head())
# print(df.describe())

# Group by administrative jurisdiction and calculate total discharge
grouped = df.groupby("اسم الإدارة")["اجمالي االتصرف الشهري"].sum()

# print(grouped)

import matplotlib.pyplot as plt
from matplotlib import font_manager
import arabic_reshaper
from bidi.algorithm import get_display

# تسجيل الخط العربي
font_path = "/content/Amiri-Regular.ttf"  # قم بتغيير المسار إذا لزم الأمر
font_manager.fontManager.addfont(font_path)
plt.rcParams["font.family"] = "Amiri"

# تهيئة النص العربي وعرض المخطط
grouped = df.groupby("اسم الإدارة")["اجمالي االتصرف الشهري"].sum()
grouped.plot(kind="bar")
plt.title(get_display(arabic_reshaper.reshape("إجمالي التصريف الشهري لكل إدارة")))
plt.xlabel(get_display(arabic_reshaper.reshape("اسم الإدارة")))
plt.ylabel(get_display(arabic_reshaper.reshape("إجمالي التصريف الشهري")))
plt.xticks(rotation=45)  # تدوير أسماء الإدارات لقراءة أفضل
plt.show()
