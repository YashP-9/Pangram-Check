user_input = input("What sentence would you like to check? ")

def pangram_or_not(user_input):
    user_input = user_input.lower()
    alphabets = {
    }

for i in user_input:
    if i.isalpha():
        alphabets[i] = True

if len(alphabets) == 26:
    return True
else:
    return False


if pangram_or_not(user_input):
    print("Your sentence is a pangram!")
else: 
    print ("Your sentence is not a pangram.")
