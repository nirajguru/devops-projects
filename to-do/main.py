user_prompt = "Enter a to-do item: "

todos= []

while True:

    todo = input(user_prompt)
    todos.append(todo)  # Adding items to the list
    # capitalize() method returns a copy of the string with only its first cletter/ character capitalized.
    # title() method returns a copy of the string in which first letter of all the words are capitalized.
    print(todos)