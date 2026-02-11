#!/usr/bin/env python

from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, 
              alnfile='6F2S.ali',
              knowns='6F2S', 
              sequence='T1026',
              assess_methods=(assess.DOPE, assess.GA341))
a.starting_model = 1
a.ending_model = 1
a.make()
