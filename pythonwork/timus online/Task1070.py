flight_out_start, flight_out_end = [
    list(map(int, i.split("."))) for i in list(input().split())]
flight_back_start, flight_back_end = [
    list(map(int, i.split("."))) for i in list(input().split())]
flight_duration_margin_of_error = 10
max_flight_time = 6
max_time_diffrence = 5
flight_out_additive = 0
flight_back_additive = 0
time_diffrence = 0
if flight_out_start[0] > flight_out_end[0] or (flight_out_start[0] == flight_out_end[0] and flight_out_start[1] > flight_out_end[1]):
    flight_out_additive = 24
    #print("Additive True")
if (flight_back_start[0] > flight_back_end[0]) or (flight_back_start[0] == flight_back_end[0] and flight_back_start[1] > flight_back_end[1]):
    flight_back_additive = 24
for proposed_time_diffrence in range(5, -1, -1):
    #print("Proposed_Time_Diffrence =", proposed_time_diffrence)

    flight_time_there = flight_out_end[0] - flight_out_start[0] + \
        proposed_time_diffrence + flight_out_additive

    #print("Flight_Time_There =", flight_time_there)

    flight_time_back = flight_back_end[0] - flight_back_start[0] - \
        proposed_time_diffrence + flight_back_additive

    #print("Flight_Time_Back =", flight_time_back)

    if flight_time_there == flight_time_back and flight_time_there <= 6:
        time_diffrence = proposed_time_diffrence
        #print("Found Match")
print(time_diffrence)
