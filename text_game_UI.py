from tkinter import *

root = Tk()
root.title("Mysterious Island Adventure")
root.geometry('600x600')


global user_choice_1
global user_choice_2_left
global user_choice_2_right
global user_choice_3_left
global user_choice_3_right
global user_choice_4_left
global user_choice_4_right


def name_entry():
    name_label = Label(root, text="Welcome, brave adventurer! What is your name?")
    name_label.pack()
    global adventurer_name
    adventurer_name = Entry(root)
    adventurer_name.pack()
    name_submit_button = Button(root, text="Submit", command=age_entry)
    name_submit_button.pack()

def age_entry():
    age_label = Label(root, text="Greetings, " + adventurer_name.get() + "! How old are you?")
    age_label.pack()
    global adventurer_age
    adventurer_age = Entry(root)
    adventurer_age.pack()
    age_submit_button = Button(root, text="Submit", command=start_game)
    age_submit_button.pack()

def start_game():
    age_integer = int(adventurer_age.get())
    if age_integer >= 18:
        welcome_label = Label(root, text="Welcome to the Mysterious Island Adventure!")
        welcome_label.pack()

        start_button = Button(root, text="Begin Your Journey", command=first_encounter)
        start_button.pack()

    else:
        cant_play_label = Label(root, text="Sorry, you must be at least 18 years old to embark on this adventure.")
        cant_play_label.pack()

def first_encounter():
    game_line_1 = Label(root, text="As you step onto the island, you encounter a fork in the road.")
    game_line_1.pack()

    game_line_2 = Label(root, text="To the left, you see a dense forest with ancient trees towering overhead.")
    game_line_2.pack()

    game_line_3 = Label(root, text="To the right, a mysterious mist blankets a winding path.")
    game_line_3.pack()

    game_line_4 = Label(root, text="Which path will you choose?")
    game_line_4.pack()

    global user_choice_1
    user_choice_1 = Entry(root)
    user_choice_1.pack()

    choice_1_submit_button = Button(root, text="Submit", command=second_encounter)
    choice_1_submit_button.pack()

def second_encounter():
    chosen_path = user_choice_1.get()
    if chosen_path.lower() == "left":
        game_line_5 = Label(root, text="You venture into the dense forest, feeling the weight of ancient magic in the air.")
        game_line_5.pack()

        game_line_6 = Label(root, text="After walking for what feels like hours, you stumble upon an overgrown path.")
        game_line_6.pack()

        game_line_7 = Label(root, text="Will you 'Follow' the path or 'Forge' ahead through the underbrush?")
        game_line_7.pack()

        global user_choice_2_left
        user_choice_2_left = Entry(root)
        user_choice_2_left.pack()

        choice_2_submit_left = Button(root, text="Submit", command=third_encounter_left)
        choice_2_submit_left.pack()

    elif chosen_path.lower() == "right":
        game_line_8 = Label(root, text="You step onto the winding path, the mist swirling around you like whispers of the past.")
        game_line_8.pack()

        game_line_9 = Label(root, text="As you walk deeper into the mist, you hear faint whispers and glimpses of shadows.")
        game_line_9.pack()

        game_line_10 = Label(root, text="Do you 'Continue' forward, or 'Retreat' from the eerie mist?")
        game_line_10.pack()

        global user_choice_2_right
        user_choice_2_right = Entry(root)
        user_choice_2_right.pack()

        choice_2_submit_right = Button(root, text="Submit", command=third_encounter_right)
        choice_2_submit_right.pack()

def third_encounter_left():
    chosen_path = user_choice_2_left.get()
    if chosen_path.lower() == "follow":
        game_line_11 = Label(root, text="You follow the overgrown path, the trees parting to reveal a hidden glade.")
        game_line_11.pack()

        game_line_12 = Label(root, text="In the center of the glade, you spot an ancient shrine covered in moss.")
        game_line_12.pack()

        game_line_13 = Label(root, text="Will you 'Approach' the shrine or 'Explore' the surrounding area?")
        game_line_13.pack()

        global user_choice_3_left
        user_choice_3_left = Entry(root)  
        user_choice_3_left.pack()

        choice_3_submit_left = Button(root, text="Submit", command=fourth_encounter_left)
        choice_3_submit_left.pack()

    elif chosen_path.lower() == "forge":
        game_line_14 = Label(root, text="You push through the thick underbrush, feeling the weight of the forest closing in around you.")
        game_line_14.pack()

        game_line_15 = Label(root, text="After what feels like an eternity, you emerge into a small clearing.")
        game_line_15.pack()

        game_line_16 = Label(root, text="In the clearing, you find an old campfire surrounded by discarded belongings.")
        game_line_16.pack()

        game_line_17 = Label(root, text="Will you 'Search' the belongings or 'Rest' by the fire?")
        game_line_17.pack()

        user_choice_3_left = Entry(root)  
        user_choice_3_left.pack()

        choice_3_submit_left = Button(root, text="Submit", command=fourth_encounter_left)
        choice_3_submit_left.pack()



