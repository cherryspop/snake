# 6.1
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []

for i in mac:
  mac_cisco.append(i.replace(':','.').upper())

print(mac_cisco)

# 6.2
ipa = input().split('.')

if int(ipa[0]) in range(1,223):
  print('unicast')

elif int(ipa[0]) in range(224,239):
  print('multicast')

elif '.'.join(ipa) in '255.255.255.255':
  print('local broadcast')

elif '.'.join(ipa) in '0.0.0.0':
  print('unssigned')

else:
  print('unused')