# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

# This method calculates the compatibily between two people.
def calculateLove(name1, name2):

    # Combine names into one string.
    combined_name = name1 + name2
    #print(f"combined name = {combined_name}")

    # Make lower case.
    combined_name = combined_name.lower()
    #print(f"combined name = {combined_name}")

    # Count TRUE.
    total_T = combined_name.count('t')
    total_R = combined_name.count('r')
    total_U = combined_name.count('u')
    total_E = combined_name.count('e')
    #print(f"total t = {total_T}")
    #print(f"total r = {total_R}")
    #print(f"total u = {total_U}")
    #print(f"total e = {total_E}")

    # Save to first_digit.
    first_digit = str(total_T + total_R + total_U + total_E)

    # Count LOVE.
    total_l = combined_name.count('l')
    total_o = combined_name.count('o')
    total_v = combined_name.count('v')
    #print(f"total l = {total_l}")
    #print(f"total o = {total_o}")
    #print(f"total v = {total_v}")
    #print(f"total e = {total_E}")
    # total_e = combined_name.count('e')
    # Save to second_digit.
    second_digit = str(total_l + total_o + total_v + total_E)

    # Get total score (string form)
    total_score = first_digit + second_digit
    # Get total score (int form)
    total_score_int = int(total_score)

    # Interpret scores.
    if total_score_int < 10 or total_score_int > 90:
        print(f"Your score is {total_score_int}, you go together like coke and mentos.")
    elif total_score_int >= 40 and total_score_int <= 50:
        print(f"Your score is {total_score_int}, you are alright together.")
    else:
        print(f"Your score is {total_score_int}.")

calculateLove(name1, name2)
