import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import folium

direction = 'concat'
method = 'patch'

gps_1 = f'../oxford_{direction}/0519_{direction}_gt.txt'
gps_2 = f'../oxford_{direction}/0828_{direction}_gt.txt'
error = f'../oxford_{direction}/{method}_error.txt'

gps_1_list = []
gps_2_list = []
error_list = []
# len(gps_1_list) == len(error_list)

with open(gps_1, 'r') as file:
    for line in file:
        line = line.split(' ')
        gps_1_list.append((line[1], line[2]))  # (lon, lat)

with open(gps_2, 'r') as file:
    for line in file:
        line = line.split(' ')
        gps_2_list.append((line[1], line[2]))  # (lon, lat)

with open(error, 'r') as file:
    for line in file:
        if line.split(' ')[0] == '#': continue
        error_list.append(float(line.split(' ')[0]))

# 지도 생성
m = folium.Map(location=[51.757, -1.263], zoom_start=15, tiles="CartoDB positron")

# 포인트 추가 (gps_1_list는 빨간 원, gps_2_list는 파란 원)

for coord in gps_2_list:
    folium.CircleMarker(
        location=coord,
        radius=0.5,
        stroke = False,
        color='blue',
        fill=True,
        fill_opacity=1,
        # popup=str(coord)
    ).add_to(m)

for coord in gps_1_list:
    folium.CircleMarker(
            location=coord,
            radius=0.5,
            stroke = False,
            color='red',
            fill=True,
            fill_opacity=1,
            # popup=str(coord)
        ).add_to(m)
    
for coord, err in zip(gps_1_list, error_list):

    if err > 50:
        folium.CircleMarker(
            location=coord,
            radius=1.5,
            # stroke = False,
            color='green',
            fill=False,
            fill_opacity=0.1,
            # popup=str(coord)
        ).add_to(m)

# 지도 HTML로 저장
m.save(f'{direction}_{method}_map.html')
print(f'{direction}_{method}_map.html is saved')