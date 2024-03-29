import json
'''
    Contact Management System:
        --> Add Contacts
        --> Search for Contacts
        --> Remove Contacts
        --> Update Contacts
'''


def read_to_py_dictionary():  # checks if the exits, reads the retrieved json data to contacts_dictionary
    try:                      # or returns 'File not found!!!' message
        with open('contacts.json', 'r') as outfile:
            contacts_dictionary = json.loads(outfile.read())
            return contacts_dictionary
    except FileNotFoundError:
        print()
        print('File not found!!!')


def write_to_contacts_file(dictionary_to_json_var):  # writes specified dictionary to contacts.json file
    with open('contacts.json', 'w') as outfile:
        outfile.write(json.dumps(dictionary_to_json_var, indent=4))


def display_all_or_range_of_contacts():
    # display user requested contacts based-on ALL, RANGE, LAST_N, FIRST_N
    contacts_dictionary = read_to_py_dictionary()
    range_of_contacts = 0
    # contacts_dictionary = json.dumps(contacts_dictionary, indent=4)
    while range_of_contacts != 'QUIT':
        try:
            print()
            question_response = input('''[ ALL | RANGE | FIRST_N | LAST_N ]
>>> "ALL" to display every contact.
>>> "RANGE" to select from a specified range. 
>>> "FIRST_N" to select the first N contacts.
>>> "LAST_N" to select the last N contacts.
            
Select from an option of above:  ''')
            if question_response not in ['ALL', 'RANGE', "FIRST_N", "LAST_N"]:
                print()
                print('Invalid Input!!!')
                continue
            elif question_response == 'ALL':
                print()
                print(json.dumps(contacts_dictionary['contacts'], indent=4))
                break
            elif question_response == 'RANGE':
                while True:
                    print()
                    try:
                        start_range_number = int(input('Enter first number in the range: '))
                        end_range_number = int(input('Enter last number in the range: '))
                        requested_output = contacts_dictionary['contacts'][start_range_number:end_range_number + 1]
                        print(json.dumps(requested_output, indent=4))
                        break
                    except ValueError:
                        print('Invalid input!!! Enter number [0, 1, 3, etc...]!!!')
                        print()
                        continue
                break
            elif question_response == 'FIRST_N':
                while True:
                    print()
                    try:
                        end_number = int(input('Enter number to display first N contacts: '))
                        requested_output = contacts_dictionary['contacts'][:end_number + 1]
                        print(json.dumps(requested_output, indent=4))
                        break
                    except ValueError:
                        print('Invalid input!!! Enter number [0, 1, 3, etc...]!!!')
                        print()
                        continue
                break
            else:  # executes if question_response == 'LAST_N'
                while True:
                    print()
                    try:
                        end_number = int(input('Enter number to display last N contacts: '))
                        requested_output = contacts_dictionary['contacts'][-end_number:]
                        print(json.dumps(requested_output, indent=4))
                        break
                    except ValueError:
                        print('Invalid input!!! Enter number [0, 1, 3, etc...]!!!')
                        print()
                        continue
                break
        except ValueError:
            print('Invalid input!!! Enter number [0, 1, 3, etc...]!!!')
            print()
            continue


def add_contact():
    # Asks user for contact's name, phone number, and email, inserts information into contact
    # python dictionaries, appends the contacts_dictionary if the file exists, writes new_doc_contacts_dict
    # dictionary to a new document if the file DOES NOT exist.
    contacts_dictionary = read_to_py_dictionary()
    while True:
        contact_name = input("Enter contact's name: ")
        contact_name = contact_name.upper()
        contact_phone_number = input("Enter contact's phone number (xxx-xxx-xxxx): ")
        contact_email = input("Enter contact's email (xxx@xxx.com): ")
        contact_email = contact_email.upper()
        contact_dict = {'name': contact_name, 'phone number': contact_phone_number, 'email': contact_email}
        new_doc_contacts_dict = {'contacts': [{'name': contact_name,
                                              'phone number': contact_phone_number,
                                               'email': contact_email}]}
        try:
            contacts_dictionary['contacts'].append(contact_dict)
            write_to_contacts_file(contacts_dictionary)
            print('COMPLETED!!!')
            break
        except (FileNotFoundError, KeyError, TypeError):
            write_to_contacts_file(new_doc_contacts_dict)
            print('COMPLETED!!!')
            break


def search_contact():
    contacts_dictionary = read_to_py_dictionary()
    while True:
        name_to_search = input('Enter the name you want to search for or [QUIT]: ')
        name_to_search = name_to_search.upper()
        try:
            name_list = [contact['name'] for contact in contacts_dictionary['contacts']]
            if name_to_search == 'QUIT':
                break
            elif name_to_search not in name_list:
                print('Contact not found!!!')
                continue
            else:
                for contact in contacts_dictionary['contacts']:
                    if contact['name'] == name_to_search:
                        print(json.dumps(contact, indent=4))
                        break
        except TypeError:  # Prevents errors from the contacts.json file not being found
            break          # to include the error with trying to search the dictionary.


