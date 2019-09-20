# 6.2 (a, b)
while True:
  ipa = input('Введите IP-адрес: ')
  ip = ipa.split('.')

  if len(ip) == 4:
    for num in ip:
      if int(num) in range(256):
        pass
      else:
        print('\nВведен неправильный IP-адресс (out of range(255))')

  else:
      print('\nНеправильный IP-адрес (недостаточно элементов)')
      continue

  if int(ip[0]) in range(1, 223):
      print('unicast')
      break

  elif int(ip[0]) in range(224, 239):
      print('multicast')
      break

  elif '.'.join(ip) in '255.255.255.255':
      print('local broadcast')
      break

  elif '.'.join(ip) in '0.0.0.0':
      print('unssigned')
      break

  else:
      print('unused')
      break