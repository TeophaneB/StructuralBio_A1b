#!/usr/bin/env python

from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, 
              alnfile='2YHH.ali',
              knowns='2YHH', 
              sequence='T1064',
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 1
a.make()
