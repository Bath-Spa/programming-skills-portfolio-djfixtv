# Define the initial glossary with programming terms and their meanings
glossary = {
    'variable': 'A named storage location in the computer\'s memory, used to store data that can be modified during program execution.',
    'function': 'A reusable block of code that performs a specific task. Functions help in organizing code and promoting code reusability.',
    'loop': 'A programming construct that repeats a set of instructions until a specified condition is met. Common types include for and while loops.',
    'conditional statement': 'A construct that allows a program to make decisions based on certain conditions. Common examples include if, elif, and else statements.',
    'list': 'A collection of ordered and mutable elements in Python. Lists are defined using square brackets [] and can store different data types.'
}

# Print each word and its meaning using a loop
for term, meaning in glossary.items():
    print(term.capitalize() + ":", meaning + "\n")

# Add five more Python terms to the glossary
glossary['dictionary'] = 'A collection of key-value pairs, where each key must be unique. Similar to a glossary, it allows quick lookups of meanings.'
glossary['tuple'] = 'An ordered and immutable collection of elements in Python, defined using parentheses ().'
glossary['module'] = 'A file containing Python definitions and statements. It can be used to organize code into reusable and importable units.'
glossary['class'] = 'A blueprint for creating objects in Python. It defines a set of attributes and methods that the objects created from the class will have.'
glossary['exception'] = 'An event that occurs during the execution of a program and disrupts the normal flow of instructions. Python provides a way to handle exceptions using try and except blocks.'

# Print the updated glossary using a loop
for term, meaning in glossary.items():
    print(term.capitalize() + ":", meaning + "\n")
