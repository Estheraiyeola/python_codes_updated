name_list = []
response_storage_for_extrovert_and_introvert = []
response_storage_for_sensing_and_intuitive = []
response_storage_for_thinking_and_feeling = []
response_storage_for_judging_and_perspective = []
response_storage = [response_storage_for_extrovert_and_introvert, response_storage_for_sensing_and_intuitive,
                    response_storage_for_thinking_and_feeling, response_storage_for_judging_and_perspective]
letters_collector = ''
question_storage = [
    ["A. Expend energy, enjoy groups.", "B. Conserve energy, one-on-one"],
    ["A. Interpret literally", "B. Look for meaning and possibilities"],
    ["A. Logical, thinking, questioning.", "B. Empathetic, feeling, accommodating"],
    ["A. Organized, orderly.", "B. Flexible, adaptable"],
    ["A. More outgoing, think out loud.", "B. More reserved, think to yourself."],
    ["A. Practical, realistic, experiential.", "B. Imagination, innovative, theoretical."],
    ["A. Candid, straight forward, frank.", "B. Tactful, kind, encouraging."],
    ["A. Plan, schedule.", "B. Unplanned, spontaneous"],
    ["A. seek many tasks, public activities, interaction with others",
     "B. seek private, solitary activities with quiet to concentrate."],
    ["A. standard, usual, conventional.", "B. different, novel, unique."],
    ["A. firm, tend to criticize, hold the line.", "B. gentle, tend to appreciate, conciliate."],
    ["A.regulated, structured.", "B. easygoing, live  and let live"],
    ["A. external, communicative, express yourself.", "B. internal, reticent, keep to yourself"],
    ["A. focus on here-and-now.", "B. look to the future, global perspective, \\\"big picture\\\""],
    ["A. tough minded, just.", "B. tender-hearted, merciful"],
    ["A. preparation, plan ahead.", "B. go with the flow, adapt as you go."],
    ["A. active, initiate.", "B. reflective, deliberate"],
    ["A. facts, things, \\\"what is\\\"", "B. ideas, dreams, 'what could be', philosophical"],
    ["A. matter of fact, issue oriented", "B. sensitive, people-oriented, compassionate"],
    ["A. control, govern.", "B. latitude, freedom."]
]


def name_function():
    global name_list
    name = input("What is your name? ")
    name_list += [name]
    question_one()


def get_name_function():
    global name_list
    return name_list


def question_one():
    response = input("""
    A. Expend energy, enjoy groups.  B. Conserve energy, one-on-one
    """)
    response_function_one(response)
    question_two()


def response_function_one(response):
    global response_storage_for_extrovert_and_introvert
    if response == 'A' or response == 'B':
        response_storage_for_extrovert_and_introvert += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_one()


def question_two():
    response = input("""
    A. Interpret literally.    B. Look for meaning and possibilities
    """)
    response_function_two(response)
    question_three()


def response_function_two(response):
    global response_storage_for_sensing_and_intuitive
    if response == 'A' or response == 'B':
        response_storage_for_sensing_and_intuitive += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_two()


def response_function_three(response):
    global response_storage_for_thinking_and_feeling
    if response == 'A' or response == 'B':
        response_storage_for_thinking_and_feeling += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_three()


def question_three():
    response = input("""
    A. Logical, thinking, questioning.   B. Empathetic, feeling, accommodating
    """)
    response_function_three(response)
    question_four()


def question_four():
    response = input("""
    A. Organized, orderly.   B. Flexible, adaptable
    """)
    response_function_four(response)
    question_five()


def response_function_four(response):
    global response_storage_for_judging_and_perspective
    if response == 'A' or response == 'B':
        response_storage_for_judging_and_perspective += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_four()


def question_five():
    response = input("""
    A. More outgoing, think out loud.    B. More reserved, think to yourself.
    """)
    response_function_five(response)
    question_six()


def response_function_five(response):
    global response_storage_for_extrovert_and_introvert
    if response == 'A' or response == 'B':
        response_storage_for_extrovert_and_introvert += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_five()


def question_six():
    response = input("""
    A. Practical, realistic, experiential.    B. Imagination, innovative, theoretical.
    """)
    response_function_six(response)
    question_seven()


