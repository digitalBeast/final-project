#copy and paste to your python shell to run it

#BESTFRIEND similator is to make choices to interact with the computer(your bestfriend).



import random
print('BESTFRIEND SIMILATOR.\n')
    
print('COMPUTER: How are you today? [Response choice: "ok", "good", "bad"]')

responses = input()

if responses == "ok":
    print('COMPUTER: just ok?, is it about the final exam? [Response choice: "yes", "no", "maybe"]')
    if responses == "yes":
            print('Don\'t you worry, you got the skill and spirit to pass it!')
    elif responses == "no":
            print('oh ok, hmmm you should be fine then! tell me you like the music?')
    elif responses == "maybe":
            print('hmm I see you don\'t know...don\'t be hiding now')
    
elif responses == 'bad':
    print('COMPUTER: Oh no! what happen? [Response choice: "sick", "failing class", "angry"]')
elif responses == 'good':
    print('COMPUTER: That\'s wonderful, what made you happy? [Response choice: "passing class", "summer time", "just happy"')
 




        


        
    


