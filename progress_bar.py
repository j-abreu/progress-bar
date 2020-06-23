# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:01:20 2020

@author: Jeremias Abreu
Email: jeremias10j@gmail.com
Github: j-abreu
"""
from time import time
from numpy import mean
from os import system
from time import sleep
class ProgressBar:
    
    def __init__(self, total_data_len, title='', percentage=True, total_bar_len=40, symbol='-',
                 style='simple'):
        self.data_len = total_data_len
        self.title = title
        self.percentage = percentage
        self.bar_len = total_bar_len
        self.symbol = symbol
        self.time_interval = [0,0]
        self.times = []
        self.switcher = True
        self.style = style
    
    def __call__(self, done, style=None):
        if style is None:
            if self.style is 'simple':
                self.simple_bar(done)
            elif self.style is 'with_time':
                self.bar_w_time(done)
        else:
            if style is 'simple':
                self.simple_bar(done)
            elif style is 'with_time':
                self.bar_w_time(done)
            else:
                self.simple_bar(done)
    
    def simple_bar(self, done):
        cur_bar_len = int(done/self.data_len*self.bar_len)
        cur_percentage = done/self.data_len*100
        print('\r%s' % (' '*100), end='')
        print('\r' + self.title + ' [%d/%d] [%s%s] %0.2f%% complete ' % (done, self.data_len,
                                                          self.symbol*cur_bar_len,
                                                          ' '*(self.bar_len-cur_bar_len),
                                                          cur_percentage), end='')
        if cur_percentage == 100.0:
            print('Done!')
            
    def bar_w_time(self, done):
        if self.switcher:
            self.possible_total_calls = self.data_len/done
            self.first_time = time()
            self.time_interval[1] = self.first_time
            self.switcher = False
        self.time_interval[0] = self.time_interval[1]
        self.time_interval[1] = time()
        self.times.append(self.time_interval[1] - self.time_interval[0])
        time_mean = mean(self.times[-20:])
        
        elapsed_mins = int((self.time_interval[1] - self.first_time)/60.0)
        elapsed_secs = (self.time_interval[1] - self.first_time)%60
        
        remaining_mins = int(time_mean*max(self.possible_total_calls, 0)/60.0)
        remaining_secs = time_mean*max(self.possible_total_calls, 0)%60.0
        
        self.possible_total_calls -= 1.0
        
        cur_bar_len = int(done/self.data_len*self.bar_len)
        cur_percentage = done/self.data_len*100
        
        system('cls||clear')
        print(self.title + ' [%d/%d] [%s%s] %0.2f%% complete ' % (done, self.data_len,
                                                                  self.symbol*cur_bar_len,
                                                                  ' '*(self.bar_len-cur_bar_len),
                                                                  cur_percentage))
            
        print('elapsed time: %dmin %.2fs\t expected remaining time: %dmin %.2fs' % (elapsed_mins,
                                                                                   elapsed_secs,
                                                                                   remaining_mins,
                                                                                   remaining_secs))
        if cur_percentage == 100.0:
            print('Done!')
            self = self.__init__(self.data_len, self.title, self.percentage, self.bar_len,
                                 self.symbol, self.style)











        