def response_function_six(response):
    global response_storage_for_sensing_and_intuitive
    if response == 'A' or response == 'B':
        response_storage_for_sensing_and_intuitive += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_six()


def question_seven():
    response = input("""
    A. Candid, straight forward, frank.   B. Tactful, kind, encouraging.
    """)
    response_function_seven(response)
    question_eight()


def response_function_seven(response):
    global response_storage_for_thinking_and_feeling
    if response == 'A' or response == 'B':
        response_storage_for_thinking_and_feeling += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_seven()


def question_eight():
    response = input("""
    A. Plan, schedule.   B. Unplanned, spontaneous
    """)
    response_function_eight(response)
    question_nine()


def response_function_eight(response):
    global response_storage
    if response == 'A' or response == 'B':
        response_storage_for_judging_and_perspective.append(response)
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_eight()


def question_nine():
    response = input("""
    A. seek many tasks, public activities, interaction with others     B. seek private, solitary activities with quiet to concentrate.
    """)
    response_function_nine(response)
    question_ten()


def response_function_nine(response):
    global response_storage_for_extrovert_and_introvert
    if response == 'A' or response == 'B':
        response_storage_for_extrovert_and_introvert += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_nine()


def question_ten():
    response = input("""
    A. standard, usual, conventional.    B. different, novel, unique.
    """)
    response_function_ten(response)
    question_eleven()


def response_function_ten(response):
    global response_storage_for_sensing_and_intuitive
    if response == 'A' or response == 'B':
        response_storage_for_sensing_and_intuitive += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_ten()


def question_eleven():
    response = input("""
    A. firm, tend to criticize, hold the line.", "B. gentle, tend to appreciate, conciliate.
    """)
    response_function_eleven(response)
    question_twelve()


def response_function_eleven(response):
    global response_storage
    if response == 'A' or response == 'B':
        response_storage_for_thinking_and_feeling.append(response)
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_eleven()


def question_twelve():
    response = input("""
    A.regulated, structured.    B. easygoing, live  and let live"
    """)
    response_function_twelve(response)
    question_thirteen()


def response_function_twelve(response):
    global response_storage
    if response == 'A' or response == 'B':
        response_storage_for_judging_and_perspective.append(response)
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_twelve()


def question_thirteen():
    response = input("""
    A. external, communicative, express yourself.    B. internal, reticent, keep to yourself.
    """)
    response_function_thirteen(response)
    question_fourteen()


def response_function_thirteen(response):
    global response_storage_for_extrovert_and_introvert
    if response == 'A' or response == 'B':
        response_storage_for_extrovert_and_introvert += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_thirteen()


def question_fourteen():
    response = input("""
    A. focus on here-and-now.    B. look to the future, global perspective, \\"big picture\\""
    """)
    response_function_fourteen(response)
    question_fifteen()


def response_function_fourteen(response):
    global response_storage_for_sensing_and_intuitive
    if response == 'A' or response == 'B':
        response_storage_for_sensing_and_intuitive += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_fourteen()


def question_fifteen():
    response = input("""
    A. tough minded, just.    B. tender-hearted, merciful
    """)
    response_function_fifteen(response)
    question_sixteen()


def response_function_fifteen(response):
    global response_storage
    if response == 'A' or response == 'B':
        response_storage_for_thinking_and_feeling.append(response)
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_fifteen()


def question_sixteen():
    response = input("""
    A. preparation, plan ahead.    B. go with the flow, adapt as you go.
    """)
    response_function_sixteen(response)
    question_seventeen()


def response_function_sixteen(response):
    global response_storage
    if response == 'A' or response == 'B':
        response_storage_for_judging_and_perspective.append(response)
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_sixteen()


def question_seventeen():
    response = input("""
    A. active, initiate.     B. reflective, deliberate
    """)
    response_function_seventeen(response)
    question_eighteen()


def response_function_seventeen(response):
    global response_storage_for_extrovert_and_introvert
    if response == 'A' or response == 'B':
        response_storage_for_extrovert_and_introvert += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_seventeen()


def question_eighteen():
    response = input("""
    A. facts, things, \\"what is\\"      B. ideas, dreams, 'what could be', philosophical
    """)
    response_function_eighteen(response)
    question_nineteen()


def response_function_eighteen(response):
    global response_storage_for_sensing_and_intuitive
    if response == 'A' or response == 'B':
        response_storage_for_sensing_and_intuitive += [response]
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_eighteen()


