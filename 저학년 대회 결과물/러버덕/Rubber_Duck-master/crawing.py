import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from os.path import join

print("pandas version: ", pd.__version__)
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

Data = pd.read_csv('./csv/player_of_month.csv', parse_dates=False, encoding='mac_roman')
Data = Data.dropna(axis=0)
Month = [Data.loc[Data["Month"] == i, ["Name", "Player"]].sort_values("Player", ascending=False).head(5).reset_index(
    drop=True) for i in range(1, 12 + 1)]

for i in range(12):
    print("------------------------------------------------------")
    print(i+1)
    print(Month[i])
Counter_Strike = []
for i in range(12):
    value = Month[i].loc[Month[i]["Name"] == "Counter-Strike: Global Offensive", "Player"].values[0]
    if value:
        Counter_Strike.append(value)
Counter_Strike = np.array(Counter_Strike)

Dota = []
for i in range(12):
    value = Month[i].loc[Month[i]["Name"] == "Dota 2", "Player"].values[0]
    if value:
        Dota.append(value)
Dota = np.array(Dota)

BATTLEGROUNDS = []
for i in range(12):
    value = Month[i].loc[Month[i]["Name"] == "PLAYERUNKNOWN'S BATTLEGROUNDS", "Player"].values[0]
    if value:
        BATTLEGROUNDS.append(value)
BATTLEGROUNDS = np.array(BATTLEGROUNDS)

MONSTER = []  # 3(0,1,2)
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Monster Hunter: World", "Player"].values[0]
        if value:
            MONSTER.append(value)
    except IndexError:
        MONSTER.append(0)
        continue
MONSTER = np.array(MONSTER)

GTA5 = []
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Grand Theft Auto V", "Player"].values[0]
        if value:
            GTA5.append(value)
    except IndexError:
        GTA5.append(0)
        continue
GTA5 = np.array(GTA5)

RAINBOW = []  # 10(1,2,3,4,5,6,7,8,9,10)
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Tom Clancy's Rainbow Six Siege", "Player"].values[0]
        if value:
            RAINBOW.append(value)
    except IndexError:
        RAINBOW.append(0)
        continue
RAINBOW = np.array(RAINBOW)

TERRARIA = []  # 2(56있음)
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Terraria", "Player"].values[0]
        if value:
            TERRARIA.append(value)
    except IndexError:
        TERRARIA.append(0)
        continue
TERRARIA = np.array(TERRARIA)

FALL = []  # 2(8,9있음)
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Fall Guys: Ultimate Knockout", "Player"].values[0]
        if value:
            FALL.append(value)
    except IndexError:
        FALL.append(0)
        continue
FALL = np.array(FALL)

TF2 = []
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Team Fortress 2", "Player"].values[0]
        if value:
            TF2.append(value)
    except IndexError:
        TF2.append(0)
        continue
TF2 = np.array(TF2)

DESTINY2 = []  # 10(5월 9월 없음)
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Destiny 2", "Player"].values[0]
        if value:
            DESTINY2.append(value)
    except IndexError:
        DESTINY2.append(0)
        continue
DESTINY2 = np.array(DESTINY2)

AMONGUS = []  # 4(9,10,11,12있음)
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Among Us", "Player"].values[0]
        if value:
            AMONGUS.append(value)
    except IndexError:
        AMONGUS.append(0)
        continue
AMONGUS = np.array(AMONGUS)

CYBERPUNK = []  # 1(12있음)
for i in range(12):
    try:
        value = Month[i].loc[Month[i]["Name"] == "Cyberpunk 2077", "Player"].values[0]
        if value:
            CYBERPUNK.append(value)
    except IndexError:
        CYBERPUNK.append(0)
        continue
# CYBERPUNK = np.array(CYBERPUNK)

plt.figure(figsize=(14, 10))
x = [_ for _ in range(1, 12 + 1)]
marker_size = 5
plt.plot(x, Counter_Strike, marker='o', color='#ccba7c', linewidth=3, label="CSGO", markersize=marker_size)
plt.plot(x, Dota, marker='o', color='#e44326', linewidth=3, label="DOTA2", markersize=marker_size)
plt.plot(x, BATTLEGROUNDS, marker='o', color='#ffde40', linewidth=3, label="PUBG", markersize=marker_size)
plt.plot(x, CYBERPUNK, 'yo', label="CYBERPUNK", markersize=marker_size)
plt.plot(x, AMONGUS, 'o', color='#3f464e', label="AMONG US", markersize=marker_size)
plt.plot(x, GTA5, 'o', color='#47761e', label="GTA5", markersize=marker_size)
plt.plot(x, TF2, 'o', color='#5899c9', label="TF2", markersize=marker_size)
plt.plot(x, FALL, 'o', color='#fe2fa3', label="FALL GUYS", markersize=marker_size)
plt.plot(x, DESTINY2, 'o', color='#461044', label="DESTINY2", markersize=marker_size)
plt.plot(x, RAINBOW, 'o', color='#4e606e', label="RAINBOW SIX", markersize=marker_size)
plt.plot(x, TERRARIA, 'o', color='#5c508d', label="TERRARIA", markersize=marker_size)
plt.plot(x, MONSTER, 'o', color='#af9483', label="MONSTER HUNTER", markersize=marker_size)
plt.plot(x, [0 for _ in range(12)], 'o', color='w', markersize=10)

plt.legend()
plt.xlabel('Month')
plt.xticks([_ for _ in range(1, 12 + 1)])
plt.ylabel('Number of Player')
plt.yticks(range(0, 1000000, 100000))
plt.title('Top 5 games of 2020', fontsize=20)
plt.show()
