# Define a glossary with programming terms and their meanings
glossary = {
    'variable': 'A named storage location in the computer\'s memory, used to store data that can be modified during program execution.',
    'function': 'A reusable block of code that performs a specific task. Functions help in organizing code and promoting code reusability.',
    'loop': 'A programming construct that repeats a set of instructions until a specified condition is met. Common types include for and while loops.',
    'conditional statement': 'A construct that allows a program to make decisions based on certain conditions. Common examples include if, elif, and else statements.',
    'list': 'A collection of ordered and mutable elements in Python. Lists are defined using square brackets [] and can store different data types.'
}

# Print each word and its meaning as neatly formatted output
for term, meaning in glossary.items():
    print(term.capitalize() + ":", meaning + "\n")
