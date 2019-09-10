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
print(list(set(vlans)).sort())

# 4.5
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
print( list( set((command1.split()[-1].split(','))) & set((command2.split()[-1].split(','))) ).sort() )