from gc import get_stats
from random import *
from dex import dex_dict

       
    
class Pokemon:
    
    def gen_hp(self, lvl, base):
        """This funcion will be called when the encounter is generated.

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
        """This funcion will be called when the encounter is generated.

        Args:
            lvl (int): Pokemons level
            base (int): stat multiplier

        Returns:
            int: returns
        """
        base = int(base)            
        stat = (((2*base)*lvl)//100)+5
        return stat



    def __init__(self, id, lvl):
    # base_stats
    #(id, name, type1, type2=None, total, hp, attack, defense, sp_atk, sp_def, speed, gen, legendary)
    #  0    1     2        3         4     5    6        7        8       9      10    11       12     
        self.id = id
        self.lvl = lvl
        base_stats = dex_dict.get(id)
        self.name = base_stats[0]
        self.type1 = base_stats[1]
        self.type2 = base_stats[2]
        self.total = base_stats[3]
        self.hp = self.gen_hp(lvl, base_stats[4])
        self.attack = self.gen_stat(lvl, base_stats[5])
        self.defense = self.gen_stat(lvl, base_stats[6])
        self.sp_atk = self.gen_stat(lvl, base_stats[7])
        self.sp_def = self.gen_stat(lvl, base_stats[8])
        self.speed = self.gen_stat(lvl, base_stats[9])
        self.gen = base_stats[10]
        self.legendary = base_stats[11]
        self.pkm = [self.id, self.name, self.lvl, self.hp, self.attack, self.defense, self.sp_atk, self.sp_def, self.speed, self.legendary, self.type1, self.type2, self.gen]
                #       0         1         2         3         4             5            6             7          8             9            10             11        12

    def __repr__(self):
        return "You found a level {} {} that has {} total hp, {} attack, {} defense, {} special attack, {} special defense and {} speed.".format(self.lvl, self.name, self.hp, self.attack, self.defense, self.sp_atk, self.sp_def, self.speed)

    def get_pkm(self):
        return self.pkm
    

class Trainer:
    def __init__(self, t_name):
        self.t_name = t_name
        self.team = []
        # self.t_id = randint(0,99999) id's are for the future
        self.bank = []
    
    def get_name(self):
        return self.t_name
        
    def update_team(self, pkm):
        """This funtion will add the caught pokemon to the team
        or send the pokemon to the pc if the party is full

        Args:
            pokemon (list): Caught pokemon to be added

        Returns:
            str: Telling the player if the pokemon was added to the party or sent to the pc
        """            
        if len(self.team) == 6:
            self.store_pokemon(pkm)
            return "You already have 6 Pokemon in your team! Pokemon sent to the pc"

        else:
            self.team.append(pkm)
            return "Level {}, {} Has been added to your party".format(pkm[2], pkm[1])
     
    def store_pokemon(self, pkm):
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
        if len(self.bank) == 0:
            return "Your bank is empty"
        for i in self.bank:
            print("Level {}, {}, At slot {}".format(i[2], i[1], self.bank.index(i)))
        return "Thansk for checking the bank"

    def encounter(self):
        """Rolls the pokemon encounter and a lorefrieldyish lvl

        Returns:
            list: id of the pokemon and its level
        """
        pk_id = randint(1,721)
        
        pkm = dex_dict[pk_id]
        if pkm[11] == 'True':
            level = 70
        else:
            level_multip = randint(1,1000)
            lower_level = 1 if level_multip <= 550 else 25 if level_multip > 550 and level_multip <= 900 else 45
            upper_level = 30 if level_multip <= 550 else 50 if level_multip > 550 and level_multip <= 900 else 70
            level = randint(lower_level, upper_level)
        return Pokemon(pk_id, level)

    def catch(self):
        pokemon = self.encounter()
        pkm = pokemon.get_pkm()
        print(pokemon)
        print()
        catch_rate = 69
        if pkm[9] == True:
            catch_rate = 95
        catch_roll = 0
        inputs = ["r", "g"]
        count = 1
        delay = 1
        print("You threw a Pokeball")
        print()
        catch_roll = randint(1,100)
        while catch_roll < catch_rate:
            print("Beep, Beep. The Pokemon broke free.")
            print()
            user = input("Press 'r' to retry or 'g' to give up. ")
            if user not in inputs:
                while user not in inputs:
                    print()
                    print("Press 'r' to retry or 'g' to give up. ")
                    user = input()
                    if user in inputs:
                        break
                        
            if user == "r":
                print()
                print("You threw a Pokeball")
                print()
                catch_roll = randint(1,100)
                count += 1
            if user == "g":
                print("You gave up on catching a level {}, {}, after {} tries".format(pkm[2], pkm[1], count))
                return 

        print("Beep, Beep, Beep.")
        print("Contratulations {}! You caught a level {}, {} in {} tries".format(self.t_name, pkm[2], pkm[1], count))
        print("*"* 120)
        return pkm

    def __repr__(self):
        return "Hello! My name is {} and I have {} Pokemons on my team".format(self.t_name, len(self.team))
    
    def get_team(self):
        for i in self.team:
            print("Level {}, {}.".format(i[2], i[1]))
        return "You have {} Pokemons in your party".format(len(self.team))
    

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
    inputs = ["withdraw","store", "q", 's', 'w']
    print(player.get_bank())
    print("""
    Type 'withdraw' to Withdraw a Pokemon from the bank.
    Type 'store' to Store a pokemon in the bank.
    If you would like to quit the bank type 'q'.""")
    print()
    usr = input()
    while usr not in inputs:
            print("""
                Type 'withdraw' to Withdraw a Pokemon from the bank.
                Type 'store' to Store a pokemon in the bank.
                If you would like to quit the bank type 'q'.""")
            print()
            usr = input()
    if usr == 'q':
        print()
        return "Thanks for using the Pokemon Bank!"
    elif usr == 'store' or usr == 's':
        if len(player.team) > 1:
            store(player)
            return "Thanks for using the Pokemon Bank!"
        else:
            print()
            return "You can't be left with no Pokemons. Thanks for using the Pokemon Bank!"
    elif usr == 'withdraw' or usr == 'w':
        if len(player.bank) > 0:
            print("Please type the slot from which you would like to withdraw the Pokemon")
            try:
                slot = int(input())
            except:
                print("PLEASE TYPE A NUMBER!")
                slot = int(input())
            while slot < 0 or slot > len(player.bank):
                print("Please type the slot from which you would like to withdraw the Pokemon")
                try:
                    slot = int(input())
                except:
                    print("PLEASE TYPE A NUMBER!")
                    slot = int(input())
            if len(player.team) < 6:
                player.withdraw(slot)
                return "Thanks for using the Pokemon Bank!"
            else:
                print()
                return "Your party is full! Thansk for using the Pokemon Bank!"
        else:
            return("Your Bank is empty! Thanks for using the Pokemon Bank!")

   
def store(player):
    inputs = []
    for i in player.team:
        print("You have a level {}, {}, in your slot {}".format(i[2], i[1], player.team.index(i)))
        inputs.append(player.team.index(i))
    print("Please type which slot in your party corresponds to the Pokemon you'd like to store.")
    try:
        usr = int(input())
    except:
        print("PLEASE TYPE A NUMBER!")
        usr = int(input())
    while usr not in inputs:
        print("Please type which slot in your party corresponds to the Pokemon you'd like to store.")
        try:
            usr = int(input())
        except:
            print("PLEASE TYPE A NUMBER!")
            usr = int(input())
        continue
    player.store_pokemon(player.team[usr])
    return "Thanks for using the bank!"


print(Play())
 
 
 
 