import re
import nltk
import firebase
from nltk.corpus import wordnet

def build_keywords(words_list, synonyms_list):
    for word in words_list:
        synonyms= []
        for syn in wordnet.synsets(word):
            for lem in syn.lemmas():
                # Remove any special characters from synonym strings
                lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
                synonyms.append(lem_name)

        # add custom synonyms
        add_synonyms(word, synonyms)

        synonyms_list[word]=set(synonyms)
        

# set up categories of questions
def setup_topics(keys, keywords):
    for key in keys:
        keywords[key] = []

def add_synonyms(key, synonyms):
    syns = []
    if key == 'fellowship':
        syns = ['fellow', 'fellows']
    elif key == 'membership':
        syns = ['member', 'members']
    elif key == 'merch':
        syns = ['merchandise', 'shop']
    elif key == 'internships':
        syns = ['intern', 'opportunity', 'job', 'jobs']
    elif key == 'join':
        syns = ['sign up']
    elif key == 'reapply':
        syns = ['sign up again', 'apply again']
    elif key == 'time':
        syns = ['duration', 'long', 'length']
    elif key == 'postgrad':
        syns = ['masters', 'phd', 'postundergrad']
    elif key == 'application':
        syns = ['apply', 'app']
    elif key == 'give referrals':
        syns = ['offer referrals']
    elif key == 'RTC':
        syns = ['rewriting the code']
    elif key == 'senior undergraduate':
        syns = ['senior undergrad', 'fourth year undergrad', 'fourth year', '4th year', '4th year undergrad', 'senior year']
    elif key == 'guidelines':
        syns = ['guide']
    elif key == 'requirements':
        syns = ['eligibility', 'eligible', 'qualify', 'qualifications']
    synonyms.extend(syns)

def build_intents(keys, keywords, keywords_dict):
    for key in keys:
        # Defining a new key in the keywords dictionary
        keywords[key].append('.*\\b'+key+'\\b.*')
        # Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters 
        for synonym in list(synonyms_list[key]):
            keywords[key].append('.*\\b'+synonym+'\\b.*')

    for intent, keys in keywords.items():
        # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
        keywords_dict[intent]=re.compile('|'.join(keys))

def select(intents):
    matched_intent = None
    if 'postgrad' in intents and 'fellowship' in intents:
        matched_intent = 'postgrad fellow'
    elif 'fellowship' in intents and 'time off' in intents:
        matched_intent = 'fellowship participation'
    elif 'fellowship' in intents and 'time' in intents:
        matched_intent = 'fellowship time'
    elif 'senior undergraduate' in intents and 'fellowship' in intents:
        matched_intent = 'senior fellow'
    elif 'international' in intents and 'fellowship' in intents:
        matched_intent = 'international fellow'
    elif 'current fellow' in intents and 'reapply' in intents:
        matched_intent = 'current fellow reapply'
    elif 'internship' in intents and 'fellowship' in intents:
        matched_intent = 'internship fellow'
    elif 'internship' in intents and 'paid' in intents and 'partner' in intents:
        matched_intent = 'paid internship partner'
    elif 'secured internship' in intents and 'fellowship':
        matched_intent = 'secured internship fellowship'
    elif 'membership' in intents and 'join' in intents:
        matched_intent = 'membership'
    elif 'housing' in intents:
        matched_intent = 'housing'
    elif 'give referrals' in intents:
        matched_intent = 'give referral'
    elif 'scholarships' in intents and 'requirements' in intents:
        matched_intent = 'scholarship requirements'
    elif 'international' in intents and 'scholarships' in intents:
        matched_intent = 'international scholarships' 
    return matched_intent
# have to check for multiple keywords for different questions
def run():
    print('What is your question for RTC?')
    # While loop to run the chatbot indefinetely
    while (True):  
        # Takes the user input and converts all characters to lowercase
        # remove special characters
        user_input = re.sub('[^a-zA-Z0-9 \n\.]', ' ', input().lower())
        
        # Defining the Chatbot's exit condition
        if user_input == 'quit': 
            print ("Thank you for visiting.")
            break    
        
        matched_intent = None 
        intents = set() # to get more nuanced responses for certain keywords
        intent_word_list = []

        for intent,pattern in keywords_dict.items():
            # Using the regular expression search function to look for keywords in user input
            if re.search(pattern, user_input): 
                # split intent into single words
                intent_word_list = intent.split()
                # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
                intents.add(intent)
                
                matched_intent = intent

        # The fallback intent is selected by default
        key='default' 
        if len(intents) > 1:
            # create custom cases for specific intents
            matched_intent = select(intents)
        if matched_intent in responses:
            # If a keyword matches, the fallback intent is replaced by the matched intent as the key for the responses dictionary
            key = matched_intent 
        # The chatbot prints the response that matches the selected intent
        print(responses[key])
        
# Building a list of Keywords
words_list = firebase.wordArr
synonyms_list = {} 

# Building dictionary of Intents & Keywords
keywords = {}
keywords_dict = {}

# Create topics for questions that will serve as keys in keyword dictionary
topic_keys = firebase.keyArr


responses = firebase.responsesDict
build_keywords(words_list, synonyms_list)
setup_topics(topic_keys, keywords)
build_intents(topic_keys, keywords, keywords_dict)

run()