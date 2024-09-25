#!/usr/bin/env python3

from os.path import isfile, join, exists
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np


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

    # Convert to numpy array for DBSCAN
    X = np.array(X)

    # DBSCAN clustering
    dbscan = DBSCAN(eps=0.001, min_samples=5)
    labels = dbscan.fit_predict(X)

    # Extract core samples (centroids for DBSCAN are not directly available)
    core_samples_mask = np.zeros_like(labels, dtype=bool)
    core_samples_mask[dbscan.core_sample_indices_] = True
    unique_labels = set(labels)

    # Calculate average error
    print(f'average error: translation: {sum(translation_error_list)/len(translation_error_list)}, rotation: {sum(rotation_error_list)/len(rotation_error_list)}')

    # Plot errors
    plt.scatter(rotation_error_list, translation_error_list, alpha=0.01)

    # Plot DBSCAN core samples as centroids (just for visualization)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = 'k'  # Black used for noise
        class_member_mask = (labels == k)
        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 1], xy[:, 0], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)

    plt.axis('scaled')
    plt.show()


if __name__ == '__main__':
    main()
