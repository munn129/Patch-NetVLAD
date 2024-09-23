'''
calculate upper bound of translation error
'''

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from tqdm import tqdm

def gps_to_error(lat1, lon1, lat2, lon2):
    from math import pi, sin, cos, sqrt, atan2

    # 지구의 넓이 반지름
    R = 6371.0072 # radius of the earth in KM
    lat_to_deg = lat2 * pi/180 - lat1 * pi/180
    long_to_deg = lon2 * pi/180 - lon1 * pi/180

    a = sin(lat_to_deg/2)**2 + cos(lat1 * pi/180) * cos(lat2 * pi/180) * sin(long_to_deg/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    d = R * c

    return d * 1000 #meter

def main():
    
    position = 'concat'
    prefix = f'oxford_{position}'
    query_gt = os.path.join(prefix, f'0519_{position}_gt.txt')
    dataset_gt = os.path.join(prefix, f'0828_{position}_gt.txt')

    query_gps_list = []
    dataset_gps_list = []

    with open(query_gt, 'r') as file:
        for line in file:
            line = line.split('\n')[0]
            query_gps_list.append(line.split(' '))

    with open(dataset_gt, 'r') as file:
        for line in file:
            line = line.split('\n')[0]
            dataset_gps_list.append(line.split(' '))

    error = []

    
    for query in tqdm(query_gps_list):
        upper_bound = 9999
        for dataset in dataset_gps_list:
            e = gps_to_error(float(query[1]), float(query[2]), float(dataset[1]), float(dataset[2]))
            if e < upper_bound:
                upper_bound = e
        
        error.append(upper_bound)

    print(sum(error)/len(error))

    query_lat_plot_list = []
    query_lon_plot_list = []
    dataset_lat_plot_list = []
    dataset_lon_plot_list = []

    for query in query_gps_list:
        query_lat_plot_list.append(query[1])
        query_lon_plot_list.append(query[2])

    for dataset in dataset_gps_list:
        dataset_lat_plot_list.append(dataset[1])
        dataset_lon_plot_list.append(dataset[2])

    plt.scatter(query_lat_plot_list, query_lon_plot_list,s = 10, c = '#FF3213')
    plt.scatter(dataset_lat_plot_list, dataset_lon_plot_list, s = 1, c = '#123344')

    plt.axis('off')

    plt.show()

if __name__ == '__main__':
    main()