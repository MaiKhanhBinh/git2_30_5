import netmiko
SW={
    "device_type":"cisco_ios",
    "ip":"10.215.27.83",
    "username":"vnpro",
    "password":"vnpro@123",
    "secret":"vnpro@321",
}
connect=netmiko.ConnectHandler(**SW)
print (connect.enable())
print (connect.send_config_set(["do sh ip int br","do sh vlan br"]))

for i in range(10,101,10):
    print (connect.send_config_set([f"vlan {i}"]))
print (connect.send_config_set(["do sh vlan br"]))