def third_encounter_right():
    chosen_action_right = user_choice_2_right.get()
    if chosen_action_right.lower() == "continue":
        game_line_18 = Label(root, text="You press on through the mist, determined to uncover its secrets.")
        game_line_18.pack()

        game_line_19 = Label(root, text="As you walk, the whispers grow louder, urging you to turn back.")
        game_line_19.pack()

        game_line_20 = Label(root, text="Do you 'Press On' despite the whispers, or 'Turn Back' to safety?")
        game_line_20.pack()

        global user_choice_3_right
        user_choice_3_right = Entry(root)
        user_choice_3_right.pack()

        choice_3_submit_right = Button(root, text="Submit", command=fourth_encounter_right)
        choice_3_submit_right.pack()

    elif chosen_action_right.lower() == "retreat":
        game_line_21 = Label(root, text="You decide to retreat from the eerie mist, your heart pounding with unease.")
        game_line_21.pack()

        game_line_22 = Label(root, text="As you turn back, the mist begins to recede, revealing a hidden path.")
        game_line_22.pack()

        game_line_23 = Label(root, text="Will you 'Follow' the newly revealed path, or 'Return' to the fork in the road?")
        game_line_23.pack()

        
        user_choice_3_right = Entry(root)
        user_choice_3_right.pack()

        choice_3_submit_right = Button(root, text="Submit", command=fourth_encounter_right)
        choice_3_submit_right.pack()

def fourth_encounter_left():
    chosen_action_left = user_choice_3_left.get()
    if chosen_action_left.lower() == "approach":
        game_line_24 = Label(root, text="You approach the ancient shrine, feeling a sense of reverence wash over you.")
        game_line_24.pack()

        game_line_25 = Label(root, text="As you draw near, the moss begins to glow, revealing hidden inscriptions.")
        game_line_25.pack()

        game_line_26 = Label(root, text="Will you 'Read' the inscriptions or 'Touch' the glowing moss?")
        game_line_26.pack()

        global user_choice_4_left
        user_choice_4_left = Entry(root)
        user_choice_4_left.pack()

        choice_4_submit_left = Button(root, text="Submit", command=fifth_encounter_left)
        choice_4_submit_left.pack()

    elif chosen_action_left.lower() == "explore":
        game_line_27 = Label(root, text="You explore the surrounding area, uncovering hidden treasures and artifacts.")
        game_line_27.pack()

        game_line_28 = Label(root, text="Among the foliage, you find a shimmering crystal emitting a soft glow.")
        game_line_28.pack()

        game_line_29 = Label(root, text="Will you 'Take' the crystal or 'Leave' it untouched?")
        game_line_29.pack()

        user_choice_4_left = Entry(root)
        user_choice_4_left.pack()

        choice_4_submit_left = Button(root, text="Submit", command=fifth_encounter_left)
        choice_4_submit_left.pack()

    elif chosen_action_left.lower() == "search":
        game_line_30 = Label(root, text="You carefully search through the belongings, finding some useful items.")
        game_line_30.pack()

        game_line_31 = Label(root, text="Among them, you find a map revealing the location of hidden treasure.")
        game_line_31.pack()

        game_line_32 = Label(root, text="Feeling excited, you decide to continue your journey and find the treasure.")
        game_line_32.pack()

        game_line_33 = Label(root, text="As you search, you notice a hidden passage leading deeper into the forest.")
        game_line_33.pack()

        game_line_34 = Label(root, text="Will you 'Investigate' the passage or 'Proceed' on your current path?")
        game_line_34.pack()

        user_choice_4_left = Entry(root)
        user_choice_4_left.pack()

        choice_4_submit_left = Button(root, text="Submit", command=fifth_encounter_left)
        choice_4_submit_left.pack()

    elif chosen_action_left.lower() == "rest":
        game_line_35 = Label(root, text="You decide to rest by the fire, enjoying the warmth and comfort.")
        game_line_35.pack()

        game_line_36 = Label(root, text="As you relax, you reflect on your journey so far and the adventures ahead.")
        game_line_36.pack()

        game_line_37 = Label(root, text="Feeling refreshed, you continue your quest with renewed energy.")
        game_line_37.pack()

        game_line_38 = Label(root, text="While resting, you notice a hidden path veering off from the clearing.")
        game_line_38.pack()

        game_line_39 = Label(root, text="Will you 'Inspect' the path or 'Proceed' on your current path?")
        game_line_39.pack()

        user_choice_4_left = Entry(root)
        user_choice_4_left.pack()

        choice_4_submit_left = Button(root, text="Submit", command=fifth_encounter_left)
        choice_4_submit_left.pack()

