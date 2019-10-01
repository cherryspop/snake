# from sys import argv
# ip = argv[1]
ip = input()
prefix = int(ip[-2:].replace('/',''))
once = '{:<032}'.format(int(prefix*'1'))
mask1 = '{:08}'.format(int(once[:8]))
mask2 = '{:08}'.format(int(once[8:16]))
mask3 = '{:08}'.format(int(once[16:24]))
mask4 = '{:08}'.format(int(once[24:]))
print('''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{4:08b} {5:08b} {6:08b} {7:08b}

Mask:
{8:}
{9:<8} {10:<8} {11:<8} {12:<8}
{13:<08} {14:<08} {15:<08} {16:<08}
'''.format(ip.split('.')[0],
           ip.split('.')[1],
           ip.split('.')[2],
           0,
           int(ip.split('.')[0]),
           int(ip.split('.')[1]),
           int(ip.split('.')[2]),
           0,
           '/'+str(prefix),
           int(once[:8],2),
           int(once[8:16],2),
           int(once[16:24],2),
           int(once[24:32],2),
           int(once[:8]),
           int(once[8:16]),
           int(once[16:24]),
           int(once[24:32])))
