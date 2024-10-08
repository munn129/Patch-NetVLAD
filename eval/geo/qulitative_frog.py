import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import folium

def gps_reader(dir, output_list):
    
    with open(dir, 'r') as file:
        for line in file:
            line = line.split(' ')
            output_list.append((line[1], line[2])) # (lat, lon)

def txt_file_reader(dir, output_list):
    
    with open(dir, 'r') as file:
        for line in file:
            l = line.split(' ')[0]
            if l == '#': continue
            output_list.append(float(l))

db_gps_dir = f'../new_ox/front/0519_front_gt.txt'
query_gps_dir = f'../new_ox/front/0828_front_gt.txt'
netvlad_error_dir = f'../new_ox/front/netvlad_error.txt'
patch_error_dir = f'../new_ox/front/patch_error.txt'
concat_error_dir = f'../new_ox/concat/patch_error.txt'

q_concat_image_names_dir = f'../new_ox/concat/0828_concat_gt.txt'

db_gps_list = []
query_gps_list = []
netvlad_error_list = []
patch_error_list = []
concat_error_list = []

q_front_image_names_list = []
q_concat_image_names_list = []

gps_reader(query_gps_dir, query_gps_list) # len: 11037
gps_reader(db_gps_dir, db_gps_list) # len: 11358
txt_file_reader(netvlad_error_dir, netvlad_error_list) # len: 11037
txt_file_reader(patch_error_dir, patch_error_list) # len: 11037
txt_file_reader(concat_error_dir, concat_error_list) # len: 11037

print(len(query_gps_list))
print(len(db_gps_list))
print(len(netvlad_error_list))
print(len(patch_error_list))
print(len(concat_error_list))

with open(query_gps_dir, 'r') as file:
    for line in file:
        q_front_image_names_list.append(line.split(' ')[0])

with open(q_concat_image_names_dir, 'r') as file:
    for line in file:
        q_concat_image_names_list.append(line.split(' ')[0])

# map init
m = folium.Map(location=[51.757, -1.263], zoom_start=15, tiles="CartoDB positron")

for coord in db_gps_list:
    folium.CircleMarker(
        location=coord,
        radius=0.5,
        stroke = False,
        color='blue',
        fill=True,
        fill_opacity=1,
        # popup=str(coord)
    ).add_to(m)

for coord in query_gps_list:
    folium.CircleMarker(
            location=coord,
            radius=0.5,
            stroke = False,
            color='red',
            fill=True,
            fill_opacity=1,
            # popup=str(coord)
        ).add_to(m)

th = 500 # 100 [m]
for gt, netvlad, patch, concat in zip(query_gps_list,
                                      netvlad_error_list,
                                      patch_error_list,
                                      concat_error_list):
    
    # # netvlad only
    # if netvlad > th and patch < th and concat < th:
    #     folium.CircleMarker(
    #         location = gt,
    #         radius = 1.5,
    #         color = 'green',
    #         fill = False,
    #         fill_opacity = 0.1,
    #         popup = str(gt)
    #     ).add_to(m)

    # # patchnetvlad only
    # if netvlad < th and patch > th and concat < th:
    #     folium.CircleMarker(
    #         location = gt,
    #         radius = 2,
    #         color = 'orange',
    #         fill = False,
    #         fill_opacity = 0.1,
    #         popup = str(gt)
    #     ).add_to(m)

    # concat only
    if netvlad < th and patch < th and concat > th:
        folium.CircleMarker(
            location = gt,
            radius = 1,
            color = 'orange',
            fill = False,
            fill_opacity = 0.1,
            popup = str(gt)
        ).add_to(m)

    # netvlad and patchnetvlad
    if netvlad > th and patch > th and concat < th:
        folium.CircleMarker(
            location = gt,
            radius = 2.5,
            color = 'green',
            fill = False,
            fill_opacity = 0.1,
            popup = str(gt)
        ).add_to(m)

m.save(f'qulitative.html')
print(f'done.')