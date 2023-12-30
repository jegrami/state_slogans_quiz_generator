#! python3

# statecaps_quiz_gen creates Nigerian state and capital quiz questions 
# in a random order, along with their corresponding answers.
import random


# STEP 1: Create a dictionary of state names and their capitals.
# The state names are the dictionary keys while the capitals are the values

states = {
    'Abia': "God's Own State", 'Adamawa': 'Land of Beauty', 'Akwa Ibom': 'Land of Promise',
    'Anambra': 'Light of the Nation', 'Bauchi': 'Pearl of Tourism', 'Bayelsa': 'Glory of All Lands',
    'Benue': 'Food Basket of the Nation', 'Borno': 'Home of Peace', 'Cross River': "The People's Paradise",
    'Delta': 'The Big Heart', 'Ebonyi': 'Salt of the Nation', 'Edo': 'Heart Beat of Nigeria',
    'Ekiti': 'Land of Honor and Integrity', 'Enugu': 'Coal City State', 'Gombe': 'Jewel in the Savannah',
    'Imo': 'Eastern Heartland', 'Jigawa': 'The New World', 'Kaduna': 'Centre of Learning',
    'Kano': 'Centre of Commerce', 'Katsina': 'Home of Hospitality', 'Kebbi': 'Land of Equity',
    'Koji': 'The Confluence State', 'Kwara': 'State of Harmony', 'Lagos': 'Centre of Excellence',
    'Nasarawa': 'Home of Solid Minerals', 'Niger': 'The Power State', 'Ogun': 'Gateway State',
    'Ondo': 'Sunshine State', 'Osun': 'Land of Virtue', 'Oyo': 'Pace Setter State',
    'Plateau': 'Home of Peace and Tourism', 'Rivers': 'Treasure Base of the Nation', 'Sokoto': 'Seat of the Caliphate',
    'Taraba': "Nature's Gift to the Nation", 'Yobe': 'Pride of the Sahel', 'Zamfara': 'Farming is Our Pride'
}


# STEP 2: Generate a specified number of question and answer files

for quiz_num in range(2):
    
    quiz_file = open(f"state_slogan_quiz{quiz_num + 1}.txt", "w")
    
    answer_file = open(f"state_slogan_quiz_answers{quiz_num + 1}.txt", "w")

    # Write a heading for the quiz files
    quiz_file.write('Name: \n\nDate: \n\nClass: \n\nTerm:\n')
    quiz_file.write(f"State Slogans Quiz (Form{quiz_num + 1})".center(60, '='))

    quiz_file.write('\n\n')

    # Create a list of state names from the states dictionary keys and shuffle it
    state_names = list(states.keys())
    random.shuffle(state_names)


# STEP 3: Create answers options
    
    for question_num in range(36):
    # Loop through all states and get the right and wrong answers 
    # for each quiz question

    # get right answer
        correct_answer = states[state_names[question_num]]

    # get wrong answers by first duplicating all the values in the 
    # states dictionary and then deleting the correct answer 
    # using their index positions
    
        wrong_answers = list(states.values())
        del wrong_answers[wrong_answers.index(correct_answer)]

        wrong_answers = random.sample(wrong_answers, 3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

    # Write the question and answer options to the quiz files

    # Questions
        quiz_file.write(f"{question_num + 1}. What is {state_names[question_num]} state's slogan?\n")
    
    # Answer options
        for i in range(4):
            quiz_file.write(f"     {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')
    
    # Write the correct answers to an answer key file
        answer_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")
    
    quiz_file.close()

    answer_file.close()



    

    






    



    



