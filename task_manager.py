#=====importing libraries===========
from datetime import datetime

#====Login Section====
user_exists = False

while user_exists == False:

    correct_name = False
    correct_pass = False
    
    # Prompt user to login
    user_name = input("Enter user name: ").lower()
    password = input("Enter password: ").lower()

    user_file = open("user.txt", "r")

    # Validate user login
    for line in user_file:

        line = line.strip("\n")
        user = line.split(", ")
        # check user name and password
        if user_name == user[0]:
            correct_name = True
        
        if password == user[1]:
            correct_pass = True

    # Close file
    user_file.close()

    if correct_name == True and correct_pass == False:
        print("You have entered an incorect password")
        correct_name = False

    elif correct_name == False and correct_pass == True:
        print("You have entered an incorect user name")
        correct_pass = False

    elif correct_name == True and correct_pass == True:
        user_exists = True
        print(user_exists)
        print("successfully logged in")

    else:
        print("Incorrect inputs!")

while user_exists:
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    
    # Check if user is an admin and display
    # a menu with an additional option
    if user_name == "admin":

        menu = input('''Select one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            s  - Display statistics
            e - Exit
            : ''').lower()
    else:

        menu = input('''Select one of the following Options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - view my task
                e - Exit
                : ''').lower()

    if menu == 'r':

        # check if the user is an admin before registering user
        if user_name == "admin":
            user_name = input("Enter a user name: ").lower()
            password = input("Enter a password: ").lower()
            conf_pass = input("Please confirm the password: ").lower()
            
            # Check if the new password and confirmed password are the same
            if password == conf_pass:

                # open the user file and register a user
                user_file = open("user.txt", "a")
                user_file.write("\n" + user_name + ", " + password)
                
                # Close the file
                user_file.close()
            else:
                print("Passwords do not match!") 
        else:
            print("Only an admin can register a user")

    elif menu == 'a':
        
        # Prompt user to enter task information
        task_person = input("Enter the name fo the person being assigned the task: ").lower()
        task_name = input("Enter the title of the task: ").lower()
        task_desc = input("Enter the task description: ").lower()
        task_due_date = input("Enter the due date for the task(dd Mon yyyy): ")
        is_complete = input("Has the task been comppleted?: ") 

        # Get the currwnt date and formate it accordingly
        current_date = datetime.now()
        assign_date = current_date.strftime("%d %b %Y")

        # Open task file
        task_file = open("tasks.txt", "a")

        # Write to task file
        task_file.write(task_person + ", " + task_name + ", " + task_desc + ", " + assign_date + ", " + task_due_date + ", " + is_complete + "\n")
        
        # Close task file
        task_file.close()

    elif menu == 'va':

        # Open the task file
        task_file = open("tasks.txt", "r")

        for line in task_file:

            # Split the line,  remove the comma and space and store it in a list
            split_line = line.split(", ")
            print("Task:\t\t\t" + split_line[1] + "\nAssigned to:\t\t" + split_line[0] + "\nDate assigned:\t\t" + split_line[3] + "\nDueDate:\t\t" + split_line[4] + "\nTask Complete?:\t\t" + split_line[5] + "\nTask description:\t" + split_line[2] + "\n\n")

        task_file.close()

    elif menu == 'vm':

        # Open the task file
        task_file = open("tasks.txt", "r")

        for line in task_file:

            # Split the line,  remove the comma and space and store it in a list
            split_line = line.split(", ")

            if split_line[0] == user_name:
                print("Task:\t\t\t" + split_line[1] + "\nAssigned to:\t\t" + split_line[0] + "\nDate assigned:\t\t" + split_line[3] + "\nDueDate:\t\t" + split_line[4] + "\nTask Complete?:\t\t" + split_line[5] + "\nTask description:\t" + split_line[2] + "\n\n")

        task_file.close()

    elif menu == 's':
        # make sure user is an admin
        if user_name == 'admin':

            user_count = 0
            task_count = 0
            user_file = open("user.txt", "r")

            # count number of users
            for user in user_file:
                user_count += 1    

            # close user file
            user_file.close()

            # Open task file
            task_file = open("tasks.txt", "r")

            # Count number of tasks
            for task in task_file:
                task_count += 1

            # Close tasks file
            task_file.close()

            # Display all statistics
            print("Number of users: " + str(user_count))
            print("Number of tasks: " + str(task_count))

        else:
            print("Only admin is authorised for this action!")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")