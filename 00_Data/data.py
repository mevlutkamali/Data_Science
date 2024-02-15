# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Coding.
source = pd.read_csv('source.csv')
print(source)

# Data preprocessing.
size = source[['boy']]
print(size)


print("\n Finish. . .")
