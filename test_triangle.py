# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testInvaildTriangleA(self):
        self.assertEqual(classify_triangle(-1,0,3),'InvalidInput','-1,0,3 shoule be InvalidInput')

    def testInvaildTriangleB(self):
        self.assertEqual(classify_triangle(201,2,201),'InvalidInput','201,0,201 shoule be InvalidInput')

    def testInvaildTriangleC(self):
        self.assertEqual(classify_triangle('1',1,1),'InvalidInput',"'1',1,1 shoule be InvalidInput")
    
    def testInvaildTriangleD(self):
        self.assertEqual(classify_triangle(0.5,1,1),'InvalidInput',"0.5,1,1 shoule be InvalidInput")

    def testNotATriangleA(self):
        self.assertEqual(classify_triangle(1,1,2),'NotATriangle','1,1,2 should NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classify_triangle(1,3,2),'NotATriangle','1,3,2 should NotATriangle')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(2,3,4),'Scalene','2,3,4 should be Scalene')
    
    def testIsocelesTriangle(self):
        self.assertEqual(classify_triangle(2,2,3),'Isoceles','2,2,3 should be Isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

