def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    config = []
    for item in intf_vlan_mapping:
      config.append(f'interface {item}')
      for line in access_template:
        if line.endswith('vlan'):
          line += f' {str(intf_vlan_mapping[item])}'
        config.append(line)
      
    print(config)

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

generate_access_config(access_config,access_mode_template)