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

    def load_blacklist_from_file(self, file_path):
        # Load blacklist from a file
        with open(file_path, 'r') as file:
            self.blacklist = file.read().splitlines()

    def load_whitelist_from_file(self, file_path):
        # Load whitelist from a file
        with open(file_path, 'r') as file:
            self.whitelist = file.read().splitlines()

    def clear_blacklist(self):
        # Clear the blacklist
        self.blacklist = []

    def clear_whitelist(self):
        # Clear the whitelist
        self.whitelist = []

    def get_blacklist(self):
        # Get the current blacklist
        return self.blacklist

    def get_whitelist(self):
        # Get the current whitelist
        return self.whitelist

# Usage example:
proxy_firewall = ProxyFirewall()

# Add items to the blacklist
proxy_firewall.add_to_blacklist("example.com")
proxy_firewall.add_to_blacklist("malicious-keyword")

# Add items to the whitelist
proxy_firewall.add_to_whitelist("trusted-domain.com")

# Test content filtering
print(proxy_firewall.content_filtering("https://example.com/page"))  # Blocked
print(proxy_firewall.content_filtering("https://trusted-domain.com/page"))  # Allowed
print(proxy_firewall.content_filtering("https://other-domain.com/page"))  # Blocked

# Load blacklist and whitelist from files
proxy_firewall.load_blacklist_from_file("blacklist.txt")
proxy_firewall.load_whitelist_from_file("whitelist.txt")

# Clear the blacklist and whitelist
proxy_firewall.clear_blacklist()
proxy_firewall.clear_whitelist()

# Get the current blacklist and whitelist
print(proxy_firewall.get_blacklist())
print(proxy_firewall.get_whitelist())
