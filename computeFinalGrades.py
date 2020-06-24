
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Lavet af Julie s184515
"""

def roundGrade(grades):
    for i in range(len(grades)):
        if grades[i] >= -3 and grades[i] < -1.5:
            grades[i] = -3
        elif grades[i] >= -1.5 and grades[i] < 1:
            grades[i] = 00
        elif grades[i] >= 1 and grades[i] < 3:
            grades[i] = 2
        elif grades[i] >= 3 and grades[i] < 5.5:
            grades[i] = 4
        elif grades[i] >= 5.5 and grades[i] < 8.5:
            grades[i] = 7
        elif grades[i] >= 8.5 and grades[i] < 11:
            grades[i] = 10
        elif grades[i] >= 11 and grades[i] <= 12:
            grades[i] = 12
    gradesRounded = grades
    return gradesRounded




# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 23:13:48 2020

@author: Peter
"""

import numpy as np

def computeFinalGrades(grades):
    
    #sorting grades, so first value of array is the lowest value
    grades = np.sort(grades)
    
    #determining amount of graded assignments
    sizeofGrades = len(grades)
    
    #setting automatic failcheck
    fail = np.array([-3])
    
    #Checking if student failed
    if fail in grades:
        gradesFinal = fail
    #Finding the final grade if two or more assignments have been graded
    #Dropping the first value which was sorted to be lowest grade
    elif sizeofGrades >= 2:
        gradesFinal = np.delete(grades, 0)
        ##replace np.mean with roundGrades function?##
        gradesFinal = np.mean(gradesFinal)
    #Setting final grade if one assignments have been grades    
    elif sizeofGrades == 1:
        gradesFinal = grades
    return gradesFinal

