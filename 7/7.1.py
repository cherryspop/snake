with open('7/ospf.txt', 'r') as f:
  for line in f:
    print('''
Protocol:              OSPF
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''.format(line.split()[1],
           line.split()[2].strip('[]'),
           line.split()[4].strip(','),
           line.split()[5].strip(','),
           line.split()[6]))