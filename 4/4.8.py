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