def determine_flight_time(start_time: int, end_time: int, current_time_diffrence: int):
    if start_time > end_time + (current_time_diffrence*60):
        return 1440+end_time - start_time + (current_time_diffrence*60)
    elif end_time-start_time+(current_time_diffrence*60) > 1440:
        return end_time-(start_time+1440-(current_time_diffrence*60))
    else:
        return end_time-start_time + (current_time_diffrence*60)


def crude_to_polished_time(time_str: list):
    return int(time_str.split(
        ".")[0]) * 60+int(time_str.split(".")[1])


max_flight_time = 360
time_diffrence = -1

flight_out_start, flight_out_end = 0, 0
current_flight_crude = input().split()
flight_out_start = crude_to_polished_time(current_flight_crude[0])
flight_out_end = crude_to_polished_time(current_flight_crude[1])
current_flight_crude = input().split()
flight_back_start = crude_to_polished_time(current_flight_crude[0])
flight_back_end = crude_to_polished_time(current_flight_crude[1])

#
# print(flight_out_start, flight_out_end,
#       flight_back_start, flight_back_end, sep="\n")
#

for proposed_time_diffrence in range(-5, 6):
    flight_time_there = determine_flight_time(
        flight_out_start, flight_out_end, proposed_time_diffrence)
    flight_time_back = determine_flight_time(
        flight_back_start, flight_back_end, proposed_time_diffrence*-1)

    if abs(flight_time_there - flight_time_back) <= 10 and flight_time_there <= max_flight_time and flight_time_back <= max_flight_time:
        time_diffrence = abs(proposed_time_diffrence)
        #print("Found Match")
print(time_diffrence)
