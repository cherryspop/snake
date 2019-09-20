from sys import argv
ip = argv[1]
print('''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{4:08b} {5:08b} {6:08b} {7:08b}

Mask:
{8:}
{9:<8} {10:<8} {11:<8} {12:<8}
{13:08b} {14:08b} {15:08b} {16:08b}
'''.format(argv[1].split('.')[0],
           argv[1].split('.')[1],
           argv[1].split('.')[2],
           argv[1].replace('/','.').split('.')[3],
           int(argv[1].split('.')[0]),
           int(argv[1].split('.')[1]),
           int(argv[1].split('.')[2]),
           int(argv[1].replace('/','.').split('.')[3]),
           argv[1][-3:],
           argv[1].split('.')[0],
           argv[1].split('.')[1],
           argv[1].split('.')[2],
           argv[1].replace('/','.').split('.')[3],
           int(argv[1].split('.')[0]),
           int(argv[1].split('.')[1]),
           int(argv[1].split('.')[2]),
           int(argv[1].replace('/','.').split('.')[3])))

prefix = int(input())
once = prefix*'1'