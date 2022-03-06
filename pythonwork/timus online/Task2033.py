import sys
x = list(map(lambda x: x.strip("\n"), sys.stdin.readlines()))
devices = {}
for i in range(0,17,3):
  friend_name = x[i]
  device_name = x[i+1]
  device_price = int(x[i+2])
  amount_of_devices = devices.get(device_name,[0,0])[1]
  old_device_price = devices.get(device_name,[0,0])[0]
  if old_device_price > device_price or old_device_price == 0:
    new_device_price = device_price
  else:
    new_device_price = old_device_price
  amount_of_devices += 1
  devices[device_name] = [new_device_price,amount_of_devices]
devices = list(devices.items())
#print(devices)
devices.sort(key=lambda x:x[1][1],reverse=True)
highest_amount = devices[0][1][1]
popular_devices = [i for i in devices if i[1][1] == highest_amount]
#print(popular_devices)
print(sorted(popular_devices, key= lambda x: x[1])[0][0])