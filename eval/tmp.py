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

def dictionary_updater(cnt_dict, critia) -> None:
    try:
        cnt_dict[critia] += 1
    except:
        cnt_dict[critia] = 0

def main():
    a = [1,2,3,4,5,6,7,8,9,10]

    tmp = [i for i in a if i > 5]
    print(tmp)

if __name__ == '__main__':
    main()