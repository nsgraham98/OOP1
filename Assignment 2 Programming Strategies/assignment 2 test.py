# vehicle_selected = False
# duration_selected = False
# features_selected = False
# features_prompt = f"{"="*75}\nEnter the number corresponding to the feature you'd like to rent (One at a time): \n1 - GPS Navigation ($5/day) \n2 - Mobile Wi-Fi ($8/day) \n3 - Child Seat ($2/day) \n4 - Toll Pass ($4.50/day)\n5 - Roadside Assistance Plus ($5/day)\n0 - Enter '0' when finished\n{"="*75}\n"

# gps = False
# child_seat = False
# wifi = False
# road_assist = False
# toll_pass = False

# adding_user_rentals = True
# total_current_session = 0
# all_sessions = []
 
 
# while adding_user_rentals == True:
#     while vehicle_selected == False:
#         vehicle_type =  int(input(f"{"="*75}\nEnter the number corresponding to the vehicle you'd like to rent: \n1 - Compact ($25/day) \n2 - Sedan ($35/day) \n3 - SUV ($50/day) \n4 - Luxury ($60/day)\n{"="*75}\n"))
#         if vehicle_type == 1:
#             total_current_session += 25
#             vehicle_selected = True
#         elif vehicle_type == 2:
#             total_current_session += 35
#             vehicle_selected = True
#         elif vehicle_type == 3:
#             total_current_session += 50
#             vehicle_selected = True
#         elif vehicle_type == 4:
#             total_current_session += 60
#             vehicle_selected = True
#         else:
#             print(f"{"="*75}\nPlease enter a valid vehicle selection (using all lowercase letters):\n{"="*75}\n")        
 
#     while duration_selected == False:
#         duration = int(input(f"{"="*75}\nHow many days would you like to rent for?\n1 day - (no discount)\n2-3 days - (4% discount)\n4-7 days - (10% discount)\n8+ days - (20% discount)\n{"="*75}\n"))
#         if duration == 1:
#             duration_selected = True    
#         elif duration <= 3:
#             total_current_session = (total_current_session * duration) / 1.04
#             duration_selected = True
#         elif duration <= 7:
#             total_current_session = (total_current_session * duration) / 1.1
#             duration_selected = True    
#         elif duration >= 8:
#             total_current_session = (total_current_session * duration) / 1.2
#             duration_selected = True    
#         else:
#             print(f"{"="*75}\nPlease enter a valid number of days (number only).\n{"="*75}\n")  
 
#     while features_selected == False:
#         features = int(input(features_prompt))
#         if (features == 1) and (gps == False):
#             gps = True
#             total_current_session += (5 * duration)
#             features_prompt = features_prompt.replace("1 -", "1 ✓")
#         elif (features == 2) and (wifi == False):
#             wifi = True
#             total_current_session += (8 * duration)
#             features_prompt = features_prompt.replace("2 -", "2 ✓")
#         elif (features == 3) and (child_seat == False):
#             child_seat = True
#             total_current_session += (2 * duration)
#             features_prompt = features_prompt.replace("3 -", "3 ✓")
#         elif (features == 4) and (toll_pass == False):
#             toll_pass = True
#             total_current_session += (4.5 * duration)
#             features_prompt = features_prompt.replace("4 -", "4 ✓")
#         elif (features == 5) and (road_assist == False):
#             road_assist = True
#             total_current_session += (5 * duration)
#             features_prompt = features_prompt.replace("5 -", "5 ✓")
#         elif features == 0:
#             features_selected = True
#         else:
#             print(f"{"="*75}\nError: Please re-enter your option (one at a time):\n{"="*75}\n ")
 
#     additional_rental_question = int(input(f"{"="*75}\nWould you like to rent another vehicle?\n1 - Yes \n0 - No\n{"="*75}\n"))
 
#     if additional_rental_question == 0:
#         adding_user_rentals = False
#         all_sessions.append(total_current_session)
#     elif additional_rental_question == 1:
#         vehicle_selected = False
#         duration_selected = False
#         features_selected = False
#         all_sessions.append(total_current_session)
#         total_current_session = 0
# else:
#     print(all_sessions)

vehicle_selected = False
duration_selected = False
features_selected = False
feature1_used = False
feature2_used = False
feature3_used = False
feature4_used = False
feature5_used = False

