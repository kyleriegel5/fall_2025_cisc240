class user:
    def __init__(self, user_id, user_first_name, user_last_name, user_email, user_phone, user_company, user_company_address):
        self.UserID: int = user_id
        self.UserFirstName: str = user_first_name
        self.UserLastName: str = user_last_name
        self.UserEmail: str = user_email
        self.UserPhone: str = user_phone
        self.UserCompany: str = user_company
        self.UserCompanyAddress: str = user_company_address

    def get_user_contact(self, user_id, user_first_name, user_last_name, user_email, user_phone, user_company, user_company_address):
        return print('\nFirst Name: ' + user_first_name,
              '\nLast Name: ' + user_last_name,
              '\nID: ' + user_id,
              '\nEmail: ' + user_email,
              '\nPhone: ' + user_phone,
              '\nCompany: ' + user_company,
              '\nCompany Address: ' + user_company_address)

class help_desk_rep:
    def __init__(self, rep_id, rep_first_name, rep_last_name):
        self.RepID = rep_id
        self.RepFirstName = rep_first_name
        self.RepLastName = rep_last_name

    def archive_ticket(self, get_ticket):
        return print('The following ticket was archived:\n' + get_ticket)

class specialist:
    def __init__(self, spec_id, spec_first_name, spec_last_name, spec_email, spec_phone, spec_company):
        self.SpecID = spec_id
        self.SpecFirstName = spec_first_name
        self.SpecLastName = spec_last_name
        self.SpecEmail = spec_email
        self.SpecPhone = spec_phone
        self.SpecCompany = spec_company

class ticket:
    def __init__(self, ticket_id, ticket_desc, ticket_opened, ticket_closed):
        self.TicketID = ticket_id
        self.TicketDesc = ticket_desc
        self.TicketOpened = ticket_opened
        self.TicketClosed = ticket_closed

    def get_ticket(self, ticket_id, get_user_contact, rep_id, rep_first_name, ticket_desc, ticket_opened, ticket_closed):
        return print('\nTicket ID: ' + ticket_id,
                     '\nOpened: ' + ticket_opened,
                     '\nHelp Desk Rep: ' + rep_first_name,
                     '\nRep ID: ' + rep_id,
                     '\nUser Contact: ' + get_user_contact(),
                     '\nDescription: ' + ticket_desc,
                     '\nClosed: ' + ticket_closed,
                     )

    def get_specialist(self, spec_id, spec_first_name, spec_email, spec_company):
        return print('\nSpec ID: ' + spec_id,
                     '\nFirst Name: ' + spec_first_name,
                     '\nEmail: ' + spec_email,
                     '\nCompany: ' + spec_company
                     )