def question_nineteen():
    response = input("""
    A. matter of fact, issue oriented     B. sensitive, people-oriented, compassionate
    """)
    response_function_nineteen(response)
    question_twenty()


def response_function_nineteen(response):
    global response_storage
    if response == 'A' or response == 'B':
        response_storage_for_thinking_and_feeling.append(response)
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_nineteen()


def question_twenty():
    response = input("""
    A. control, govern    B. latitude, freedom
    """)
    response_function_twenty(response)
    connect_responses_for_extroverts_and_introverts_to_the_questions()
    connect_responses_for_sensing_and_intuitive_to_the_questions()
    connect_responses_for_thinking_and_feeling_to_the_questions()
    connect_responses_for_judging_and_perspective_to_the_questions()
    print(letters_collector)
    print(personality_decider())


def response_function_twenty(response):
    global response_storage
    if response == 'A' or response == 'B':
        response_storage_for_judging_and_perspective.append(response)
    else:
        print('Expected A or B as a response')
        print('I know this is an Error. Please retry again')
        question_twenty()


def extrovert_and_introvert_response_analyzer(storage):
    global letters_collector
    letter = ''
    a_counter = 0
    b_counter = 0
    for response in storage:
        if response == 'A':
            a_counter += 1
        if response == 'B':
            b_counter += 1
    if a_counter > b_counter:
        letter = 'E'
    if a_counter < b_counter:
        letter = 'I'
    letters_collector += letter
    print(f'Number of A selected is: {a_counter}')
    print(f'Number of B selected is: {b_counter}')
    print()


def sensing_and_intuitive_response_analyzer(storage):
    global letters_collector
    letter = ''
    a_counter = 0
    b_counter = 0
    for response in storage:
        if response == 'A':
            a_counter += 1
        if response == 'B':
            b_counter += 1
    if a_counter > b_counter:
        letter = 'S'
    if a_counter < b_counter:
        letter = 'N'
    letters_collector += letter
    print(f'Number of A selected is: {a_counter}')
    print(f'Number of B selected is: {b_counter}')
    print()


def thinking_and_feeling_response_analyzer(storage):
    global letters_collector
    letter = ''
    a_counter = 0
    b_counter = 0
    for response in storage:
        if response == 'A':
            a_counter += 1
        if response == 'B':
            b_counter += 1
    if a_counter > b_counter:
        letter = 'T'
    if a_counter < b_counter:
        letter = 'F'
    letters_collector += letter
    print(f'Number of A selected is: {a_counter}')
    print(f'Number of B selected is: {b_counter}')
    print()


def judging_and_perspective_response_analyzer(storage):
    global letters_collector
    letter = ''
    a_counter = 0
    b_counter = 0
    for response in storage:
        if response == 'A':
            a_counter += 1
        if response == 'B':
            b_counter += 1
    if a_counter > b_counter:
        letter = 'J'
    if a_counter < b_counter:
        letter = 'P'
    letters_collector += letter
    print(f'Number of A selected is: {a_counter}')
    print(f'Number of B selected is: {b_counter}')
    print()


def connect_responses_for_extroverts_and_introverts_to_the_questions():
    global response_storage, question_storage
    if response_storage[0][0] == 'A':
        print(question_storage[0][0])
    if response_storage[0][0] == 'B':
        print(question_storage[0][1])
    if response_storage[0][1] == 'A':
        print(question_storage[4][0])
    if response_storage[0][1] == 'B':
        print(question_storage[4][1])
    if response_storage[0][2] == 'A':
        print(question_storage[8][0])
    if response_storage[0][2] == 'B':
        print(question_storage[8][0])
    if response_storage[0][3] == 'A':
        print(question_storage[12][0])
    if response_storage[0][3] == 'B':
        print(question_storage[12][1])
    if response_storage[0][4] == 'A':
        print(question_storage[16][0])
    if response_storage[0][4] == 'B':
        print(question_storage[16][1])
    extrovert_and_introvert_response_analyzer(response_storage_for_extrovert_and_introvert)


