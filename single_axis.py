#!/usr/bin/env python

'''
 ' Single Axis
'''

import os
from farmware_tools import device
from farmware_tools import app
from farmware_tools import get_config_value

x=y=z=0
axis = 'X'#get_config_value('Single Axis', 'axis')
pos = -5#get_config_value('Single Axis', 'pos')
log = 'Axis: {}, Position: {}'.format(axis, pos)
device.log(log, 'info', ['toast'])
