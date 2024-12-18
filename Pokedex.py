# %% imports
import random
# %% intentinal game design
On = True
# %% Pokedex and player inventory
pokedex = ["Carbink"]
party = ["Carbink"]
box = []
sent_out = ["Carbink"]
# %% Encounter function
def encounters(turn,did_catch,encounter_choices,did_flee,catch_chance,PartyChange,crit_catch,shiny_chance,buyoptions,fleesuccess,money,inshop,purchases):
    Pokeballs = 10
    money = 1000
    ## makes the encounters infinate
    while On == True:
        inshop = True
        purchases = 0
        print("You found a shop! Do you want to buy anything? You can also check your pokedex")
        while inshop == True and purchases <= 6:
            print("You have " + str(money) + " money and " + str(Pokeballs) + " pokeballs")
            print("Stock: (₽10)Pokeball, ")
            buyoptions = input("What do you buy?(1 for the first option, 2 for the second, etc... (press L or l to leave the shop, or press p or P to check pokedex, you may only but up to 7 items)) ")
            if buyoptions == "1" and money >= 10:
                money -= 10
                Pokeballs += 1
                purchases += 1
                print("Pokeballs: " + str(Pokeballs))
            elif buyoptions == "p" or buyoptions == "P":
                print(pokedex)
            elif buyoptions == "1" and money < 10:
                print("You dont have enough money!")
            elif buyoptions == "l" or buyoptions == "L":
                inshop = False
                print("On to adventure!")
            else:
                print("Please type one of the options")
        Encounter = random.randint(1,6)
        if Encounter == 1 or Encounter == 2 or Encounter == 3:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Bulbasaur!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Bulbasaur! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,2)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Bulbasaur(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Bulbasaur(shiny)")
                            else:
                                box.append("Bulbasaur(shiny)")
                        else:
                            pokedex.append("Bulbasaur(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Bulbasaur(shiny)")
                            else:
                                box.append("Bulbasaur(shiny)")
                    elif catch_chance == 2 and shiny_chance == 1000:
                        print("Bulbasaur was caught! (This pokemon looks a little different)")
                        if "Bulbasaur(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Bulbasaur(shiny)")
                            else:
                                box.append("Bulbasaur(shiny)")
                        else:
                            pokedex.append("Bulbasaur(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Bulbasaur(shiny)")
                            else:
                                box.append("Bulbasaur(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Bulbasaur" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Bulbasaur")
                            else:
                                box.append("Bulbasaur")
                        else:
                            pokedex.append("Bulbasaur")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Bulbasaur")
                            else:
                                box.append("Bulbasaur")
                    elif catch_chance == 2:
                        print("Bulbasaur was caught!")
                        if "Bulbasaur" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Bulbasaur")
                            else:
                                box.append("Bulbasaur")
                        else:
                            pokedex.append("Bulbasaur")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Bulbasaur")
                            else:
                                box.append("Bulbasaur")
                    else:
                        print("Bwoop, Bwoop, Bang! Bulbasaur broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")
            else:
                print("The pokemon saw a moment to react and fled...")
        ## All over again...
        elif Encounter == 4 or Encounter == 5:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Ivysaur!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Ivysaur! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,4)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Ivysaur(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Ivysaur(shiny)")
                            else:
                                box.append("Ivysaur(shiny)")
                        else:
                            pokedex.append("Ivysaur(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Ivysaur(shiny)")
                            else:
                                box.append("Ivysaur(shiny)")
                    elif catch_chance == 4 and shiny_chance == 1000:
                        print("Ivysaur was caught! (This pokemon looks a little different)")
                        if "Ivysaur(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Ivysaur(shiny)")
                            else:
                                box.append("Ivysaur(shiny)")
                        else:
                            pokedex.append("Ivysaur(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Ivysaur(shiny)")
                            else:
                                box.append("Ivysaur(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Ivysaur" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Ivysaur")
                            else:
                                box.append("Ivysaur")
                        else:
                            pokedex.append("Ivysaur")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Ivysaur")
                            else:
                                box.append("Ivysaur")
                    elif catch_chance == 4:
                        print("Ivysaur was caught!")
                        if "Ivysaur" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Ivysaur")
                            else:
                                box.append("Ivysaur")
                        else:
                            pokedex.append("Ivysaur")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Ivysaur")
                            else:
                                box.append("Ivysaur")
                    else:
                        print("Bwoop, Bwoop, Bang! Ivysaur broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")  
            else:
                print("The pokemon saw a moment to react and fled...")
## And again...
        elif Encounter == 6:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Venusaur!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Venusaur! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,6)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Venusaur(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Venusaur(shiny)")
                            else:
                                box.append("Venusaur(shiny)")
                        else:
                            pokedex.append("Venusaur(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Venusaur(shiny)")
                            else:
                                box.append("Venusaur(shiny)")
                    elif catch_chance == 6 and shiny_chance == 1000:
                        print("Venusaur was caught! (This pokemon looks a little different)")
                        if "Venusaur(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Venusaur(shiny)")
                            else:
                                box.append("Venusaur(shiny)")
                        else:
                            pokedex.append("Venusaur(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Venusaur(shiny)")
                            else:
                                box.append("Venusaur(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Venusaur" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Venusaur")
                            else:
                                box.append("Venusaur")
                        else:
                            pokedex.append("Venusaur")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Venusaur")
                            else:
                                box.append("Venusaur")
                    elif catch_chance == 6:
                        print("Venusaur was caught!")
                        if "Venusaur" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Venusaur")
                            else:
                                box.append("Venusaur")
                        else:
                            pokedex.append("Venusaur")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Venusaur")
                            else:
                                box.append("Venusaur")
                    else:
                        print("Bwoop, Bwoop, Bang! Venusaur broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")
            else:
                print("The pokemon saw a moment to react and fled...")
        if Encounter == 7 or Encounter == 8 or Encounter == 9:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Charmander!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Charmander! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,2)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Charmander(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmander(shiny)")
                            else:
                                box.append("Charmander(shiny)")
                        else:
                            pokedex.append("Charmander(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmander(shiny)")
                            else:
                                box.append("Charmander(shiny)")
                    elif catch_chance == 2 and shiny_chance == 1000:
                        print("Charmander was caught! (This pokemon looks a little different)")
                        if "Charmander(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmander(shiny)")
                            else:
                                box.append("Charmander(shiny)")
                        else:
                            pokedex.append("Charmander(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmander(shiny)")
                            else:
                                box.append("Charmander(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Charmander" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmander")
                            else:
                                box.append("Charmander")
                        else:
                            pokedex.append("Charmander")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmander")
                            else:
                                box.append("Charmander")
                    elif catch_chance == 2:
                        print("Charmander was caught!")
                        if "Charmander" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmander")
                            else:
                                box.append("Charmander")
                        else:
                            pokedex.append("Charmander")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmander")
                            else:
                                box.append("Charmander")
                    else:
                        print("Bwoop, Bwoop, Bang! Charmander broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")
            else:
                print("The pokemon saw a moment to react and fled...")
        ## All over again...
        elif Encounter == 10 or Encounter == 11:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Charmeleon!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Charmeleon! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,4)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Charmeleon(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmeleon(shiny)")
                            else:
                                box.append("Charmeleon(shiny)")
                        else:
                            pokedex.append("Charmeleon(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmeleon(shiny)")
                            else:
                                box.append("Charmeleon(shiny)")
                    elif catch_chance == 4 and shiny_chance == 1000:
                        print("Charmeleon was caught! (This pokemon looks a little different)")
                        if "Charmeleon(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmeleon(shiny)")
                            else:
                                box.append("Charmeleon(shiny)")
                        else:
                            pokedex.append("Charmeleon(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmeleon(shiny)")
                            else:
                                box.append("Charmeleon(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Charmeleon" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmeleon")
                            else:
                                box.append("Charmeleon")
                        else:
                            pokedex.append("Charmeleon")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmeleon")
                            else:
                                box.append("Charmeleon")
                    elif catch_chance == 4:
                        print("Charmeleon was caught!")
                        if "Charmeleon" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmeleon")
                            else:
                                box.append("Charmeleon")
                        else:
                            pokedex.append("Charmeleon")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charmeleon")
                            else:
                                box.append("Charmeleon")
                    else:
                        print("Bwoop, Bwoop, Bang! Charmeleon broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")  
            else:
                print("The pokemon saw a moment to react and fled...")
## And again...
        elif Encounter == 12:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Charizard!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Charizard! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,6)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Charizard(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charizard(shiny)")
                            else:
                                box.append("Charizard(shiny)")
                        else:
                            pokedex.append("Charizard(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charizard(shiny)")
                            else:
                                box.append("Charizard(shiny)")
                    elif catch_chance == 6 and shiny_chance == 1000:
                        print("Charizard was caught! (This pokemon looks a little different)")
                        if "Charizard(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charizard(shiny)")
                            else:
                                box.append("Charizard(shiny)")
                        else:
                            pokedex.append("Charizard(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charizard(shiny)")
                            else:
                                box.append("Charizard(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Charizard" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charizard")
                            else:
                                box.append("Charizard")
                        else:
                            pokedex.append("Charizard")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charizard")
                            else:
                                box.append("Charizard")
                    elif catch_chance == 6:
                        print("Charizard was caught!")
                        if "Charizard" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charizard")
                            else:
                                box.append("Charizard")
                        else:
                            pokedex.append("Charizard")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Charizard")
                            else:
                                box.append("Charizard")
                    else:
                        print("Bwoop, Bwoop, Bang! Charizard broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")
            else:
                print("The pokemon saw a moment to react and fled...")
        if Encounter == 13 or Encounter == 14 or Encounter == 15:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Squirtle!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Squirtle! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,2)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Squirtle(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Squirtle(shiny)")
                            else:
                                box.append("Squirtle(shiny)")
                        else:
                            pokedex.append("Squirtle(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Squirtle(shiny)")
                            else:
                                box.append("Squirtle(shiny)")
                    elif catch_chance == 2 and shiny_chance == 1000:
                        print("Squirtle was caught! (This pokemon looks a little different)")
                        if "Squirtle(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Squirtle(shiny)")
                            else:
                                box.append("Squirtle(shiny)")
                        else:
                            pokedex.append("Squirtle(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Squirtle(shiny)")
                            else:
                                box.append("Squirtle(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Squirtle" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Squirtle")
                            else:
                                box.append("Squirtle")
                        else:
                            pokedex.append("Squirtle")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Squirtle")
                            else:
                                box.append("Squirtle")
                    elif catch_chance == 2:
                        print("Squirtle was caught!")
                        if "Squirtle" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Squirtle")
                            else:
                                box.append("Squirtle")
                        else:
                            pokedex.append("Squirtle")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Squirtle")
                            else:
                                box.append("Squirtle")
                    else:
                        print("Bwoop, Bwoop, Bang! Squirtle broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")
            else:
                print("The pokemon saw a moment to react and fled...")
        ## All over again...
        elif Encounter == 16 or Encounter == 17:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Wartortle!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Wartortle! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,4)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Wartortle(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Wartortle(shiny)")
                            else:
                                box.append("Wartortle(shiny)")
                        else:
                            pokedex.append("Wartortle(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Wartortle(shiny)")
                            else:
                                box.append("Wartortle(shiny)")
                    elif catch_chance == 4 and shiny_chance == 1000:
                        print("Wartortle was caught! (This pokemon looks a little different)")
                        if "Wartortle(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Wartortle(shiny)")
                            else:
                                box.append("Wartortle(shiny)")
                        else:
                            pokedex.append("Wartortle(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Wartortle(shiny)")
                            else:
                                box.append("Wartortle(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Wartortle" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Wartortle")
                            else:
                                box.append("Wartortle")
                        else:
                            pokedex.append("Wartortle")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Wartortle")
                            else:
                                box.append("Wartortle")
                    elif catch_chance == 4:
                        print("Wartortle was caught!")
                        if "Wartortle" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Wartortle")
                            else:
                                box.append("Wartortle")
                        else:
                            pokedex.append("Wartortle")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Wartortle")
                            else:
                                box.append("Wartortle")
                    else:
                        print("Bwoop, Bwoop, Bang! Wartortle broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")  
            else:
                print("The pokemon saw a moment to react and fled...")
## And again...
        elif Encounter == 18:
            print(sent_out[0] + " Was sent out!")
            turn = 0
            did_catch = False
            did_flee = False
            print("You encountered Blastoise!")
            while turn <= 5 and did_catch == False and did_flee == False:
                turn += 1
                print("Pokeballs: " + str(Pokeballs))
                if turn == 1:
                    encounter_choices = input("What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                else:
                    encounter_choices = input("It's still Blastoise! What will you do? (1) Throw pokeball, (2) Change pokemon, (3) Try to flee: ")
                if encounter_choices == "1" and Pokeballs >= 1:
                    Pokeballs -= 1
                    crit_catch = random.randint(1,100)
                    catch_chance = random.randint(1,6)
                    shiny_chance = random.randint(1,1000)
                    ## checks crit catch, shiny chance, etc...
                    if crit_catch == 100 and shiny_chance == 1000:
                        print("CRITICAL CATCH!!! (This pokemon looks a little different)")
                        if "Blastoise(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Blastoise(shiny)")
                            else:
                                box.append("Blastoise(shiny)")
                        else:
                            pokedex.append("Blastoise(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Blastoise(shiny)")
                            else:
                                box.append("Blastoise(shiny)")
                    elif catch_chance == 6 and shiny_chance == 1000:
                        print("Blastoise was caught! (This pokemon looks a little different)")
                        if "Blastoise(shiny)" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Blastoise(shiny)")
                            else:
                                box.append("Blastoise(shiny)")
                        else:
                            pokedex.append("Blastoise(shiny)")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Blastoise(shiny)")
                            else:
                                box.append("Blastoise(shiny)")
                    elif crit_catch == 100:
                        print("CRITICAL CATCH!!!")
                        if "Blastoise" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Blastoise")
                            else:
                                box.append("Blastoise")
                        else:
                            pokedex.append("Blastoise")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Blastoise")
                            else:
                                box.append("Blastoise")
                    elif catch_chance == 6:
                        print("Blastoise was caught!")
                        if "Blastoise" in pokedex:
                            did_catch = True
                            if len(party) < 6:
                                party.append("Blastoise")
                            else:
                                box.append("Blastoise")
                        else:
                            pokedex.append("Blastoise")
                            did_catch = True
                            if len(party) < 6:
                                party.append("Blastoise")
                            else:
                                box.append("Blastoise")
                    else:
                        print("Bwoop, Bwoop, Bang! Blastoise broke free!")
                elif encounter_choices == "1" and Pokeballs <= 0:
                    print("No pokeballs left!")
                    did_flee = True
                elif encounter_choices == "2":
                    print(party)
                    PartyChange = input("Type the number of the party member to send out, 1 for the first, 2 for the second, etc... BUT anything other than 1, 2, 3, 4, or 5 will send out the 6th party member: ")
                    if PartyChange == "1":
                        sent_out.insert(0, party[0])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "2":
                        sent_out.insert(0, party[1])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "3":
                        sent_out.insert(0, party[2])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "4":
                        sent_out.insert(0, party[3])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    elif PartyChange == "5":
                        sent_out.insert(0, party[4])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                    else:
                        sent_out.insert(0, party[5])
                        del sent_out[1]
                        print("You sent out: " + sent_out[0])
                elif encounter_choices == 3:
                    fleesuccess = random.randint(1,2)
                    if fleesuccess == 1:
                        print("You fled the battle!")
                        did_flee = True
                        turn = 6
                    else:
                        print("You failed to flee...")
                else:
                    print("Please type one of the options")
                    turn -= 1
            if did_catch == True:
                print("On to the next battle!")
            else:
                print("The pokemon saw a moment to react and fled...")
        else:
            print("Good job, the game broke")
# %% Function calling
turn = 0
did_catch = False
encounter_choices = 0
did_flee = False
catch_chance = 5
PartyChange = -1
crit_catch = 100
shiny_chance = 1000
buyoptions = 0
fleesuccess = 1
money = 1000
inshop = False
purchases = 0
encounters(turn,did_catch,encounter_choices,did_flee,catch_chance,PartyChange,crit_catch,shiny_chance,buyoptions,fleesuccess,money,inshop,purchases)