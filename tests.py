# 4.1
NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT.replace('Fast', 'Gigabit'))

# 4.2
mac = 'AAAA:BBBB:CCCC'
print(mac.replace(':','.'))

# 4.3
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print((config.split()[-1].split(',')))

# 4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(list(set(vlans))))

# 4.5
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
print(sorted(list(set((command1.split()[-1].split(',')))&set((command2.split()[-1].split(','))))))

# 4.6
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

# 4.7
mac = 'AAAA:BBBB:CCCC'
print('{:08b}'.format(int(mac.replace(':',''),16)))

# 4.8
ip = '192.168.3.1'
print('''
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}'''.format(ip.split('.')[0],
                                      ip.split('.')[1],
                                      ip.split('.')[2],
                                      ip.split('.')[3],
                                      int(ip.split('.')[0]),
                                      int(ip.split('.')[1]),
                                      int(ip.split('.')[2]),
                                      int(ip.split('.')[3]),))

# 5.1 (a,c,d)
london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
print(london_co.get(input('Введите имя устройства: ')).get(input('Введите имя параметра: ').lower(),'Такого параметра нет'))

# 5.1 (b - working on it)
# x = london_co.get(input('Введите имя устройства: '))
# print(x.get(input('Введите имя параметра (' + str(list(x.keys())).strip('()[]').replace("'",'') +'): ').lower(),'Такого параметра нет'))