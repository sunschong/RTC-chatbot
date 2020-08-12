# Rewriting the Code (RTC) Chatbot Infrastructure

**Problem Statement:** RTC leadership often struggles with a huge volume of repetitive questions from students about different RTC procedures. There is room to automate this process so that leaders aren’t bogged down with menial questions and so that there is a single source of information for common questions that can get people instantaneous answers. On the backend, we could track common questions and make sure that the chat bot is updated with the most relevant information. A simpler scope project would have this learning be manual, a more complex project could use some AI in the background.

## Project Scope
- Collecting the commonly asked questions
- Creating a database
- Creating a model and is able to run on the said database with all the key performance indicators
- Test model

## Desired End Result
A chatbot that is presentable and accessible. The goal is for it to be efficient and informative. The bot is able to work with the following conditions:
- Synonyms
- spelling mistakes
- case sensitivity
- incomplete sentences
- Multiple questions

## Our Approach
A rule-based chatbot that uses Python to match appropriate responses to questions and Firebase for data storage and retrieval. With more time for the project, some modifications could be made to improve the chatbot, such as retrieving the synonyms from the database instead and changing the way we check for keywords.


