# -*- coding: utf-8 -*-
import numpy as np
from sympy import *

p1 = {'c1': 1, 'c3': 3}
p2 = {'c3': 3, 'c2': 2}

p_all = [p1,p2]

def model_components (processes):
    comps_unsorted = []
    for process in processes:
        comps_unsorted = comps_unsorted + list(process.keys())
    comps_sorted = sorted(list(set(comps_unsorted)))
    return (comps_sorted)

compos = model_components (p_all)
print (compos)

def gujer_stoch_builder (processes):
    components = model_components (processes)
    gujer_stoch = np.zeros((len(processes),len(components)))
    j = 0
    for process in processes:
        i = 0
        for comp_i in components:
            for proc_comp in process:
                if comp_i == proc_comp:
                    gujer_stoch [(j,i)] = process[proc_comp]
            i = i + 1
        j = j + 1
    return (gujer_stoch)

stoch = gujer_stoch_builder (p_all)
print (stoch)