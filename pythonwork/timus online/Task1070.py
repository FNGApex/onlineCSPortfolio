def determine_flight_time(starttime: list, endtime: list, time_diffrence: int):
    start_hour = starttime[0]
    end_hour = endtime[0]
    if start_hour > end_hour+time_diffrence:
        return 24+end_hour-start_hour+time_diffrence
    else:
        return end_hour-start_hour+time_diffrence


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
for proposed_time_diffrence in range(-5, 6):
    flight_time_there = determine_flight_time(
        flight_out_start, flight_out_end, proposed_time_diffrence)
    flight_time_back = determine_flight_time(
        flight_back_start, flight_back_end, proposed_time_diffrence*-1)
    #print("Flight_Time_Back =", flight_time_back)

    if flight_time_there == flight_time_back and flight_time_there <= 6:
        time_diffrence = proposed_time_diffrence
        #print("Found Match")
print(abs(time_diffrence))
