import numpy as np

import sys, os
print(os.path.realpath('../../../../../datascience'))
sys.path.append( os.path.realpath('.'))
sys.path.append( os.path.realpath('../../../../..') + '/datascience' )
#sys.path.append( '/Users/amylarson/Documents/__Coding/REU/__data8/datascience/datascience/')
from datascience import *

pop = Table.read_table("world_population.csv").column("Population")
years = np.arange(1950, 2015+1)
print("Population:", pop)
print("Years:", years)

