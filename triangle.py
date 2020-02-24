# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: Tiancheng
"""

def classify_triangle(line_a, line_b, line_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(line_a, int) and isinstance(line_b, int) and isinstance(line_c, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if line_a > 200 or line_b > 200 or line_c > 200:
        return 'InvalidInput'

    if line_a <= 0 or line_b <= 0 or line_c <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (line_a <= abs(line_b - line_c))\
        or (line_b <= abs(line_a - line_c))\
        or (line_c < abs(line_a - line_b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if line_a == line_b and line_b == line_c and line_a == line_c:
        output = 'Equilateral'
    elif ((line_a**2) + (line_b**2)) == (line_c**2)\
        or ((line_a**2) + (line_c**2)) == (line_b**2)\
        or ((line_c**2) + (line_b**2)) == (line_a**2):
        output = 'Right'
    elif (line_a != line_b) and  (line_b != line_c) and (line_a != line_c):
        output = 'Scalene'
    else:
        output = 'Isoceles'
    return output
