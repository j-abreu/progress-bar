# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:01:20 2020

@author: Jeremias Abreu
Email: jeremias10j@gmail.com
Github: j-abreu
"""


def progress_bar(done, total, title='copying...', percentage=True, bar_total_len=40, symbol='-'):
    bar_len = int(done/total*bar_total_len)
    perc = done/total*100
    print('\r%s' % (' '*50), end='')
    print('\r'+title + ' [%s%s] %0.2f%%' % (symbol*bar_len, ' '*(bar_total_len-bar_len), perc), end='')
    if done == total:
        print(' Done!')