def update_contact():
    # Function searches through all contacts for the user specified name, and updates the user targeted info
    # and updates the Name, Phone Number, or Email as specified by the user.
    contacts_dictionary = read_to_py_dictionary()
    while True:
        try:
            contact_to_update = input('Enter name of the contact you want to update or [QUIT]: ')
            contact_to_update = contact_to_update.upper()
            contact_names_list = [contact['name'] for contact in contacts_dictionary['contacts']]
            if contact_to_update == 'QUIT':
                break
            # checks if the specified name has a contact entry in the contacts.json document
            elif contact_to_update not in contact_names_list:
                print('Contact not found!!!')
                continue
            else:
                for contact in contacts_dictionary['contacts']:
                    if contact['name'] == contact_to_update:
                        # Define info_to_update before the while loop to avoid potential reference before assignment
                        info_to_update = 0
                        # Request user input to assign info_to_update a value from 1 to 3. If the user
                        # inputs a non-integer value, the except will be thrown. If the value is not [1, 2, or 3]
                        # an error message will be outputted and the question will be asked again.
                        while True:
                            try:
                                info_to_update = int(input('''[0. QUIT | 1. Name | 2. Phone Number | 3. Email]
    Enter the a 0, 1, 2, or 3 for what you want to update: '''))
                                if info_to_update in [1, 2, 3]:
                                    break
                                elif info_to_update == 0:
                                    break
                                else:
                                    print('Invalid input!!! Enter number 0 to quit or 1, 2, or 3 for option!!!')
                                    continue
                            except ValueError:
                                print('Invalid input!!! Enter number 0 to quit or 1, 2, or 3 for option!!!')
                                continue
                        # For loop goes through each contact in the contacts dictionary, if statements
                        # checks which value the user wants to update, if the name in contact is the
                        # same as the user selected name the value will be updated.
                        if info_to_update == 1:
                            update_value = input('Enter new name: ')
                            update_value.upper()
                            contact['name'] = update_value
                            write_to_contacts_file(contacts_dictionary)
                            break
                        elif info_to_update == 2:
                            update_value = input('Enter new phone number: ')
                            contact['phone number'] = update_value
                            write_to_contacts_file(contacts_dictionary)
                            break
                        elif info_to_update == 3:                           # for infor_to_update == 3 or email
                            update_value = input('Enter new email: ')
                            update_value.upper()
                            contact['email'] = update_value
                            write_to_contacts_file(contacts_dictionary)
                            break   # breaks the for loop that loops through the contacts_dictionary
                break   # breaks the top while loop to end the function
        except TypeError:
            print('File does not exist!!!')
            break


def remove_contact():
    # function asks the user to specify the name of the contact they want to remove, removes the contact
    # if found, if contact is not found then they are ask again for another contact name
    contacts_dictionary = read_to_py_dictionary()
    while True:
        contact_to_remove = input('Enter contacts name that you want to remove or [QUIT]: ')
        contact_to_remove = contact_to_remove.upper()
        try:
            contact_names_list = [contact['name'] for contact in contacts_dictionary['contacts']]
            if contact_to_remove == 'QUIT':
                break
            elif contact_to_remove not in contact_names_list:
                print('Contact not found!!!')
                break
            else:
                for contact in contacts_dictionary['contacts']:
                    if contact['name'] == contact_to_remove:
                        contacts_dictionary['contacts'].remove(contact)
                        write_to_contacts_file(contacts_dictionary)
                        print('Completed!!!')
                        break
                break
        except TypeError:
            print('File does not exist!!!')
            break


function_to_perform = ''
while function_to_perform != 'quit':
    print('\n\n\n')
    print('''######################################################
This program will allow you to manage your contacts (Name, Phone Number, &
Email) from the contacts.json document.
######################################################''')
    print()
    print('[ QUIT | ADD | UPDATE | SEARCH | RANGE | DELETE ]')
    function_to_perform = input('Enter function you would like to perform: ')
    print()

    function_to_perform = function_to_perform.upper()

    if function_to_perform == 'QUIT':
        break
    elif function_to_perform == 'ADD':
        add_contact()
    elif function_to_perform == 'UPDATE':
        update_contact()
    elif function_to_perform == 'SEARCH':
        search_contact()
    elif function_to_perform == 'RANGE':
        display_all_or_range_of_contacts()
    elif function_to_perform == 'DELETE':
        remove_contact()
    else:
        print('Invalid input!!! Try again!!!')
        continue
