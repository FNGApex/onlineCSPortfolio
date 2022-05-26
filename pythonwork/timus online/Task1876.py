# On left Foot
# ALl right boots
# x2*2
# Switch to left boots
# min(x1,40)
# x2*2+x1

# On left Foot
# 39 right boots when on left leg
# +78
# Now equip 39 left boots
# +39
# Switch to Other Leg
# 1 Right boot not equiped
# Find all remaining left boots
# (x1-39)*2
# equip the last right boot
# +1
# 78+39+(x1-39)*2

x1, x2 = list(map(int, input().split()))
print(max([(78+39+(x1-39)*2), (x2*2+min(x1, 40))]))