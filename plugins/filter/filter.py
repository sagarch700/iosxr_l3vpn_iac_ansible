#!/usr/bin/env python

'''
This module provides custom filters for Ansible playbooks.

It includes the following filters:
- rd_max: Parses RD values and returns the maximum RD value.
- rt_max: Parses RT values and returns the greatest RT value.
- bgp_password: Generates a strong random password and returns the password
'''

import re
import heapq
import random
class FilterModule:
    '''
    Defines a Filter module object.
    '''
    @staticmethod
    def filters():
        '''
        Return a int values where key is the filter
        '''
        return {
            'rd_max' : FilterModule.rd_max,
            'rt_max' : FilterModule.rt_max,
            'bgp_password' : FilterModule.bgp_password
        }

    @staticmethod
    def rd_max(text):
        '''
        Parses the rd value text into list of rd values and returns max rd value using heap dsa.
        '''
        rd_values = re.findall(r'(?<=:)\d+', text)
        rd_values_neg = [-int(val) for val in rd_values]
        heapq.heapify(rd_values_neg)
        rd_max_val = abs(heapq.heappop(rd_values_neg))
        return rd_max_val

    @staticmethod
    def rt_max(text):
        '''
        Parses the rt values and return the last greatest rt value configured on iosxr device.
        '''
        val = re.findall(r'(?:\d+):(\d+)', text)
        return int(val[0])

    @staticmethod
    def bgp_password(value=None):
        '''
        Creates a strong BGP password and returns the same
        '''
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        pass_letters = 4
        pass_symbols = 2
        pass_numbers = 2
        pwd_list = []
        pwd = ""

        for _ in range(0, pass_letters):
            pwd_list.append(random.choice(letters))

        for _ in range(0, pass_numbers):
            pwd_list.append(random.choice(numbers))

        for _ in range(0, pass_symbols):
            pwd_list.append(random.choice(symbols))

        random.shuffle(pwd_list)
        for char in pwd_list:
            pwd += char
        return pwd
