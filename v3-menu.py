import re

class ProxyFirewall:
    def __init__(self):
        self.blacklist = []  # List of blocked URLs, domains, or keywords
        self.whitelist = []  # List of allowed URLs, domains, or keywords

    def content_filtering(self, data):
        # Implement content filtering rules to examine and filter data
        if self.is_blocked(data):
            return False  # Block data
        elif self.is_allowed(data):
            return True  # Allow data
        else:
            return False  # Block data (default)

    def is_blocked(self, data):
        # Check if the data matches any item in the blacklist
        for item in self.blacklist:
            if re.search(item, data, re.IGNORECASE):
                return True
        return False

    def is_allowed(self, data):
        # Check if the data matches any item in the whitelist
        for item in self.whitelist:
            if re.search(item, data, re.IGNORECASE):
                return True
        return False

    def add_to_blacklist(self, item):
        # Add an item to the blacklist
        self.blacklist.append(item)

    def remove_from_blacklist(self, item):
        # Remove an item from the blacklist
        if item in self.blacklist:
            self.blacklist.remove(item)

    def add_to_whitelist(self, item):
        # Add an item to the whitelist
        self.whitelist.append(item)

    def remove_from_whitelist(self, item):
        # Remove an item from the whitelist
        if item in self.whitelist:
            self.whitelist.remove(item)

    def show_menu(self):
        while True:
            print("\nProxy Firewall Menu:")
            print("1. Add to Blacklist")
            print("2. Remove from Blacklist")
            print("3. Add to Whitelist")
            print("4. Remove from Whitelist")
            print("5. Test Content Filtering")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                item = input("Enter the item to add to the blacklist: ")
                self.add_to_blacklist(item)
                print("Item added to the blacklist.")
            elif choice == "2":
                item = input("Enter the item to remove from the blacklist: ")
                self.remove_from_blacklist(item)
                print("Item removed from the blacklist.")
            elif choice == "3":
                item = input("Enter the item to add to the whitelist: ")
                self.add_to_whitelist(item)
                print("Item added to the whitelist.")
            elif choice == "4":
                item = input("Enter the item to remove from the whitelist: ")
                self.remove_from_whitelist(item)
                print("Item removed from the whitelist.")
            elif choice == "5":
                data = input("Enter the data to test content filtering: ")
                if self.content_filtering(data):
                    print("Content allowed.")
                else:
                    print("Content blocked.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

# Usage example:
proxy_firewall = ProxyFirewall()

# Add a disclaimer
print("Disclaimer: This proxy firewall script is provided for educational purposes only. Use it responsibly and in accordance with applicable laws and regulations.")

# Show the menu
proxy_firewall.show_menu()

# Add your name
print("Script developed by Tadash10)
