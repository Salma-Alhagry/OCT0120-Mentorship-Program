def eval_loop():
    """Iteratively prompts the user, takes the resulting input and evaluates it
    using eval, and prints the result.
    It should continue until the user enters 'done', and then return the value of
    the last expression it evaluated.
    """
    while True:
        user_input = input(">")
        
        if eval(user_input) == 'done':  
            break
        print(eval(user_input))

    return eval(user_input)

eval_loop()
