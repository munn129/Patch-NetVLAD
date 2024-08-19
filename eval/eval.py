#!/usr/bin/env python3

from os.path import isfile, join, exists
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Result:
    def __init__(self, result_path: str, patch = True) -> None:

        if not exists(result_path):
            raise Exception(f'{result_path} is not exists.')

        if patch:
            self.result_path = join(result_path, 'PatchNetVLAD_predictions.txt')
        else:
            self.result_path = join(result_path, 'NetVLAD_predictions.txt')

        if not isfile(self.result_path):
            raise FileNotFoundError(f'{result_path} is not exists.')  
        
        self.query_list = []
        self.retrieved_list = []
        self.retrieval_num = 0
        self._read_result()

    def _read_result(self) -> None:
        with open(self.result_path, 'r') as file:
            for line in file:
                if line[0] == '#': continue
                
                line = line.split('\n')[0]
                line = line.split(', ')
                self.query_list.append(line[0][1:].split('/')[-1])
                self.retrieved_list.append(line[1][1:].split('/')[-1])

        tmp_query_list = []
        
        for i in self.query_list:
            if i not in tmp_query_list:
                tmp_query_list.append(i)

        self.retrieval_num = int(len(self.query_list) / len(tmp_query_list))
        self.query_list = tmp_query_list[:]
    
    def get_query_list(self) -> list:
        return self.query_list
    
    def get_retrieved_list(self) -> list:
        return self.retrieved_list
    
    def get_retrieval_num(self) -> int:
        return self.retrieval_num


class GeoTagImage:
    def __init__(self, image_name: str, latitude: float, longitude: float, heading: float) -> None:
        self.image_name = image_name
        self.latitude = latitude
        self.longitude = longitude
        self.heading = heading
    
    def get_image_name(self) -> str:
        return self.image_name
    
    def get_latitude(self) -> float:
        return self.latitude
    
    def get_longitude(self) -> float:
        return self.longitude
    
    def get_heading(self) -> float:
        return self.heading


class GPS:
    def __init__(self, gps_path: str) -> None:
        if not isfile(gps_path):
            raise FileNotFoundError(f'{gps_path} is not exist.')
        
        self.gps_path = gps_path
        self.geo_tag_image_list = []
        self._read_gps()

    def _read_gps(self) -> None:
        with open(self.gps_path, 'r') as file:
            for line in file:
                line = line.split(' ')
                image_name = line[0].split('/')[-1]
                latitude = float(line[1])
                longitude = float(line[2])
                heading = float(line[3])
                self.geo_tag_image_list.append(GeoTagImage(image_name, latitude, longitude, heading))
    
    def get_geo_tag_image_list(self) -> list:
        return self.geo_tag_image_list
    
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

class Evaluation:
    def __init__(self, result: Result, query: GPS, db: GPS, is_save = False) -> None:
        self.result = result
        self.query = query
        self.db = db
        self.is_save = is_save
        
        self._db_list = []
        self._db_filtering()

        self.db_name_list = []
        self.query_name_list = []

    def _db_filtering(self) -> None:
        
        for i in range(len(self.result.get_query_list())):
           self._db_list.append(self.result.get_retrieved_list()[i * self.result.get_retrieval_num()])

    def _filtering(self) -> None:
        
        q_name_list_all = []
        for i in self.query.get_geo_tag_image_list():
            q_name_list_all.append(i.get_image_name())

        for i in self.result.get_query_list:
            if i in q_name_list_all:
                self.query_list.append(i)


            
def main() -> None:

    dataset = 'kiapi'

    result = Result(dataset)
    query = GPS(join(dataset, 'q.txt'))
    db = GPS(join(dataset, 'd.txt'))
    eval = Evaluation(result, query, db)

    print(eval._db_list)

if __name__ == '__main__':
    main()