def connect_responses_for_sensing_and_intuitive_to_the_questions():
    global response_storage, question_storage
    if response_storage[1][0] == 'A':
        print(question_storage[1][0])
    if response_storage[1][0] == 'B':
        print(question_storage[1][1])
    if response_storage[1][1] == 'A':
        print(question_storage[5][0])
    if response_storage[1][1] == 'B':
        print(question_storage[5][1])
    if response_storage[1][2] == 'A':
        print(question_storage[9][0])
    if response_storage[1][2] == 'B':
        print(question_storage[9][0])
    if response_storage[1][3] == 'A':
        print(question_storage[13][0])
    if response_storage[1][3] == 'B':
        print(question_storage[13][1])
    if response_storage[1][4] == 'A':
        print(question_storage[17][0])
    if response_storage[1][4] == 'B':
        print(question_storage[17][1])
    sensing_and_intuitive_response_analyzer(response_storage_for_sensing_and_intuitive)


def connect_responses_for_thinking_and_feeling_to_the_questions():
    global response_storage, question_storage
    if response_storage[2][0] == 'A':
        print(question_storage[2][0])
    if response_storage[2][0] == 'B':
        print(question_storage[2][1])
    if response_storage[2][1] == 'A':
        print(question_storage[6][0])
    if response_storage[2][1] == 'B':
        print(question_storage[6][1])
    if response_storage[2][2] == 'A':
        print(question_storage[10][0])
    if response_storage[2][2] == 'B':
        print(question_storage[10][1])
    if response_storage[2][3] == 'A':
        print(question_storage[14][0])
    if response_storage[2][3] == 'B':
        print(question_storage[14][1])
    if response_storage[2][4] == 'A':
        print(question_storage[18][0])
    if response_storage[2][4] == 'B':
        print(question_storage[18][1])
    thinking_and_feeling_response_analyzer(response_storage_for_thinking_and_feeling)


def connect_responses_for_judging_and_perspective_to_the_questions():
    global response_storage, question_storage
    if response_storage[3][0] == 'A':
        print(question_storage[3][0])
    if response_storage[3][0] == 'B':
        print(question_storage[3][1])
    if response_storage[3][1] == 'A':
        print(question_storage[7][0])
    if response_storage[3][1] == 'B':
        print(question_storage[7][1])
    if response_storage[3][2] == 'A':
        print(question_storage[11][0])
    if response_storage[3][2] == 'B':
        print(question_storage[11][1])
    if response_storage[3][3] == 'A':
        print(question_storage[15][0])
    if response_storage[3][3] == 'B':
        print(question_storage[15][1])
    if response_storage[3][4] == 'A':
        print(question_storage[19][0])
    if response_storage[3][4] == 'B':
        print(question_storage[19][1])
    judging_and_perspective_response_analyzer(response_storage_for_judging_and_perspective)


def personality_INTJ():
    print("Architect")
    print("""
    An Architect (INTJ) is a person with the Introverted, Intuitive, Thinking, and Judging personality traits. 
    These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. 
    Their inner world is often a private, complex one.
    A Pioneering Spirit
    Architects question everything. 
    Many personality types trust the status quo, relying on conventional wisdom and other people’s expertise to guide their lives. 
    But ever-skeptical Architects prefer to make their own discoveries. In their quest to find better ways of doing things, they aren’t afraid to break the rules or risk disapproval – in fact, they rather enjoy it.               
    But as anyone with this personality type would tell you, a new idea isn’t worth anything unless it actually works. 
    Architects want to be successful, not just inventive. They bring a single-minded drive to their work, applying the full force of their insight, logic, and willpower. And heaven help anyone who tries to slow them down by enforcing pointless rules or offering poorly thought-out criticism.               
    """)


def personalityINTP():
    print("Logician")
    print("""
    A Logician (INTP) is someone with the Introverted, Intuitive, Thinking, and Prospecting personality traits. 
    These flexible thinkers enjoy taking an unconventional approach to many aspects of life. 
    They often seek out unlikely paths, mixing willingness to experiment with personal creativity.
    From the outside, Logicians may seem to live in a never-ending daydream. 
    They have a reputation for being pensive, detached, and a bit reserved. 
    That is, until they try to train all of their mental energy on the moment or the person at hand, which can be a bit uncomfortable for everyone. 
    But regardless of which mode they’re in, Logicians are Introverts and tend to get tired out by extensive socializing. 
    After a long day, they crave time alone to consult their own thoughts.             
    But it would be a mistake to think that Logicians are unfriendly or uptight. When they connect with someone who can match their mental energy, these personalities absolutely light up, leaping from one thought to another. Few things energize them like the opportunity to swap ideas or enjoy a lively debate with another curious, inquiring soul.
    """)


