#Task 4b King Letter
'''
Task 4b King Letter (2marks)

Add to the code from part 1 to change the output when a number is 
greater than 100 to show for example:

=========================
How old are you? 111
You already got your letter 11 years ago
========================= 

'''
def main():
    x="Task4b"
    #===============================
    # Write your code here
    age = int(input("How old are you? ")) # Ask for user input
    years_until_letter = 100 - age # Calculate years until the letter
    if years_until_letter > 0:
        print("Years until your letter...")
        print(years_until_letter) # Print years until the letter
    else:
        years_over = -years_until_letter # Calculate how many years ago they received the letter
        print(f"You already got your letter {years_over} years ago")

    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
