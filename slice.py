# -*- coding: utf-8 -*-
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    k=len(s)

    if s[0] == ' ' and s[k-1] == ' ':
        print s[1:k-1]
    else:
        print "nothing"

x=' hello '
print trim(x)
