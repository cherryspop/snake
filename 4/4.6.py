ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
print('''
Protocol:               {0:}SPF 
Prefix:                 {1:} 
AD/Metric:              {2:} 
Next-Hop:               {3:} 
Last update:            {4:} 
Outbound Interface:     {5:}
'''.format(ospf_route.split()[0],
           ospf_route.split()[1],
           ospf_route.split()[2].replace('[','').replace(']',''),
           ospf_route.split()[4],
           ospf_route.split()[5],
           ospf_route.split()[6]))