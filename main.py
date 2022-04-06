def choice_story_type() -> int:
    """Asks with verification to the user for the story he wants and returns the number of the story"""

    print("What story do you want to complete :")
    print("\t1. A day a the zoo!")
    print("\t2. In the jungle!")
    print("\t3. A trip to Disney World!")
    print("\t4. The Monkey King!")

    user_input = input("> ")

    while user_input.strip() not in ("1", "2", "3", "4"):
        user_input = input("Enter the number of the story : [1-4] ")
    return int(user_input)


def story_zoo():
    """ Ask the user for the words to complete the story and print it"""

    adj_1 = input("\tPlease, enter an adjective > ")
    non_1 = input("\tPlease, enter an noun > ")
    vrb_1 = input("\tPlease, enter a verb in past tense > ")
    adv_1 = input("\tPlease, enter an adverb > ")
    adj_2 = input("\tPlease, enter an adjective > ")
    non_2 = input("\tPlease, enter an noun > ")
    non_3 = input("\tPlease, enter an noun > ")
    adj_3 = input("\tPlease, enter an adjective > ")
    vrb_2 = input("\tPlease, enter a verb > ")
    adv_2 = input("\tPlease, enter an adverb > ")
    vrb_3 = input("\tPlease, enter a verb in past tense > ")
    adj_4 = input("\tPlease, enter an adjective > ")

    story = (f"~~~~~\n"
             f"Today I went to the zoo. I saw a(n) {adj_1} "
             f"{non_1} jumping up and down in its tree.\n"
             f"He {vrb_1} {adv_1} through the large tunnel that led to its {adj_2} {non_2}.\n"
             f"I got some peanuts and passed them through the cage" 
             f" to a gigantic gray {non_3} towering above my head. " 
             f"Feeding that animal made me hungry. I went to get a {adj_3} scoop of ice cream.\n" 
             f"It filled my stomach. Afterwards I had to {vrb_2} {adv_2} to catch our bus.\n"
             f"When I got home I {vrb_3} my mom for a {adj_4} day at the zoo.")
    print(story)


def story_jungle():
    """ Ask the user for the words to complete the story and print it"""

    adj_1 = input("\tPlease, enter an adjective > ")
    adj_2 = input("\tPlease, enter an adjective > ")
    non_1 = input("\tPlease, enter an noun > ")
    vrb_1 = input("\tPlease, enter a verb in past tense > ")
    adv_1 = input("\tPlease, enter an adverb > ")
    non_2 = input("\tPlease, enter an noun > ")
    non_3 = input("\tPlease, enter an noun > ")
    adj_3 = input("\tPlease, enter an adjective > ")
    vrb_2 = input("\tPlease, enter a verb > ")
    adv_2 = input("\tPlease, enter an adverb > ")
    vrb_3 = input("\tPlease, enter a verb in past tense > ")
    adj_4 = input("\tPlease, enter an adjective > ")

    story = (f"I walk through the color jungle. I take out my {adj_1} canteen.\n "
             f"There's a {adj_2}
________(adjective) parrot with a ______________(adjective)
_______________(noun) in his mouth right there in front
of me in the _________(adjective) trees! I gaze at his
__________(adjective) _______________(noun). A sudden
sound awakes me from my daydream! A panther’s
_______________(verb) in front of my head! I
_______________(verb) his _______________(adjective)
breath. I remember I have a packet of _________(noun)
that makes go into a deep slumber! I
__________(verb)it away from me in front of the
_______________(noun).Yes he's eating it! I
_______________(verb) away through the
____________(adjective) jungle. I meet my parents at the
tent. Phew! It’s been an exciting day in the jungle."
    print(story)


if __name__ == "__main__":
    number_story = choice_story_type()
    if number_story == 1:
        story_zoo()
    else:
        print("No yet")