def personalityENTJ():
    print("Commander")
    print("""
    A Commander (ENTJ) is someone with the Extraverted, Intuitive, Thinking, and Judging personality traits. 
    They are decisive people who love momentum and accomplishment. 
    They gather information to construct their creative visions but rarely hesitate for long before acting on them.
    Commanders are natural-born leaders. 
    People with this personality type embody the gifts of charisma and confidence, and project authority in a way that draws crowds together behind a common goal. However, Commanders are also characterized by an often ruthless level of rationality, using their drive, determination and sharp minds to achieve whatever end they’ve set for themselves. 
    Perhaps it is best that they make up only three percent of the population, lest they overwhelm the more timid and sensitive personality types that make up much of the rest of the world – but we have Commanders to thank for many of the businesses and institutions we take for granted every day.
    """)


def personalityENTP():
    print("Debater")
    print("""
    A Debater (ENTP) is a person with the Extraverted, Intuitive, Thinking, and Prospecting personality traits. 
    They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. 
    They pursue their goals vigorously despite any resistance they might encounter.               
    Quick-witted and audacious, Debaters aren’t afraid to disagree with the status quo. 
    In fact, they’re not afraid to disagree with pretty much anything or anyone. 
    Few things light up people with this personality type more than a bit of verbal sparring – and if the conversation veers into controversial terrain, so much the better.     
    It would be a mistake, though, to think of Debaters as disagreeable or mean-spirited.
    Instead, people with this personality type are knowledgeable and curious, with a playful sense of humor, and they can be incredibly entertaining. 
    They simply have an offbeat, contrarian idea of fun – one that involves a healthy dose of spirited debate.    
    """)


def personalityINFJ():
    print("Advocate")
    print("""
    An Advocate (INFJ) is someone with the Introverted, Intuitive, Feeling, and Judging personality traits. 
    They tend to approach life with deep thoughtfulness and imagination. 
    Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.
    Advocates (INFJs) may be the rarest personality type of all, but they certainly leave their mark on the world. Idealistic and principled, they aren’t content to coast through life – they want to stand up and make a difference. 
    For Advocate personalities, success doesn’t come from money or status but from seeking fulfillment, helping others, and being a force for good in the world.
    While they have lofty goals and ambitions, Advocates shouldn’t be mistaken for idle dreamers. 
    People with this personality type care about integrity, and they’re rarely satisfied until they’ve done what they know to be right. 
    Conscientious to the core, they move through life with a clear sense of their values, and they aim never to lose sight of what truly matters – not according to other people or society at large, but according to their own wisdom and intuition.
    """)


def personalityINFP():
    print("Mediator")
    print("""
    A Mediator (INFP) is someone who possesses the Introverted, Intuitive, Feeling, and Prospecting personality traits. 
    These rare personality types tend to be quiet, open-minded, and imaginative, and they apply a caring and creative approach to everything they do.
    Although they may seem quiet or unassuming, Mediators (INFPs) have vibrant, passionate inner lives. 
    Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and conversations in their minds. 
    These personalities are known for their sensitivity – Mediators can have profound emotional responses to music, art, nature, and the people around them.               
    Idealistic and empathetic, Mediators long for deep, soulful relationships, and they feel called to help others. 
    But because this personality type makes up such a small portion of the population, Mediators may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to appreciate the traits that make them unique.               
    """)


def personalityENFJ():
    print("Protagonist")
    print("""
    A Protagonist (ENFJ) is a person with the Extraverted, Intuitive, Feeling, and Judging personality traits. 
    These warm, forthright types love helping others, and they tend to have strong ideas and values. 
    They back their perspective with the creative energy to achieve their goals.          
    Protagonists (ENFJs) feel called to serve a greater purpose in life. 
    Thoughtful and idealistic, these personality types strive to have a positive impact on other people and the world around them. 
    They rarely shy away from an opportunity to do the right thing, even when doing so is far from easy.
    Protagonists are born leaders, which explains why these personalities can be found among many notable politicians, coaches, and teachers. 
    Their passion and charisma allow them to inspire others not just in their careers but in every arena of their lives, including their relationships.
     Few things bring Protagonists a deeper sense of joy and fulfillment than guiding friends and loved ones to grow into their best selves                
    """)


