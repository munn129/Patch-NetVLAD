#!/usr/bin/env python3

from os.path import isfile, join, exists
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt

def main():
    direction = ['concat', 'front']
    method = ['patch', 'netvlad']

    error_list_dic = {}

    for direc in direction:
        for mthd in method:
            translation_list = []
            rotation_list = []

            with open(f'oxford_{direc}/{mthd}_error.txt') as file:
                for line in file:
                    if line[0] == '#': continue

                    line = line.split('\n')[0]
                    line = line.split(' ')

                    translation_list.append(float(line[0]))
                    rotation_list.append(float(line[1]))

            error_list_dic[f'{direc}_{mthd}_translation'] = translation_list
            error_list_dic[f'{direc}_{mthd}_rotation'] = rotation_list

    for direc in direction:
        for mthd in method:

            plt.hist(error_list_dic[f'{direc}_{mthd}_translation'],
                     bins = 200,
                     alpha = 0.1,
                     label = f'{direc}_{mthd}',
                     range = (0, 50)
                     )
    

    plt.show()

    for direc in direction:
        for mthd in method:

            plt.hist(error_list_dic[f'{direc}_{mthd}_rotation'],
                     bins = 200,
                     alpha = 0.1,
                     label = f'{direc}_{mthd}',
                     range = (0, 10)
                     )
    

    plt.show()


if __name__ == '__main__':
    main()