def fourth_encounter_right():
    chosen_action_right = user_choice_3_right.get()
    if chosen_action_right.lower() == "press on":
        game_line_40 = Label(root, text="You press on through the mist, determination overcoming fear.")
        game_line_40.pack()

        game_line_41 = Label(root, text="As you walk, the whispers fade, replaced by a sense of calm.")
        game_line_41.pack()

        game_line_42 = Label(root, text="You emerge from the mist into a clearing, the sun shining overhead.")
        game_line_42.pack()

        game_line_43 = Label(root, text="Will you 'Rest' in the clearing or 'Continue' your journey?")
        game_line_43.pack()

        global user_choice_4_right
        user_choice_4_right = Entry(root)
        user_choice_4_right.pack()

        choice_4_submit_right = Button(root, text="Submit", command=fifth_encounter_right)
        choice_4_submit_right.pack()

    elif chosen_action_right.lower() == "turn back":
        game_line_44 = Label(root, text="You turn back from the mist, relief flooding through you.")
        game_line_44.pack()

        game_line_45 = Label(root, text="As you retreat, the mist begins to dissipate, revealing a hidden path.")
        game_line_45.pack()

        game_line_46 = Label(root, text="Will you 'Follow' the path or 'Return' to the fork in the road?")
        game_line_46.pack()

        user_choice_4_right = Entry(root)
        user_choice_4_right.pack()

        choice_4_submit_right = Button(root, text="Submit", command=fifth_encounter_right)
        choice_4_submit_right.pack()

    elif chosen_action_right.lower() == "follow":
        game_line_47 = Label(root, text="You decide to follow the hidden path revealed by the dissipating mist.")
        game_line_47.pack()

        game_line_48 = Label(root, text="As you walk along the path, you feel a sense of anticipation building.")
        game_line_48.pack()

        game_line_49 = Label(root, text="The path leads you deeper into the heart of the island, uncovering new mysteries.")
        game_line_49.pack()

        game_line_50 = Label(root, text="Will you 'Continue' along the path or 'Rest' for a moment?")
        game_line_50.pack()

        user_choice_4_right = Entry(root)
        user_choice_4_right.pack()

        choice_4_submit_right = Button(root, text="Submit", command=fifth_encounter_right)
        choice_4_submit_right.pack()

    elif chosen_action_right.lower() == "return":
        game_line_51 = Label(root, text="You choose to return to the fork in the road, leaving the mist behind.")
        game_line_51.pack()

        game_line_52 = Label(root, text="As you journey back, you reflect on the path not taken and the mysteries left behind.")
        game_line_52.pack()

        game_line_53 = Label(root, text="Perhaps there are other paths to explore, but for now, you continue your adventure.")
        game_line_53.pack()

        game_line_54 = Label(root, text="Will you 'Explore' the fork in the road or 'Rest' for a moment?")
        game_line_54.pack()

        user_choice_4_right = Entry(root)
        user_choice_4_right.pack()

        choice_4_submit_right = Button(root, text="Submit", command=fifth_encounter_right)
        choice_4_submit_right.pack()
    

