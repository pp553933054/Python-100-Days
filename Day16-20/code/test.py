#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-08-28 8:08 
# @Author : YXH
# @Site :  
# @File : test.py 
# @Software: PyCharm

from hello_closure import foo

bar = "Hi!"

# 以下三次 foo 函数调用属于同一个闭包实例
print("1. test module bar: %s" % bar)
foo()
print("2. test module bar: %s" % bar)
foo()
print("3. test module bar: %s" % bar)
foo()
