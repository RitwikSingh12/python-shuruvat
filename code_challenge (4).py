# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
people = int(input('enter number of people in the stupid list\n'))
for stupid in range(0,people):
    Fname = input("enter your first name")
    if Fname[0] == 'A' or Fname[0] == 'B':
        print('go to room AB')
    elif Fname[0] == 'C':
        orint('go to room CD')
    else:
        Lname = input('enter your last name')
        if Lname[0] == 'Z':
            print('go get your stupid arse to room Z')
        else:
            print('now listen, GO TO ROOM OTHERR!')
