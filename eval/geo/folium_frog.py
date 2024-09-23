import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import folium
from folium.plugins import MarkerCluster

gps_1 = '../oxford_concat/0519_concat_gt.txt'
gps_2 = '../oxford_concat/0828_concat_gt.txt'

gps_1_list = []
gps_2_list = []

with open(gps_1, 'r') as file:
    for line in file:
        line = line.split(' ')
        gps_1_list.append((line[1], line[2]))  # (lon, lat)

with open(gps_2, 'r') as file:
    for line in file:
        line = line.split(' ')
        gps_2_list.append((line[1], line[2]))  # (lon, lat)

# 지도 생성
m = folium.Map(location=[51.757, -1.263], zoom_start=15, tiles="CartoDB positron")

# MarkerCluster 객체 생성

# 포인트 추가 (gps_1_list는 빨간 원, gps_2_list는 파란 원)
for coord in gps_1_list:
    folium.CircleMarker(
        location=coord,
        radius=3,
        color='red',
        fill=True,
        fill_opacity=0.6,
        # popup=str(coord)
    ).add_to(m)

for coord in gps_2_list:
    folium.CircleMarker(
        location=coord,
        radius=3,
        color='blue',
        fill=True,
        fill_opacity=0.6,
        # popup=str(coord)
    ).add_to(m)

# 지도 HTML로 저장
m.save("map.html")