from Class import user, help_desk_rep, specialist, ticket

print('Please identify who handled this ticket:')
help_desk_rep.rep_id = input('Help Desk Representative ID: ')
help_desk_rep.rep_first_name = input('Help Desk First Name: ')
help_desk_rep.rep_last_name = input('Help Desk Last Name: ')

print('Please enter the ticket user information:')
user.user_id = input('User ID: ')
user.user_first_name = input('User First Name: ')
user.user_last_name = input('User Last Name: ')
user.user_email = input('User Email: ')
user.user_phone = input('User Phone Number: ')
user.user_company = input('User Company Name: ')
user.user_company_address = input('User Company Address: ')

print('Please enter the ticket information:')
ticket.ticket_id = input('Ticket ID: ')
ticket.ticket_opened = input('Ticket Opened: ')
ticket.ticket_desc = input('Ticket Description: ')

answer = 'answer'
while answer != 'yes' or 'Yes' and answer != 'no' or 'No':
    answer = input('Was a specialist required to resolve this issue? Please type "yes" or "no": ')
    if answer == 'yes':
        print('Please enter the required specialist information:')
        specialist.spec_id = input('Specialist ID: ')
        specialist.spec_first_name = input('Specialist First Name: ')
        specialist.spec_last_name = input('Specialist Last Name: ')
        specialist.spec_email = input('Specialist Email: ')
        specialist.spec_phone = input('Specialist Phone Number: ')
        specialist.spec_company = input('Specialist Company Name: ')
        break

    elif answer == 'no':
        break

    else:
        print('Please type "yes" or "no".')
        continue

ticket.ticket_closed = input('Please enter when the ticket was closed and resolved: ')

# while loop that exits when rep quits or archives ticket
selection = 'selection'
while selection != '5':
    print(f'Hello {help_desk_rep.rep_first_name}, what would you like to do?\n'
          '1. Retrieve Ticket Information\n'
          '2. Retrieve User Contact Information\n'
          '3. Retrieve Specialist Information\n'
          '4. Archive Ticket\n'
          '5. Quit')
    selection = input('Please enter your menu selection: ')
    if selection == '1':
        ticket.get_ticket(ticket.ticket_id, user.get_user_contact, help_desk_rep.rep_id, help_desk_rep.rep_first_name, ticket.ticket_desc, ticket.ticket_opened, ticket.ticket_closed)
    elif selection == '2':
        user.get_user_contact(user.user_id, user.user_first_name, user.user_last_name, user.user_email, user.user_phone, user.user_company, user.user_company_address)
    elif selection == '3':
        ticket.get_specialist(specialist.spec_id, specialist.spec_first_name, specialist.spec_email, specialist.spec_company)
    elif selection == '4':
        help_desk_rep.archive_ticket(ticket.get_ticket)
    elif selection == '5':
        print('Goodbye')
        break
    else:
        print('Please enter a number from the selection menu.')
        continue