import pprint
from constants import TEAMS, PLAYERS

players_per_team = int(len(PLAYERS) / len(TEAMS))


def start_app():
    
    teams = [{team:list()} for team in TEAMS]
    
    
    def clean_player(**player):
        
        def player_packer(**kwargs):
            return kwargs
        
        def player_unpacker(name, guardians, experience, height):
            #modify player data here
            clean_player = player_packer(name=name, 
                          guardians=guardians, 
                          experience=experience,
                          height=height)
            return clean_player


        clean_player = player_unpacker(**player)
        return clean_player
    

    def menu_display(version):
        if version == "main":
            print("\n")
            print("Basketball Team Stats Tool")
            print("\n")
            print("----------Menu---------")
            print("\n")
            print("1. Display Team Stats")
            print("2. Quit") 
            print("\n")
        
        if version == "teams":
            print("\n")
            for team in TEAMS:
                print("{}. {}".format(TEAMS.index(team) + 1, team))
            print("{}. Quit".format(len(TEAMS)+1))
            print("\n")
    

    def menu_handler(menu, choice):
        main_choices = [1, 2]
        team_choices = [TEAMS.index(team)+1 for team in TEAMS]
        while True:
            try:
                choice = input("Please choose an option (number) above. > ")
                if not choice.isdigit():
                    raise ValueError("Choice must be an integer value. Please try again!")
                    continue 
                choice = int(choice)    
                if menu == "main":
                    if choice in main_choices:
                        if choice == 1:
                            menu_display("teams")
                            choice  = input("Please choose a team (number) above. > ")
                            stat_display(choice)
                            
                            break
                        if choice == 2:
                            quit() 
                        break
                if menu == "teams":
                    if int(choice) in team_choices:
                        print(choice)
                        break
                else:
                    raise ValueError("Something went wrong. Please try again!")
            except ValueError as err:
                print("Uh oh! {}".format(err))
                continue
    

    def stat_display(choice):
        for key in teams[int(choice)-1]:
            print(key)



    cleaned_players = [clean_player(**player) for player in PLAYERS]
    choice = menu_display("main")
    menu_handler("main", choice)
    
    

if __name__ == "__main__":
    start_app()