def fifth_encounter_left():
    chosen_action_left = user_choice_4_left.get()
    if chosen_action_left.lower() == "read":
        game_line_55 = Label(root, text="As you read the inscriptions, ancient knowledge floods your mind.")
        game_line_55.pack()

        game_line_56 = Label(root, text="You gain insights into the island's history and its mysteries.")
        game_line_56.pack()

        game_line_57 = Label(root, text="Feeling enlightened, you continue your journey with newfound purpose.")
        game_line_57.pack()

    elif chosen_action_left.lower() == "touch":
        game_line_58 = Label(root, text="As you touch the glowing moss, a surge of energy courses through you.")
        game_line_58.pack()

        game_line_59 = Label(root, text="You feel connected to the island's magic, as if it recognizes you.")
        game_line_59.pack()

        game_line_60 = Label(root, text="With renewed vigor, you press on, eager to uncover more secrets.")
        game_line_60.pack()

    elif chosen_action_left.lower() == "take":
        game_line_61 = Label(root, text="You carefully pick up the shimmering crystal, feeling its power in your hands.")
        game_line_61.pack()

        game_line_62 = Label(root, text="It emits a soft glow, illuminating your path as you continue your journey.")
        game_line_62.pack()

    elif chosen_action_left.lower() == "leave":
        game_line_63 = Label(root, text="You decide to leave the crystal untouched, respecting its mysterious presence.")
        game_line_63.pack()

        game_line_64 = Label(root, text="With a sense of reverence, you continue your adventure, wondering about its significance.")
        game_line_64.pack()

    elif chosen_action_left.lower() == "investigate":
        game_line_65 = Label(root, text="Intrigued by the hidden passage, you decide to investigate further.")
        game_line_65.pack()

        game_line_66 = Label(root, text="As you venture into the passage, you discover a hidden chamber.")
        game_line_66.pack()

        game_line_67 = Label(root, text="Within the chamber, you find ancient relics and treasures beyond imagination.")
        game_line_67.pack()

        game_line_68 = Label(root, text="With your newfound riches, you decide to retire from adventuring, content with your discoveries.")
        game_line_68.pack()

        
    elif chosen_action_left.lower() == "proceed":
        game_line_69 = Label(root, text="Deciding to stay on your current path, you continue your journey through the forest.")
        game_line_69.pack()

        game_line_70 = Label(root, text="As you travel, you encounter various challenges and wonders, each adding to your story.")
        game_line_70.pack()

        game_line_71 = Label(root, text="With each step, you grow wiser and more experienced, ready for whatever lies ahead.")
        game_line_71.pack()
        
    elif chosen_action_left.lower() == "inspect":
        game_line_72 = Label(root, text="Intrigued by the hidden path, you decide to inspect it closely.")
        game_line_72.pack()

        game_line_73 = Label(root, text="You find markings indicating that it leads to a forgotten temple deep within the island.")
        game_line_73.pack()

        game_line_74 = Label(root, text="Determined to uncover its secrets, you follow the path into the heart of the island.")
        game_line_74.pack()

def fifth_encounter_right():
    chosen_action_right = user_choice_4_right.get()
    if chosen_action_right.lower() == "rest":
        game_line_75 = Label(root, text="You take a moment to rest in the clearing, basking in the warmth of the sun.")
        game_line_75.pack()

        game_line_76 = Label(root, text="As you rest, you calm yourself and reflect on your journey and the challenges ahead.")
        game_line_76.pack()

        game_line_77 = Label(root, text="Feeling rejuvenated, you continue your adventure with renewed determination.")
        game_line_77.pack()

    elif chosen_action_right.lower() == "continue":
        game_line_78 = Label(root, text="With a sense of purpose, you continue your journey through the island's mysteries.")
        game_line_78.pack()

        game_line_79= Label(root, text="You know that every step brings you closer to uncovering its secrets.")
        game_line_79.pack()

        game_line_80 = Label(root, text="With each passing moment, your resolve grows stronger.")
        game_line_80.pack()

    elif chosen_action_right.lower() == "follow":
        game_line_81 = Label(root, text="You decide to follow the hidden path revealed by the dissipating mist.")
        game_line_81.pack()

        game_line_82 = Label(root, text="As you walk along the path, you feel a sense of anticipation building.")
        game_line_82.pack()

        game_line_83 = Label(root, text="The path leads you deeper into the heart of the island, uncovering new mysteries.")
        game_line_83.pack()

    elif chosen_action_right.lower() == "explore":
        game_line_84 = Label(root, text="You decide to explore the fork in the road, curious about what lies ahead.")
        game_line_84.pack()

        game_line_85 = Label(root, text="As you explore, you stumble upon hidden treasures and ancient artifacts.")
        game_line_85.pack()

        game_line_86 = Label(root, text="Each discovery fuels your sense of adventure, spurring you onward.")
        game_line_86.pack()

    elif chosen_action_right.lower() == "return":
        game_line_87 = Label(root, text="You choose to return to the fork in the road, leaving the mist behind.")
        game_line_87.pack()

        game_line_88 = Label(root, text="As you journey back, you reflect on the path not taken and the mysteries left behind.")
        game_line_88.pack()

        game_line_89 = Label(root, text="Perhaps there are other paths to explore, but for now, you continue your adventure.")
        game_line_89.pack()
        

name_entry()

root.mainloop()
