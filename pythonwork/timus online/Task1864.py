from math import floor
amount_of_friends = int(input())
amount_of_juice = list(map(int,input().split()))
juice_net = []
total_juice = sum(amount_of_juice)
juice_consumed = total_juice/(amount_of_friends+1)
for i in amount_of_juice:
  juice_net.append(max(0,i-juice_consumed))
total_juice_net = sum(juice_net)
for i in juice_net:
  payout = floor(i/total_juice_net*100)
  print(payout, end=" ")
print(juice_net)
