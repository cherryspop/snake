table = []
counter = 0
with open('7/CAM_table.txt', 'r') as f:
  for line in f:
    if line == '\n':
      continue
    if list(line.strip().split())[0].isdigit() == True:
      counter += 1
      vlan, mac, _, port = line.split()
      table.append([vlan,mac,port])

# bubble
  for i in range(counter-1):
    for j in range(counter-i-1):
      if int(table[j][0]) > int(table[j+1][0]):
        table[j], table[j+1] = table[j+1], table[j]

  for item in table:
    vlan, mac, port = item
    print(f'  {vlan:5} {mac:15} {port}')