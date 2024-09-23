#!/usr/bin/env python3

from os.path import isfile, join, exists
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class ErrorAnalysis:
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
    def __init__(self) -> None:
        pass