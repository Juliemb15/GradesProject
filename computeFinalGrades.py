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

