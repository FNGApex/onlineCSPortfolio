from math import ceil
page_height, page_width, words_amount = list(map(int, input().split()))
words = [input() for i in range(words_amount)]
line_count = 1
current_line = words[0]
for i in words[1:]:
    if len(current_line + " " + i) <= page_width:
        current_line += " " + i
    else:
        # print(current_line)
        #print(*list(range(1, page_width+1)), sep="")
        current_line = i
        line_count += 1
# print(current_line)
#print(*list(range(1, page_width+1)), sep="")
print(ceil(line_count/page_height))
