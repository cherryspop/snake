dec = input('Enter vlan num: ')
with open('7/CAM_table.txt', 'r') as f:
  for line in f:
    if line == '\n':
      continue
    if list(line.strip().split())[0] == dec:
      vlan, mac, _, port = line.split()
      print(f' {vlan:5} {mac:15} {port}')