def personalityENFP():
    print("Campaigner")
    print("""
    A Campaigner (ENFP) is someone with the Extraverted, Intuitive, Feeling, and Prospecting personality traits. 
    These people tend to embrace big ideas and actions that reflect their sense of hope and goodwill toward others. 
    Their vibrant energy can flow in many directions.
    Campaigners (ENFPs) are true free spirits – outgoing, openhearted, and open-minded. 
    With their lively, upbeat approach to life, they stand out in any crowd. 
    But even though they can be the life of the party, Campaigners don’t just care about having a good time. 
    These personality types run deep – as does their longing for meaningful, emotional connections with other people  
    """)


def personalityISTJ():
    print("Logistician")
    print("""
    A Logistician (ISTJ) is someone with the Introverted, Observant, Thinking, and Judging personality traits. 
    These people tend to be reserved yet willful, with a rational outlook on life. 
    They compose their actions carefully and carry them out with methodical purpose.
    Logisticians pride themselves on their integrity. 
    People with this personality type mean what they say, and when they commit to doing something, they make sure to follow through.                
    This personality type makes up a good portion of the overall population, and while Logisticians may not be particularly flashy or attention-seeking, they do more than their share to keep society on a sturdy, stable foundation. 
    In their families and their communities, Logisticians often earn respect for their reliability, their practicality, and their ability to stay grounded and logical, even in the most stressful situations.                
    """)


def personalityISFJ():
    print("Defender")
    print("""
    A Defender (ISFJ) is someone with the Introverted, Observant, Feeling, and Judging personality traits. 
    These people tend to be warm and unassuming in their own steady way. 
    They’re efficient and responsible, giving careful attention to practical details in their daily lives.
    In their unassuming, understated way, Defenders help make the world go round. Hardworking and devoted, people with this personality type feel a deep sense of responsibility to those around them. 
    Defenders can be counted on to meet deadlines, remember birthdays and special occasions, uphold traditions, and shower their loved ones with gestures of care and support. 
    But they rarely demand recognition for all that they do, preferring instead to operate behind the scenes.
    This is a capable, can-do personality type, with a wealth of versatile gifts. 
    Though sensitive and caring, Defenders also have excellent analytical abilities and an eye for detail. 
    And despite their reserve, they tend to have well-developed people skills and robust social relationships. 
    Defenders are truly more than the sum of their parts, and their varied strengths shine in even the most ordinary aspects of their daily lives.
    """)


def personalityESTJ():
    print("Executive")
    print("""
    An Executive (ESTJ) is someone with the Extraverted, Observant, Thinking, and Judging personality traits. 
    They possess great fortitude, emphatically following their own sensible judgment. 
    They often serve as a stabilizing force among others, able to offer solid direction amid adversity.
    Executives are representatives of tradition and order, utilizing their understanding of what is right, wrong and socially acceptable to bring families and communities together. 
    Embracing the values of honesty, dedication and dignity, people with the Executive personality type are valued for their clear advice and guidance, and they happily lead the way on difficult paths. 
    Taking pride in bringing people together, Executives often take on roles as community organizers, working hard to bring everyone together in celebration of cherished local events, or in defense of the traditional values that hold families and communities together.              
    """)


def personalityESFJ():
    print("Consul")
    print("""
    A Consul (ESFJ) is a person with the Extroverted, Observant, Feeling, and Judging personality traits. 
    They are attentive and people-focused, and they enjoy taking part in their social community. 
    Their achievements are guided by decisive values, and they willingly offer guidance to others.
    For Consuls, life is sweetest when it’s shared with others. People with this personality type form the bedrock of many communities, opening their homes – and their hearts – to friends, loved ones, and neighbors.                
    This doesn’t mean that Consuls like everyone, or that they’re saints. But Consuls do believe in the power of hospitality and good manners, and they tend to feel a sense of duty to those around them. 
    Generous and reliable, people with this personality type often take it upon themselves – in ways both large and small – to hold their families and their communities together.                
    """)


