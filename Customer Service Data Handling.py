# Task 1

def new_ticket (service_tickets, new_ticket):
    while True:
      new_ticket = input("Enter the new ticket number: ")
      if new_ticket not in service_tickets:
          customer_name = input("Enter the customer's name: ")
          customer_issue = input("Enter the issue: ")
          ticket_status = input("Enter ticket status: (open/closed): ")
          service_tickets[new_ticket] = {'Customer' : customer_name, 'Issue' : customer_issue, 'Status' : ticket_status}
          print(f"Service {new_ticket} has been added.")
      else:
          print(f"Service {new_ticket} already exists.")
         
      continue_input = input("Would you like to enter a new service ticket? (yes/no) ").lower()
      if continue_input != 'yes':
        break

def update_ticket_status (service_tickets):
    while True:
        update_ticket = input("What ticket number would you like to update? (ex Ticket001): ")
        if update_ticket in service_tickets:
            if service_tickets[update_ticket]['Status'] == 'closed':
                print(f"{update_ticket} already has a status of closed.") 
            else:
                new_status = service_tickets[update_ticket]['Status'] = 'closed'  
                print(f"{update_ticket} now has a status of {new_status}")          
        else:
            print("That service ticket does not exist!")

        continue_input = input("Would you like to update another ticket status? (yes/no): ").lower()
        if continue_input != 'yes':
            break

def display_all_tickets (service_tickets):
  print("\nAll Service Tickets: ")
  for ticket in service_tickets.items():
    print(ticket)
   
def display_by_status (service_tickets): 
        customer_status_input = input("What status would you like to view? (open/closed)").lower()
        if customer_status_input == 'open':
            print("Open Tickets: ")
            for ticket, status in service_tickets.items():
                if status['Status'] == 'open':
                    print(f"{ticket} Status: {status['Status']}")
        elif customer_status_input == 'closed':
            print("Closed Tickets: ")
            for ticket, status in service_tickets.items():
                if status['Status'] == 'closed':
                    print(f"{ticket} Status: {status['Status']}")
 
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
 
while True:
    print("\n1: Enter a new ticket\n2: Update Ticket Status\n3: Display ALL tickets\n4: Display Tickets by Status\n5: Quit\n")
    
    try:
        choice = input("Choose an option: ")
        if choice == "1":
            new_ticket(service_tickets, new_ticket)
       
        elif choice == "2":
            update_ticket_status(service_tickets)
       
        elif choice == "3":
            display_all_tickets(service_tickets)
       
        elif choice == "4":
            display_by_status(service_tickets)
 
        elif choice == "5":
            print("Thank you for using the Service Ticket Management System!")
            break
    except ValueError:
        print("Invalid entry.  Enter a number from 1 to 5.")
        continue