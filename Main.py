#Idris Sampson
#4/16/24
#main function the begging of the end for our fearless acheologist
#get player input and desired race of choice made by idris

print('You are a fearless archaeologist who begins his adventure  with his friends by venturing to Egypt to enter the tomb of King Ramesses.')
player = input("what is your name:")
race = input("choose race are you White or Black:")

while True:
    if race.lower() == 'white':
        print("You and your friends Stephanie and Todd bust open the door to the tomb, as you guys fully open the tomb a huge gust of wind carrying a  ton of sand and dust"'\n'"comes flying out from the inside of the tomb, and from the bowels of it you hear “Turn back now or face my curse” *in an echoing taunt*"'\n'"Despite the clear warnings you provide because you know what you could gain if you successfully tomb taker this a flood of wealth, fame and power will"'\n'"engulf your every being, so yall enter the tomb.")
        break
    elif race.lower() == 'black':
        print("You and your friends Jamar and Tyrone bust open the door to the tomb, as you guys fully open the tomb a huge gust of wind carrying a s**t ton of sand and"'\n'"dust comes flying out from the inside of the tomb, and from the bowels of it you hear “Turn back now or I will f**k you up” *in an echoing taunt*"'\n'"You, Jamal and Tyrone  turn to each other and stand there for a good 1 minutes contemplating the reason yall are here in complete silence,"'\n'"then Tyrone says “yeah nah man I aint messin this this s**t” you and Jamal agree, y'all take the quickest flight back home and never went to egypt again")
        quit()
    else:
        print("must be White or Black")
        race = input("what race are you White or Black:")
print("As you guys further deeper into the tomb Todd begins to get hesitant due to the creepy event unfloding such as creepy noises and huge spider and this isnt Australia and dashes to the exit like a titan from AOT with his hands flailing left and right.")
trick_rooni = input("Would you like to leave with him (yes or no)")
if trick_rooni == 'yes':
    print("You grab onto Stephanie’s arm and also begin to make a mad dash to the exit then the door suddenly shuts right infront Todd almost crushing him, These events are almost like the entity doesn't want y'all to leave.")
elif trick_rooni == 'no':
    print("As your narrarator I would have suggested running with Todd but now it is to late."'\n'"You decided not to run away with Todd so he was able to escape while you and Stephanie continued down the tomb."'\n'"Then yall remebered Todd had all the food so yall died")
    quit()

