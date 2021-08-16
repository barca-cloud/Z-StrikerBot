import os

def lichess():
    program = "python3"
    arguments = ["lichess-bot.py","-u"]
    print(os.execvp(program, (program,) +  tuple(arguments)))
lichess()    
© 2021 GitHub, Inc.