checkmark1 = ""
checkmark2 = ""
checkmark3 = ""
checkmark4 = ""
checkmark5 = ""
 
adding_user_rentals = True
total_current_session = 0
all_sessions = []
 
 
while adding_user_rentals == True:
    while vehicle_selected == False:
        vehicle_type =  int(input(f"{'='*75}\nEnter the number corresponding to the vehicle you'd like to rent: \n1 - Compact ($25/day) \n2 - Sedan ($35/day) \n3 - SUV ($50/day) \n4 - Luxury ($60/day)\n{'='*75}\n"))
        if vehicle_type == 1:
            total_current_session += 25
            vehicle_selected = True
        elif vehicle_type == 2:
            total_current_session += 35
            vehicle_selected = True
        elif vehicle_type == 3:
            total_current_session += 50
            vehicle_selected = True
        elif vehicle_type == 4:
            total_current_session += 60
            vehicle_selected = True
        else:
            print(f"{'='*75}\nPlease enter a valid vehicle selection (using all lowercase letters):\n{'='*75}\n")        
 
    while duration_selected == False:
        duration = int(input(f"{'='*75}\nHow many days would you like to rent for?\n1 day - (no discount)\n2-3 days - (4% discount)\n4-7 days - (10% discount)\n8+ days - (20% discount)\n{'='*75}\n"))
        if duration == 1:
            duration_selected = True    
        elif duration <= 3:
            total_current_session = (total_current_session * duration) / 1.04
            duration_selected = True
        elif duration <= 7:
            total_current_session = (total_current_session * duration) / 1.1
            duration_selected = True    
        elif duration >= 8:
            total_current_session = (total_current_session * duration) / 1.2
            duration_selected = True    
        else:
            print(f"{'='*75}\nPlease enter a valid number of days (number only).\n{'='*75}\n")  
 
    while features_selected == False:
        features = int(input(f"{"="*75}\nEnter the number corresponding to the feature you'd like to rent (One at a time): \n1 - GPS Navigation ($5/day){checkmark1:>5}\n2 - Mobile Wi-Fi ($8/day){checkmark2:>5} \n3 - Child Seat ($2/day){checkmark3:>5} \n4 - Toll Pass ($4.50/day){checkmark4:>5}\n5 - Roadside Assistance Plus ($5/day){checkmark5:>5}\n0 - Enter '0' when finished\n{"="*75}\n"))
        if features == 1:
            if feature1_used == True:
                print("You cannot enter a feature you have previously selected.")
            total_current_session += (5 * duration)
            feature1_used = True
            checkmark1 = "\u2713"
        elif features == 2:
            if feature2_used == True:
                print("You cannot enter a feature you have previously selected.")
            total_current_session += (8 * duration)
            feature2_used = True
            checkmark2 = "\u2713" 
        elif features == 3:
            if feature3_used == True:
                print("You cannot enter a feature you have previously selected.")
            total_current_session += (2 * duration)
            feature3_used = True
            checkmark3 = "\u2713"
        elif features == 4:
            if feature4_used == True:
                print("You cannot enter a feature you have previously selected.")
            total_current_session += (4.5 * duration)
            feature4_used = True
            checkmark4 = "\u2713" 
        elif features == 5:
            if feature1_used == True:
                print("You cannot enter a feature you have previously selected.")
            total_current_session += (5 * duration)
            feature5_used = True
            checkmark5 = "\u2713" 
        elif features == 0:
            features_selected = True
        else:
            print(f"{'='*75}\nError: Please re-enter your option (one at a time):\n{'='*75}\n ")
 
    additional_rental_question = int(input(f"{'='*75}\nWould you like to rent another vehicle?\n1 - Yes \n0 - No\n{'='*75}\n"))
 
    if additional_rental_question == 0:
        adding_user_rentals = False
        all_sessions.append(total_current_session)
    elif additional_rental_question == 1:
        vehicle_selected = False
        duration_selected = False
        features_selected = False
        all_sessions.append(total_current_session)
        total_current_session = 0
        checkmark1 = ""
        checkmark2 = ""
        checkmark3 = ""
        checkmark4 = ""
        checkmark5 = ""  
        feature1_used = False
        feature2_used = False
        feature3_used = False
        feature4_used = False
        feature5_used = False   
else:
    print(all_sessions)