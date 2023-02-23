air_controller_messages_dictionary = {
    "q1": "Air-traffic-controller: Is flight B12 is takeoff already? [y/n]:",
    "q2": "Air-traffic-controller: is current weather is between -35 to -55? [y/n]:",
    "q3": "Air-traffic-controller: Is flight A12 completed covid-19 health requirements? [y/n]:",
    "q4": "Air-traffic-controller: Please proceed to gate 12",
    "q5": "Air-traffic-controller: Is the current weather is safe to land? [y/n]: ",
    "redirect": "Air-traffic-controller: we are redirecting you to nearby airport.",
    "taxi": "Air-traffic-controller: Flight A12 you're clear taxi is open proceed to gate G12",
}

air_controller_flights_records = {
    "inbound": "",
    "outbound": "",
    "maintenance": "idle",
    "isHealthRequirementCompleted": False,
    "isLanded": False,
}

is_flight_B12_takeoff = str(input(air_controller_messages_dictionary["q1"]))

if is_flight_B12_takeoff == "n":
    air_controller_flights_records["outbound"] = "Flight B12" 
    print("Wait for flight B12 to take off first.")
    print(air_controller_messages_dictionary["redirect"])
else:
    air_controller_flights_records["inbound"] = "Flight A12" 
    set_flight_current_weather = str(input(air_controller_messages_dictionary["q2"]))

    if set_flight_current_weather == "y":
        print("Weather is not safe to land.")
        print(air_controller_messages_dictionary["redirect"])
    else:
        is_weather_okay = str(input(air_controller_messages_dictionary["q5"]))
        if is_weather_okay == "n":
            print(air_controller_messages_dictionary["redirect"])
        else:
            is_health_req_complete = str(
                input(air_controller_messages_dictionary["q3"])
            )
            if is_health_req_complete == "n":
                print('Need to complete covid-19 health requirements first')
                print(air_controller_messages_dictionary["redirect"])
            else:
                air_controller_flights_records["maintenance"] = "operation"
                air_controller_flights_records["isHealthRequirementCompleted"] = True
                air_controller_flights_records["isLanded"] = True
                print(air_controller_messages_dictionary["taxi"])
                print(air_controller_flights_records)