def formatLine(time: int, line_number: int):
    line = ""
    classes = []
    # classes = [["Social Science"], [
    #    "Theo Phys Math"], ["Advanced Python Prog"]]
    for i in range(3):
        classes.append(formated_calendar[i][time])
    formated_classes = []
    current_line_number = 1
    line_number += 1
    current_segment = ''
    #print("Classes =", classes)
    #print("Line Number =", line_number, "Time =", time)
    #print()
    for i in classes:
        current_line_number = 1
        #print("New Class")
        current_segment = ""
        if i == []:
          formated_classes.append(None)
        else:
            for j in i[0].split():
                #print("Class = ", i)
                #print("Segment:", current_segment)
                #print("J:", j)
                if len(current_segment + j) > 10:
                    #print("Can't add more")
                    #print("Current Line Number", current_line_number)
                    #print("Desired Line Number", line_number)
                    if current_line_number == line_number:
                        #print("Current and Desired Line Numbers Match")
                        #print("Appending Segment", current_segment)
                        formated_classes.append(current_segment[:-1])
                        break
                    #print("Line Numbers Do Not Match Resseting Segment Incrementing Line Number")
                    current_segment = ""
                    current_line_number += 1
                #print("Combining", current_segment, "and", j)
                current_segment += j + " "
                #print()
            else:
                if current_line_number == line_number:
                    formated_classes.append(current_segment[:-1])
                else:
                    formated_classes.append(None)
    if formated_classes == [None, None, None]:
        return None
    return formated_classes


n = int(input())
daytodate = {"Saturday": 2, "Thursday": 1, "Tuesday": 0}
formated_calendar = []
for i in range(3):
    formated_calendar.append([[], [], [], []])
for i in range(n):
    class_name = input()
    day, time = input().split()
    day = daytodate[day]
    formated_calendar[day][int(time)-1] = [class_name]
lines = []
separator = "+----------+----------+----------+"
#print(separator)

for time in range(4):
    line_number = 0
    # while True:
    for i in range(5):
        current_line = formatLine(time, line_number)
        line_number += 1
        if current_line == None:
            if line_number == 1:
                lines.append([None, None, None])
            break
        lines.append(current_line)
    lines.append("New_Day")
    #print("New Day")
#print("Lines", lines)
print(separator)
for i in lines:
    if i == "New_Day":
        print(separator)
    else:
        print("|", end="")
        for j in i:
            if j == None:
                print("          |",end="") 
            else:
                print(j+" "*(10-len(j)),end="|")
        print()
