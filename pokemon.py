from random import *
from dex import dex_dict

       
#############################################################################################################################################
# Main Pokemon Class
class Pokemon:
    # The pokemon class will be used to create the pokemons derived from the full (up to gen 6) pokedex. 
    def gen_hp(self, lvl, base):
        """This funcion will be called when the pokemon object is created and it will  
            calculate the pokemons total hp (3rd gen onward formula) from the stats dex_dict stats.
        

        Args:
            lvl (int): Pokemons level
            base (int): stat multiplier

        Returns:
            int: returns
        """
        base_hp = int(base)
        
        hp = ((base_hp*2 * lvl)//100)+lvl+10
        return hp
    
    def gen_stat(self, lvl, base):
        """This funcion will be called when the pokemon object is created and it will  
            calculate each stat (3rd gen onward formula) from the stats dex_dict stats

        Args:
            lvl (int): Pokemons level
            base (int): stat multiplier

        Returns:
            int: returns
        """
        # each argument is passed in as a string and converted to an int
        base = int(base)        
        # stat formula not considering EV's or IV's    
        stat = (((2*base)*lvl)//100)+5
        return stat



    def __init__(self, id, lvl):
        
        base_stats = dex_dict.get(id)  
            # base_stats from the dex_dict
            #(id, name, type1, type2=None, total, hp, attack, defense, sp_atk, sp_def, speed, gen, legendary)
            #  0    1     2        3         4     5    6        7        8       9      10    11       12   
        
        self.id = id
        self.lvl = lvl
        self.name = base_stats[0]
        self.type1 = base_stats[1]
        self.type2 = base_stats[2]
        self.total = base_stats[3]
        # ------------------------------
            # stat generation, for each pokemon stat the program will use the base stat at the
            # base_stats corresponding index to then calculate the actual stat
        self.hp = self.gen_hp(lvl, base_stats[4])
        self.attack = self.gen_stat(lvl, base_stats[5])
        self.defense = self.gen_stat(lvl, base_stats[6])
        self.sp_atk = self.gen_stat(lvl, base_stats[7])
        self.sp_def = self.gen_stat(lvl, base_stats[8])
        self.speed = self.gen_stat(lvl, base_stats[9])
        # ------------------------------
        # gen stat is not that relevant but still included for a future "Pokedex menu option"
        self.gen = base_stats[10]
        # legendary stat is relevan for catch rates.
        self.legendary = base_stats[11]
        #pkm is a list containing the final pokemon data.
                #       0         1         2         3         4             5            6             7          8             9            10             11        12
        self.pkm = [self.id, self.name, self.lvl, self.hp, self.attack, self.defense, self.sp_atk, self.sp_def, self.speed, self.legendary, self.type1, self.type2, self.gen]
                #       0         1         2         3         4             5            6             7          8             9            10             11        12

    def __repr__(self):
        return "You found a level {} {} that has {} total hp, {} attack, {} defense, {} special attack, {} special defense and {} speed.".format(self.lvl, self.name, self.hp, self.attack, self.defense, self.sp_atk, self.sp_def, self.speed)

    def get_pkm(self):
        return self.pkm
    
    # def update_hp(self, lvl):
        # will update the total hp of the Pokemon object
    
    # def update_stat(self. lvl)
        # will run a loop in range(5,10)
            # calling gen_stat with the index of the range to generate the stats
            # updating each stat of the Pokemon object







#############################################################################################################################################
# Trainer Class

class Trainer:
    def __init__(self, t_name):
        self.t_name = t_name
        self.team = []
            # team is a list consisint in the pkm list data, it's creted in the initialization of a Pokemon        
        # self.t_id = randint(0,99999) id's are for the future discord bot project
        self.bank = []
            # bank (will be a dict) is the player's personal Pokemon Storage, it'll hold as a key the pokemon object itself
            # and the value will be the pokemon.pkm final stats list
    
    
    def get_name(self):
        # getter for the trainer name
        return self.t_name
        
    def update_team(self, pkm):
        """This funtion will add the 'caught' pokemon to the team
        or send the pokemon to the pc if the party is full

        Args:
            pokemon (list): Caught pokemon to be added

        Returns:
            str: Telling the player if the pokemon was added to the party or sent to the pc
        """            
        if len(self.team) == 6:
            # if the party is full (6 Pokemons) the functiol will call the store_pokemon function
            # that will store the created pokemon in the bnak.
            
            self.store_pokemon(pkm)
            # this has to be updated acording to the new changes in the bank/pokemon objects
            return "You already have 6 Pokemon in your team! Pokemon sent to the pc"

        else:
            # this will curently just adds the pkm data to the team lis.
            self.team.append(pkm)
            # this has to be updated acording to the new changes in the bank/pokemon objects
            return "Level {}, {} Has been added to your party".format(pkm[2], pkm[1])
     
    def store_pokemon(self, pkm):
        """ Storing the pokemon in the bank.
            adds the specified 'Pokemon' to tha bank and removes from the party/
        Args:
            pkm (list): Pokemon 'Final' data.

        Returns:
            string
        """
        # has to be changed to store the objects so them
        self.bank.append(pkm)
        self.team.remove(pkm)
        print("The level {}, {}, was added to the Pokemon Bank!".format(pkm[2], pkm[1]))
        return "The level {}, {}, was added to the Pokemon Bank!".format(pkm[2], pkm[1])
                
    def withdraw(self, slot):
        try:
            pkm = self.bank[slot]
            print("The level {}, {}, was added to your party!".format(pkm[2],pkm[1]))
            self.team.append(pkm)
            self.bank.remove(pkm)
        except:
            print("Invalid slot")
        return
                
    def get_bank(self):
        """Printing the bank current status

        Returns:
            Every Pokemon present in the bank
        """
        # if the bank is empty there's nothing to be returned nor printed
        if len(self.bank) == 0:
            return "Your bank is empty"
        # iterating throught the bank in order to print out wich pokemon and at which index it sits on
        for i in self.bank:
                                                 # i[2] == lvl - i[1] == pokemon name
            print("Level {}, {}, At slot {}".format(i[2], i[1], self.bank.index(i)))
        return "Thansk for checking the bank"

    def encounter(self):
        """Rolls the pokemon encounter and a lorefrieldyish lvl

        Returns:
            list: id of the pokemon and its level
        """
        # rolling the pokemon
        pk_id = randint(1,721)
        
        # just checking if "Legendary" flag is true so the level can be more "accurate"
        if dex_dict[pk_id][11] == 'True':
            level = 70
            # this part needs a bit of work and some changes in the source data are needed
            # in order to account for mythic pokemon and set them at the lvl 50    
        else:
            # rolling the level
            level_multip = randint(1,1000)
            # how high the roll is the higher the level will be
            lower_level = 1 if level_multip <= 550 else 25 if level_multip > 550 and level_multip <= 900 else 45
            # having a lower/high level variables allow for more "natural" levels.
                # further development will take in account evolving levels for the wild encounters.
            upper_level = 30 if level_multip <= 550 else 50 if level_multip > 550 and level_multip <= 900 else 70
            level = randint(lower_level, upper_level)
                # the level will always be a random int between the lower and upper bounds.
        return Pokemon(pk_id, level)

    def catch(self):
        # Catching part
        pokemon = self.encounter()
            # Creating the pokemon object
        pkm = pokemon.get_pkm()
            # getting the actual stat's of the pokemon
        print(pokemon)
            # __repr__ pokemon printing
        print()
        catch_rate = 70
            # 70 means that every roll from 1-100 will have 30 success chances (30% catch rate)
        if pkm[9] == True:
            # Unless the legendary flag is True, then you have only 5% chance
            catch_rate = 95
        catch_roll = 0
            # Keeping count of how many 'tries' it took to catch the pokemon
        inputs = ["r", "g"]
            # Valid input list in order to keep the user from sending invalid inputs
        count = 1
        #delay = 1
            # Delay in the catching will be present in the next versions
        print("You threw a Pokeball")
        print()
        catch_roll = randint(1,100)
            # doing the actual roll for the catch
        while catch_roll <= catch_rate:
            # if the catch_roll is smaller than the catch_rate the catch will fail
            print("Beep, Beep. The Pokemon broke free.")
            print()
                # Failing the catch will ask for the user whether he wants to keep trying or to give up 
            user = input("Press 'r' to retry or 'g' to give up. ")
            if user not in inputs:
                # if the input was invalid this will lock the user into sending a valid input
                while user not in inputs:
                    print()
                    # Again prompting the valid choices
                    print("Press 'r' to retry or 'g' to give up. ")
                    user = input()
                    if user in inputs:
                        # if a right input was given the loop will break
                        break
                        
            if user == "r":
                # This will retry the catch.
                print()
                print("You threw a Pokeball")
                print()
                catch_roll = randint(1,100)
                count += 1
                    # Keeping the tries count
            if user == "g":
                # the user has given up, prompting how many tries it took to give up on chaching the pokemon.
                print("You gave up on catching a level {}, {}, after {} tries".format(pkm[2], pkm[1], count))
                return 

        print("Beep, Beep, Beep.")
        # if the pokemon was caught the program will congratulate the user and again show the pokemon and how many tries it took.
        print("Contratulations {}! You caught a level {}, {} in {} tries".format(self.t_name, pkm[2], pkm[1], count))
        print("*"* 120)
        return pkm

    def __repr__(self):
        # print(player_object) will prompt the trainer name and how many pokemons are in the party.
        # This will be changed in the future for a more 'immersive' line for the future discord iterations.
        return "Hello! My name is {} and I have {} Pokemons on my team".format(self.t_name, len(self.team))
    
    def get_team(self):
        # getter function to print out each pokemon present in the party.
        for i in self.team:
            print("Level {}, {}.".format(i[2], i[1]))
        return "You have {} Pokemons in your party".format(len(self.team))
    
    
    # def get_stats(self):
        # this will be a getter for the complete stat list in a readable way
    
#############################################################################################################################################
# Playing functions below   

def Play():
    player = input("Hello Trainer, What is your name? ")
    player = Trainer(player)
    print()
    print("Hello {}".format(player.get_name()))
    
    while True:
        print()
        print("Type 'search' search for a Pokemon, 'team' to view your team, 'bank' to access your Poke Bank. OR 'q' TO QUIT.")
        usr = input()
        print()
        print("*"* 120)
        if usr ==  "q":
            pokecount = len(player.bank) + len(player.team)
            if pokecount > 0:
                print("Congratulations {}! You caught {} Pokemons while playing this game!".format(player.get_name(), pokecount))
            return "Goodbye!"
        elif usr == 't' or usr == 'team':
            if len(player.team) != 0:
                print(player.get_team())
            else:
                print("Your team is empty!")
                usr = ""
                continue
        elif usr == 's' or usr == 'search':
            try:
                player.update_team(player.catch())
            except:
                print("*"* 120)
                usr = ""
                continue
        elif usr == 'bank' or usr == 'b':
            if len(player.team) > 0 and len(player.bank) > 0:
                print()
                print(bank(player))
                print()
            elif len(player.team) == 1 and len(player.bank) == 0:
                print("Please catch another Pokemon!")
            else:
                print("Please catch a Pokemon before using the bank!")
        else:
            print("Sorry, try again!")
        
        
def bank(player):
    """This is the main funcion that in which the user interacts with the bank

    Args:
        player (object): It's called by the main game function

    Returns:
        str: 'Thanks for using the bank!' :o
    """    
    # valid input list to avoid errors
    inputs = ["withdraw","store", "q", 's', 'w']

    print(player.get_bank())
        # calling the get_bank function in order to show the user the stored
        # pokemons and their indexes, so withdrawing is easier.
    print("""
    Type 'withdraw' to Withdraw a Pokemon from the bank.
    Type 'store' to Store a pokemon in the bank.
    If you would like to quit the bank type 'q'.""")
    print()
        # Asking for the user inputs.
    usr = input()
    
    while usr not in inputs:
        # Looping the user into giving a valid input
            print("""
                Type 'withdraw' to Withdraw a Pokemon from the bank.
                Type 'store' to Store a pokemon in the bank.
                If you would like to quit the bank type 'q'.""")
            print()
            usr = input()
    if usr == 'q':
        # 'q' means the user wats to quit the bank so it'll throw him out of this funcion and back into the main game
        print()
        return "Thanks for using the Pokemon Bank!"
    elif usr == 'store' or usr == 's':
        # If the user want's to store a pokemon he needs to have more than 1 pokemon in his party.
        # How the player will walk in tall grass without a pokemon ?????
        if len(player.team) > 1:
            # If he has then it'll call the store funcion using the player object as argument
            store(player)
                # The store helper function will handle the inputs for storing the desired pokemon
            # Then quit the bank
            return "Thanks for using the Pokemon Bank!"
        else:
            print()
            # Not having more than 1 pokemon in the party will result in the bank kicking the user out.
            return "You can't be left with no Pokemons. Thanks for using the Pokemon Bank!"
    elif usr == 'withdraw' or usr == 'w':
        # *** Withdraw is likely to get a separete helper function like store so more than 1 pokemons can be withdrawn.
        # You can't withdraw something that doesen't exist, so if theres no pokemons in the bank
        # the user will get kicked out:
        if len(player.bank) > 0 and len(player.team) < 6:
            print("Please type the slot from which you would like to withdraw the Pokemon")
            try:
                # This will try to check if the input sent from the user is valid.
                slot = int(input())
                    # slot it's the place where the pokemon is on the bank
            except:
                # Needs rework but it's a function for calling out the user for inputing somethin invalid.
                print("PLEASE TYPE A NUMBER!")
                slot = int(input())
            while slot < 0 or slot > len(player.bank):
                # Again holding the user into sending a valid input.
                print("Please type the slot from which you would like to withdraw the Pokemon")
                try:
                    # This will try to check if the input sent from the user is valid.
                    slot = int(input())
                except:
                    print("PLEASE TYPE A NUMBER!")
                        # Needs rework but it's a function for calling out the user for inputing somethin invalid.
                    slot = int(input())
            # This will finally withdraw the specified Pokemon from the bank in the withdraw helper add this pokemon
            # to the user's party.
            player.withdraw(slot)
            return "Thanks for using the Pokemon Bank!"
        else:
            if len(player.team) == 6:
                return ("You aleady have 6 Pokemons in your party, please store one if you'd like to withdraw a Pokemon.")
            return("Your Bank is empty! Thanks for using the Pokemon Bank!")

   
def store(player):
    """Storing the pokemon is a bit trickier than withdrawing it.
    So in order to accomplish evereything this funcion will coordinate with
    the storing function present in the 'Trainer' Class.

    * This will be updated to allow multiple pokemons to be stored at the same time
    Args:
        player (object): It's used in order to access the functions inside the class.

    Returns back to the bank and then back to the main game.
    """    
    inputs = []
    # Iterating through the team in order to present the Pokemons that the user can store.
    for i in player.team:
        # Letting the user know each pokemon presnt in the party and the its position in order to store.
        print("You have a level {}, {}, in your slot {}".format(i[2], i[1], player.team.index(i)))
        inputs.append(player.team.index(i))
            # Creating the valid input's list so the user can't trigger a index error
    print("Please type which slot in your party corresponds to the Pokemon you'd like to store.")
    try:
        # This will again lock the user into sending a valid input
        usr = int(input())
    except:
        print("PLEASE TYPE A NUMBER!")
        usr = int(input())
    while usr not in inputs:
        # Looping the user into sending a valid input.
        print("Please type which slot in your party corresponds to the Pokemon you'd like to store.")
        try:
            usr = int(input())
        except:
            print("PLEASE TYPE A NUMBER!")
            usr = int(input())
        continue
        # Now that the input is valid call the Trainer class helper function to store the pokemon at that index.
    player.store_pokemon(player.team[usr])
    return "Thanks for using the bank!"
        # going back to the bank then back to the main game.


print(Play())
    # Playing :D
 
 
 
 