name = input("Name: ")
title = input("Role: ")
activity = input("Activity: ")
emote = input("Emotion: ")
adj1 = input("Adjective: ")
celeb = input("Celebrity: ")
adj2 = input("Second Adjective: ")
business = input("Name of Business: ")
fcharacter = input("Fictional Character: ")
verb1 = input("Verb: ")
description = input("Descriptive Adjective: ")
com = input("Method of Communication: ")
desverb = input("Descriptive Verb: ")
pleasantry = input("Pleasantry: ")

madlib = f"Hello world! I am a {title}. I have a passion for {activity} and it makes people {emote}." \
         f" im sorry if that makes you {adj1}," \
         f" but i am who i am." \
         f" you know what? you remind me of someone...." \
         f" are you {celeb}?! that would be {adj2}, its very nice to meet you {name}"\
         f" So let get down to business. Welcome to your new job at {business}."\
         f" You will be work along side {fcharacter}. Don't {verb1} they are {description}"\
         f" If you should need anything feel free to contact me Via {com}"\
         f" I will do my best to be as {desverb} as I can {pleasantry}."

print(madlib)
