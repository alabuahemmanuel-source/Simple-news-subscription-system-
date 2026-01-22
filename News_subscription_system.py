subscribers = []

def add_subscriber():
    name = input("Enter subscriber name: ")
    email = input("Enter email address: ")
    subscribers.append({
        "name": name,
        "email": email
    })
    print("Subscription successful")

def view_subscribers():
    if not subscribers:
        print("No subscribers found")
    else:
        for s in subscribers:
            print("Name:", s["name"], "| Email:", s["email"])

def main():
    while True:
        print("1. Add Subscriber")
        print("2. View Subscribers")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_subscriber()
        elif choice == "2":
            view_subscribers()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
