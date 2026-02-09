{
    "id":1,
    "title": "Login issue",
    "description": "User cannot log in",
    "status": "open"
}

tickets = []
ticket_id = 1

while True:
    print("\nSupport Ticket Tracker")
    print("1. Create Ticket")
    print("2. View tickets")
    print("3. Update ticket status")
    print("4. Exit")

    choice = input("Select an option (1-4): ").strip()

    if choice == "1":
        title = input("Enter ticket title: ").strip()
        description = input("Enter ticket description: ").strip()

        ticket = {
            "id": ticket_id,
            "title": title,
            "description": description,
            "status": "open"
        }

        tickets.append(ticket)
        ticket_id += 1

        print("Ticket created successfully.")
    elif choice == "2":
        if not tickets:
            print("No tickets found.")
        else:
            print(
                f"ID: {ticket['id']} | "
                f"Title: {ticket['title']} | "
                f"Status: {ticket['status']}"
            )    
    elif choice == "3":
        ticket_number = input("Enter ticket ID to update: ").strip()

        found = False
        for ticket in tickets:
            if str(ticket["id"]) == ticket_number:
                new_status = input("Enter new status (Open / In Progress / Closed): ").strip()
                ticket["status"] = new_status
                found = True
                print("Ticket updated successfully.")
                break
        
        if not found:
            print("Ticket ID not found.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid selection. Try again.")