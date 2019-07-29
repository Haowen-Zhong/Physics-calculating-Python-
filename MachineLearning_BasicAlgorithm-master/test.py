#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: test.py
@time: 2019/4/4 20:58
"""

import numpy as np
if __name__ == '__main__':
    a = np.arange(27)
    print(a)
    print(a.reshape(3,3,3))
    print(a.transpose(0,1,2))