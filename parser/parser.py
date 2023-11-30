import configparser

from configparser import ConfigParser, ExtendedInterpolation

config = configparser.ConfigParser()
config.read('sampleInstance.dat')

# Access values using the section and option
nOrders = config.getint('Values', 'nOrders')
nSlots = config.getint('Values', 'nSlots')
p = config.get('Values', 'p')
l = config.get('Values', 'l')
c = config.get('Values', 'c')
mindi = config.get('Values', 'mindi')
maxdi = config.get('Values', 'maxdi')
maxsur = config.getfloat('Values', 'maxsur')

# Parse string lists into actual lists
p = [float(val) for val in p.strip('[]').split(',')]
l = [int(val) for val in l.strip('[]').split(',')]
c = [float(val) for val in c.strip('[]').split(',')]
mindi = [int(val) for val in mindi.strip('[]').split(',')]
maxdi = [int(val) for val in maxdi.strip('[]').split(',')]
