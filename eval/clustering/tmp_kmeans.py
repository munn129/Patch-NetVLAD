#!/usr/bin/env python3

from os.path import isfile, join, exists
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


'''
TODO
- average error:
    - translation
    - rotation
- recall rate:
    - translation: 0.25, 0.5, 1, 5, 10
    - rotation: 1, 2, 5, 10
    - both: ?
- Pearson correlation coefficient...?
'''

def dictionary_updater(cnt_dict, critia) -> None:
    try:
        cnt_dict[critia] += 1
    except:
        cnt_dict[critia] = 1

def main():
    condition = 'concat'
    vlad = 'patch'

    # both lists must have same length
    t_err_check_list = [0.25, 0.5, 5]
    r_err_check_list = [2, 5, 10]
    if len(t_err_check_list) != len(r_err_check_list):
        raise Exception('check lists are not same length')

    folder = f'oxford_{condition}'
    file = f'{vlad}_error.txt'
    error_result_dir = os.path.join(folder, file)

    translation_error_list = []
    rotation_error_list = []

    cnt_dict = {}

    with open(error_result_dir, 'r') as file:
        for line in file:
            if line[0] == '#': continue

            line = line.split('\n')[0]
            line = line.split(' ')

            translation_error = float(line[0])
            rotation_error = float(line[1])
            
            translation_error_list.append(translation_error)
            rotation_error_list.append(rotation_error)

            # recall(only translation error)
            for i in t_err_check_list:
                if translation_error < float(i):
                    dictionary_updater(cnt_dict, f'{str(i)}_m')

            # recall(only rotation error)
            for i in r_err_check_list:
                if rotation_error < float(i):
                    dictionary_updater(cnt_dict, f'{str(i)}_degree')

            # recall(translation and rotation error)
            for t, r in zip(t_err_check_list, r_err_check_list):
                if translation_error < float(t) and rotation_error < float(r):
                    dictionary_updater(cnt_dict, f'{str(t)}_m_and_{str(r)}_degree')

    print(f'########## Result of {error_result_dir} ##########')
    for i in cnt_dict:
        print(f'recall rate @ {i}: {cnt_dict[i]/len(translation_error_list) *100} %')

    # plot tendency

    X = []
    for t, r in zip(translation_error_list, rotation_error_list):
        X.append([t, r])

    # k-means clustering
    k_means = KMeans(n_clusters = 3,
                     init = 'random')
    k_means.fit_predict(X)

    print(f'k_means centroid: translation: {k_means.cluster_centers_[:,0]}, rotation: {k_means.cluster_centers_[:,1]}')
    print(f'average error: translation: {sum(translation_error_list)/len(translation_error_list)}, rotation: {sum(rotation_error_list)/len(rotation_error_list)}')

    # plot errors
    plt.scatter(rotation_error_list, translation_error_list, alpha=0.01)

    # plot centroid
    plt.scatter(k_means.cluster_centers_[:, 0],
                k_means.cluster_centers_[:,1],
                marker = '*')

    plt.axis('scaled')
    plt.show()


if __name__ == '__main__':
    main()