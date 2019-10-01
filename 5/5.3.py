access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

template = dict(access = access_template, trunk = trunk_template)
mainPart = '\n'.join(template.get(input('choose type access/trunk: '), 'No such thing... im done here')).format(input('vlan: '))
print('\n' + f'interface {input("interface type: ")}' + '\n' + mainPart)