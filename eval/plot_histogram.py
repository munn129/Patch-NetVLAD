#!/usr/bin/env python3

from os.path import isfile, join, exists
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import lognorm

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
            
            data = error_list_dic[f'{direc}_{mthd}_translation'][error_list_dic[f'{direc}_{mthd}_translation'] < 20]

            shape, loc, scale = lognorm.fit(data, floc = 0)
            pdf = np.linspace(min(data), max(data), len(data))
            pdf_fitted = lognorm.pdf(pdf, shape, loc = loc, scale = scale)

            plt.plot(pdf, pdf_fitted, label = 'log-normal')

            plt.hist(data,
                     bins = len(data),
                     alpha = 0.1,
                     label = f'{direc}_{mthd}'
                     )
    

    plt.show()

    for direc in direction:
        for mthd in method:

            data = error_list_dic[f'{direc}_{mthd}_rotation'][error_list_dic[f'{direc}_{mthd}_rotation'] < 10]

            shape, loc, scale = lognorm.fit(data, floc = 0)
            pdf = np.linspace(min(data), max(data), len(data))
            pdf_fitted = lognorm.pdf(pdf, shape, loc = loc, scale = scale)

            plt.plot(pdf, pdf_fitted, label = 'log-normal')

            plt.hist(data,
                     bins = len(data),
                     alpha = 0.1,
                     label = f'{direc}_{mthd}',
                     range = (0, 10)
                     )
    

    plt.show()


if __name__ == '__main__':
    main()