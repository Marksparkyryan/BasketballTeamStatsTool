import logging
import os
from constants import TEAMS, PLAYERS

#debug logging to app.log
logging.basicConfig(filename="app.log", level=logging.DEBUG)


def start_app():
    """Initaites the game logic and some variables.
    """
    
    teams = [{team:list()} for team in TEAMS]
    
    def clean_player(**player):
        """Takes each player dictionary in list of player dictionaries 
        and redirects into a dict unpacking function and then finally a 
        dict packing function below. 
        """


        def player_packer(**kwargs):
            """Packs each player and individual objects back into key, value
            dictionary format.  
            """

            return kwargs


        def player_unpacker(name, guardians, experience, height):
            """Unpacks each vakue in player dictionary provided into 
            individual objects. Each object can then be modified if 
            necessary i.e. guardians is split into a list of values.  
            """

            guardians = guardians.split(" and ")
            clean_player = player_packer(name=name, 
                          guardians=guardians, 
                          experience=experience,
                          height=height)
            return clean_player

        clean_player = player_unpacker(**player)
        return clean_player
    

    def balance_players():
        """Split all players into lists of experienced and 
        non-experienced players. Then, distribute experienced and 
        non-experienced players evenly among available teams.
        """
        
        experienced_players = []
        non_experienced_players = []
        for player in cleaned_players:
            if player["experience"] == "YES":
                experienced_players.append(player)
            else:
                non_experienced_players.append(player)
        team_keys = [key for team in teams for key in team]
        for start in range(0,len(teams)):
            for i in range(start, len(experienced_players), len(teams)):
                teams[start][team_keys[start]].append(experienced_players[i])
        for start in range(0,len(teams)):
            for i in range(start, len(non_experienced_players), len(teams)):
                teams[start][team_keys[start]].append(non_experienced_players[i])


    def menu_display(version):
        """Display appropriate menus/info based on keyword passed in.
        """

        if version == "greeting":
            print("\n")
            print("Basketball Team Stats Tool")
        
        if version == "main":
            menu_display("greeting")
            print("\n")
            print("----------Menu---------")
            print("1. Display Team Stats")
            print("2. Quit") 
            print("\n")
    
        if version == "teams":
            menu_display("greeting")
            print("\n")
            print("----------Teams---------")
            for team in teams:
                for key in team:
                    print("{}. {}".format(teams.index(team) + 1, key))
            print("{}. Quit".format(len(TEAMS)+1))
            print("\n")

        if version == "again":
            print("\n")
            if input("""Continue? Press any key to continue, """
            """or "n" to quit. > """).lower() == "n":
                menu_display("goodbye")
                quit()
            else:
                pass
        
        if version == "goodbye":
            clear_screen()
            print("\n")
            print("Goodbye! See you soon!")
            print("\n")
    

    def clear_screen():
        """Clears terminal screen when called.
        """

        os.system("cls" if os.name == "nt" else "clear")


    def choice_checker():
        """Verifies that choice selection is a digit then converts to 
        integer.
        """

        while True:
            try:
                choice = input("Please choose an option (number) above. > ")
                if not choice.isdigit():
                    raise ValueError("Choice must be a positive integer value."
                    " Please try again.")
                else:
                    choice = int(choice)
                    return choice
            except ValueError as err:
                print("Uh oh! {}".format(err))
                continue


    def menu_handler(menu, choice):
        """Display correct menu to user, check if user's choice is 
        available on displayed menu, and display further information to 
        user based on menu selection i.e. team stats. 
        """

        main_choices = [1, 2]
        team_choices = [TEAMS.index(team)+1 for team in TEAMS]
        team_choices.append(len(team_choices)+1)
        
        if menu == "main":
            while True:
                try:
                    if choice not in main_choices:
                        raise ValueError("Invalid menu selection. "
                        "Please try again.")
                except ValueError as err:
                    print("Uh oh! {}".format(err))
                    choice = choice_checker()
                else:  
                    if choice == 1:
                        clear_screen()
                        menu_display("teams")
                        break
                    if choice == 2:
                        clear_screen()
                        menu_display("goodbye")
                        quit()

        if menu == "teams":
            while True:
                try:
                    if int(choice) not in team_choices:
                        raise ValueError("Invalid menu selection. "
                        "Please try again.")   
                except ValueError as err:
                    print("Uh oh! {}".format(err))
                    choice = choice_checker()
                else:
                    if int(choice) == len(team_choices):
                        clear_screen()
                        menu_display("goodbye")
                        quit()
                    else:
                        clear_screen()
                        stat_display(choice)
                        break


    def stat_display(choice):
        """Display selected team stats to user. 
        """

        inexperienced_players = 0
        experienced_players = 0
        players_heights = 0
        index = int(choice)-1
        team_name = None
        all_guardians = []
        max_height = 0 
        min_height = 99 

        for key in teams[index]:
            team_name = key
        
        number_players = len(teams[int(choice)-1][key])

        for player in teams[int(choice)-1][key]:    
            if player["experience"] == "NO":
                inexperienced_players += 1
            else:
                experienced_players += 1
            players_heights += int(player["height"][:3])
            player_height = int(player["height"][:3])
            if player_height > max_height:
                max_height = player_height
            if player_height < min_height:
                min_height = player_height
            for guardian in player["guardians"]:
                all_guardians.append(guardian)

        average_height = players_heights / len(teams[int(choice)-1][key])
        
        def progress_bar(multiple):
            """Display/represent data from stats display to user via
            visually engaging progress bars. Each block in bar represents 
            an approriate unit of information. 
            """

            bar = "" + ("⬜ " * multiple) + ""
            return bar 
        
        #debug logging line for team dicts
        logging.debug("team items: {}".format(teams[int(choice)-1]))
        
        menu_display("greeting")
        
        print("\n")
        print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁"
        "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
        print("Team Stats")  
        print("\n")  
        print("Team Name:", team_name)
        print("\n")
        print("Number of Players:", number_players, "\t\t", 
            progress_bar(number_players))
        print("Experienced Players: ", experienced_players, "\t", 
            progress_bar(experienced_players))
        print("Inexperienced Players:", inexperienced_players, "\t", 
            progress_bar(inexperienced_players))
        print("\n")
        print("Max Height:", max_height, "inches", "\t\t", 
            progress_bar(max_height))
        print("Avg Height:", int(average_height), "inches", "\t\t", 
            progress_bar(int(average_height)))
        print("Min Height:", min_height, "inches", "\t\t", 
            progress_bar(min_height))
        print("\n")
        print("Players:")
        for player in teams[int(choice)-1][key]:
            print(player["name"], end=", ")
        print("\nGuardians:")
        for guardian in all_guardians:
            print(guardian, end=", ")
        print("\n")
        print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁"
        "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")

    cleaned_players = [clean_player(**player) for player in PLAYERS]
    balance_players()

    while True:
        clear_screen()
        menu_display("main")
        choice = choice_checker()
        
        menu_handler("main", choice)
        choice = choice_checker()        
        
        menu_handler("teams", choice)
        menu_display("again")

 
if __name__ == "__main__":
    start_app()