def personalityISTP():
    print("Virtuoso")
    print("""
    A Virtuoso (ISTP) is someone with the Introverted, Observant, Thinking, and Prospecting personality traits. 
    They tend to have an individualistic mindset, pursuing goals without needing much external connection. 
    They engage in life with inquisitiveness and personal skill, varying their approach as needed.
    Virtuosos love to explore with their hands and their eyes, touching and examining the world around them with cool rationalism and spirited curiosity. 
    People with this personality type are natural Makers, moving from project to project, building the useful and the superfluous for the fun of it, and learning from their environment as they go. 
    Often mechanics and engineers, Virtuosos find no greater joy than in getting their hands dirty pulling things apart and putting them back together, just a little bit better than they were before.
    """)


def personalityISFP():
    print("Adventurer")
    print("""
    An Adventurer (ISFP) is a person with the Introverted, Observant, Feeling, and Prospecting personality traits. 
    They tend to have open minds, approaching life, new experiences, and people with grounded warmth. 
    Their ability to stay in the moment helps them uncover exciting potentials.
    Adventurers are true artists – although not necessarily in the conventional sense. 
    For this personality type, life itself is a canvas for self-expression. 
    From what they wear to how they spend their free time, Adventurers act in ways that vividly reflect who they are as unique individuals.                
    And every Adventurer is certainly unique. 
    Driven by curiosity and eager to try new things, people with this personality often have a fascinating array of passions and interests. 
    With their exploratory spirits and their ability to find joy in everyday life, Adventurers can be among the most interesting people you’ll ever meet. 
    The only irony? Unassuming and humble, Adventurers tend to see themselves as “just doing their own thing,” so they may not even realize how remarkable they really are.
    """)


def personalityESTP():
    print("Entrpreneur")
    print("""
    An Entrepreneur (ESTP) is someone with the Extraverted, Observant, Thinking, and Prospecting personality traits. 
    They tend to be energetic and action-oriented, deftly navigating whatever is in front of them. 
    They love uncovering life’s opportunities, whether socializing with others or in more personal pursuits.
    Entrepreneurs always have an impact on their immediate surroundings – the best way to spot them at a party is to look for the whirling eddy of people flitting about them as they move from group to group. 
    Laughing and entertaining with a blunt and earthy humor, Entrepreneur personalities love to be the center of attention. 
    If an audience member is asked to come on stage, Entrepreneurs volunteer – or volunteer a shy friend.                
    Theory, abstract concepts and plodding discussions about global issues and their implications don’t keep Entrepreneurs interested for long. 
    Entrepreneurs keep their conversation energetic, with a good dose of intelligence, but they like to talk about what is – or better yet, to just go out and do it. 
    Entrepreneurs leap before they look, fixing their mistakes as they go, rather than sitting idle, preparing contingencies and escape clauses.
    """)


def personalityESFP():
    print("Entertainer")
    print("""
    An Entertainer (ESFP) is a person with the Extraverted, Observant, Feeling, and Prospecting personality traits. 
    These people love vibrant experiences, engaging in life eagerly and taking pleasure in discovering the unknown. 
    They can be very social, often encouraging others into shared activities.
    If anyone is to be found spontaneously breaking into song and dance, it is the Entertainer personality type. 
    Entertainers get caught up in the excitement of the moment, and want everyone else to feel that way, too. 
    No other personality type is as generous with their time and energy as Entertainers when it comes to encouraging others, and no other personality type does it with such irresistible style.                
    """)


def personality_decider():
    if letters_collector == "INFJ": personality_INTJ()
    if letters_collector == "INTP": personalityINTP()
    if letters_collector == "ENTJ": personalityENTJ()
    if letters_collector == "ENTP": personalityENTP()
    if letters_collector == "INFJ": personalityINFJ()
    if letters_collector == "INFP": personalityINFP()
    if letters_collector == "ENFJ": personalityENFJ()
    if letters_collector == "ENFP": personalityENFP()
    if letters_collector == "ISTJ": personalityISTJ()
    if letters_collector == "ISFJ": personalityISFJ()
    if letters_collector == "ESTJ": personalityESTJ()
    if letters_collector == "ESFJ": personalityESFJ()
    if letters_collector == "ISTP": personalityISTP()
    if letters_collector == "ISFP": personalityISFP()
    if letters_collector == "ESTP": personalityESTP()
    if letters_collector == "ESFP": personalityESFP()


print(name_function())
