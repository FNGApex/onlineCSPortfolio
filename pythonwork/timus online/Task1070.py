def determine_flight_time(start_time: list, end_time: list, time_diffrence: int):
    if start_time > end_time+time_diffrence*60:
        return 1440+end_time-start_time+time_diffrence*60
    else:
        return end_time-start_time+time_diffrence*60


max_flight_time = 370
time_diffrence = -1

flight_out_start, flight_out_end = 0, 0
current_flight_crude = input().split()
flight_out_start = int(current_flight_crude[0].split(
    ".")[0]) * 60+int(current_flight_crude[0].split(".")[1])
flight_out_end = int(current_flight_crude[1].split(
    ".")[0]) * 60+int(current_flight_crude[1].split(".")[1])
current_flight_crude = input().split()
flight_back_start = int(current_flight_crude[0].split(
    ".")[0]) * 60+int(current_flight_crude[0].split(".")[1])
flight_back_end = int(current_flight_crude[1].split(
    ".")[0]) * 60+int(current_flight_crude[1].split(".")[1])

#
# print(flight_out_start, flight_out_end,
#       flight_back_start, flight_back_end, sep="\n")
#

for proposed_time_diffrence in range(-5, 6):
    flight_time_there = determine_flight_time(
        flight_out_start, flight_out_end, proposed_time_diffrence)
    flight_time_back = determine_flight_time(
        flight_back_start, flight_back_end, proposed_time_diffrence*-1)
    #print("Flight_Time_Back =", flight_time_back)

    if abs(flight_time_there - flight_time_back) <= 10 and flight_time_there <= max_flight_time:
        time_diffrence = abs(proposed_time_diffrence)
        #print("Found Match")
print(time_diffrence)
