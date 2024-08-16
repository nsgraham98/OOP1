vehicle_selected = False
duration_selected = False
features_selected = False

gps = False
wifi = False
child_seat = False
toll_pass = False
road_assist = False

checkmark1 = ""
checkmark2 = ""
checkmark3 = ""
checkmark4 = ""
checkmark5 = ""

adding_user_rentals = True
sum_current_session = 0
all_sessions = []


while adding_user_rentals == True:
    while vehicle_selected == False:
        vehicle_type =  int(input(f"{"="*75}\nEnter the number corresponding to the vehicle you'd like to rent: \n1 - Compact ($25/day) \n2 - Sedan ($35/day) \n3 - SUV ($50/day) \n4 - Luxury ($60/day)\n{"="*75}\n"))
        if vehicle_type == 1:
            sum_current_session += 25
            vehicle_selected = True
        elif vehicle_type == 2:
            sum_current_session += 35
            vehicle_selected = True
        elif vehicle_type == 3:
            sum_current_session += 50
            vehicle_selected = True
        elif vehicle_type == 4:
            sum_current_session += 60
            vehicle_selected = True
        else:
            print(f"{"="*75}\nPlease enter a valid vehicle selection (using all lowercase letters):")        

    while duration_selected == False:
        duration = int(input(f"{"="*75}\nHow many days would you like to rent for?\n1 day - (no discount)\n2-3 days - (4% discount)\n4-7 days - (10% discount)\n8+ days - (20% discount)\n{"="*75}\n"))
        if duration == 1:
            duration_selected = True     
        elif duration <= 3:
            sum_current_session = (sum_current_session * duration) / 1.04
            duration_selected = True
        elif duration <= 7:
            sum_current_session = (sum_current_session * duration) / 1.1
            duration_selected = True    
        elif duration >= 8:
            sum_current_session = (sum_current_session * duration) / 1.2
            duration_selected = True    
        else:
            print(f"{"="*75}\nPlease enter a valid number of days (number only).\n{"="*75}\n")  

    while features_selected == False:
        features = int(input(f"{"="*75}\nEnter the number corresponding to the feature you'd like to rent (One at a time): \n1 - GPS Navigation ($5/day){checkmark1:>5}\n2 - Mobile Wi-Fi ($8/day){checkmark2:>5} \n3 - Child Seat ($2/day){checkmark3:>5} \n4 - Toll Pass ($4.50/day){checkmark4:>5}\n5 - Roadside Assistance Plus ($5/day){checkmark5:>5}\n0 - Enter '0' when finished\n{"="*75}\n"))
        if features == 1:
            if gps == True:
                print("You cannot enter a feature you have previously selected.")
            sum_current_session += (5 * duration)
            gps = True
            checkmark1 = "\u2713"
        elif features == 2:
            if wifi == True:
                print("You cannot enter a feature you have previously selected.")
            sum_current_session += (8 * duration)
            wifi = True
            checkmark2 = "\u2713" 
        elif features == 3:
            if child_seat == True:
                print("You cannot enter a feature you have previously selected.")
            sum_current_session += (2 * duration)
            child_seat = True
            checkmark3 = "\u2713"
        elif features == 4:
            if toll_pass == True:
                print("You cannot enter a feature you have previously selected.")
            sum_current_session += (4.5 * duration)
            toll_pass = True
            checkmark4 = "\u2713" 
        elif features == 5:
            if road_assist == True:
                print("You cannot enter a feature you have previously selected.")
            sum_current_session += (5 * duration)
            road_assist = True
            checkmark5 = "\u2713" 
        elif features == 0:
            features_selected = True
        else:
            print(f"{'='*75}\nError: Please re-enter your option (one at a time):\n{'='*75}\n ")

    additional_rental_question = int(input(f"{"="*75}\nWould you like to rent another vehicle?\n1 - Yes \n0 - No\n{"="*75}\n"))

    if additional_rental_question == 0:
        adding_user_rentals = False
        all_sessions.append(sum_current_session)
    elif additional_rental_question == 1:
        all_sessions.append(sum_current_session)
        sum_current_session = 0
        vehicle_selected = False
        duration_selected = False
        features_selected = False
        gps = False 
        wifi = False
        child_seat = False
        toll_pass = False
        road_assist = False
        checkmark1 = ""
        checkmark2 = ""
        checkmark3 = ""
        checkmark4 = ""
        checkmark5 = ""

else:
    print(f"{"="*30}\nBill Summary:\n{"="*30}")
    n = 1
    for session in all_sessions:
        print(f"{"Vehicle: ":<10}{n}{session:>10.2f}")
        n += 1
print(f"{"="*30}\n{"GST: ":<10}{sum(all_sessions) * 0.05:>10.2f}\n{"="*30}")
print(f"{"Total Due: ":<10}{sum(all_sessions) * 1.05:>10.2f}\n{"="*30}")
