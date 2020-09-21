#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:03:12 2020

@author: vishalr
"""
import treecompare

def calc_fpfn(method,data):

    fnfp = []
    fn = 0
    fp = 0
    for i in range(20):
        fnfp.append(treecompare.compareTreesFromPath('/home/vishalr/Downloads/hw3agb/1000M'+str(data)+'/R'+str(i)+'/rose.tt','/home/vishalr/Downloads/hw3agb/1000M'+str(data)+'/R'+str(i)+'/'+method))
        #print(fnfp[i][3:5])
        
    for i in range(20):
        fn = fn + fnfp[i][4]
        fp = fp + fnfp[i][3]
        
    return(fp/20,fn/20)
    
print(calc_fpfn('FastTree_JC',1))
print(calc_fpfn('FastTree_GTR',1))
print(calc_fpfn('FastTree_JC',4))
print(calc_fpfn('FastTree_GTR',4))
print(calc_fpfn('FastME_pdist',1))
print(calc_fpfn('FastME_JC69',1))
print(calc_fpfn('FastME_logdet',1))
print(calc_fpfn('FastME_pdist',4))
print(calc_fpfn('FastME_JC69',4))
print(calc_fpfn('FastME_logdet',4))