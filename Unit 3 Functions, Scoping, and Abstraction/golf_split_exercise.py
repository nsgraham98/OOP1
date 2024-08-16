
def create_golf_player_scores():
    golf_file = open("golf.txt", "w")

    num_players = (int(input("Enter number of golf players: ")))

    for i in range(1, num_players + 1):
        player_name = input(f"Enter name of player {i}: ")
        player_score = input(f"Enter score for player {i}: ")
        golf_file.write(f"{player_name},{player_score}\n")
        
    golf_file.close()

create_golf_player_scores()

def golf_file_print():
    golf_file = open("golf.txt", "r")

    for i in golf_file:
        player_list = i.rstrip().split(",")
        player_name = player_list[0]
        player_score = player_list[1]
        print(f"{player_name} - {player_score}\n")
    golf_file.close()

golf_file_print()