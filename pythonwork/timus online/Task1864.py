import fractions
from math import floor
amount_of_friends = int(input())
amount_of_juice = list(map(int,input().split()))
juice_net = []
total_juice = sum(amount_of_juice)
#juice_consumed = total_juice/(amount_of_friends+1)
#juice_consumed = (total_juice,amount_of_friends+1)
for i in amount_of_juice:
  temp = ((i*(amount_of_friends+1))-(total_juice),amount_of_friends+1)
  juice_net.append(max([0,0],temp,key= lambda x: x[0]))
#print(juice_net)
total_juice_net = sum(i[0] for i in juice_net)
#print(total_juice_net)
for i in juice_net:
  #(i[0]/i[1])/(total_juice_net[0]/total_juice[1])
  payout = floor(i[0]/total_juice_net*100)
  print(payout, end=" ")
#print(juice_net)
