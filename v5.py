import re
import json
import logging

class ProxyFirewall:
    def __init__(self):
        self.blacklist = []  # List of blocked URLs, domains, or keywords
        self.whitelist = []  # List of allowed URLs, domains, or keywords
        self.logger = self.setup_logger()

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
        self.blacklist = [i for i in self.blacklist if i != item]

    def add_to_whitelist(self, item):
        # Add an item to the whitelist
        self.whitelist.append(item)

    def remove_from_whitelist(self, item):
        # Remove an item from the whitelist
        self.whitelist = [i for i in self.whitelist if i != item]

    def load_configuration(self, file_path):
        # Load blacklist and whitelist from a configuration file
        try:
            with open(file_path, 'r') as file:
                config = json.load(file)
                self.blacklist = config.get('blacklist', [])
                self.whitelist = config.get('whitelist', [])
        except FileNotFoundError:
            self.logger.error(f"Configuration file '{file_path}' not found.")
        except json.JSONDecodeError:
            self.logger.error(f"Invalid JSON format in configuration file '{file_path}'.")

    def save_configuration(self, file_path):
        # Save current blacklist and whitelist to a configuration file
        config = {'blacklist': self.blacklist, 'whitelist': self.whitelist}
        try:
            with open(file_path, 'w') as file:
                json.dump(config, file, indent=2)
        except IOError:
            self.logger.error(f"Error saving configuration to file '{file_path}'.")

    def validate_rules(self):
        # Validate the integrity and correctness of the blacklist and whitelist entries
        unique_items = set(self.blacklist + self.whitelist)
        if len(unique_items) != len(self.blacklist) + len(self.whitelist):
            self.logger.warning("Duplicate entries found in blacklist or whitelist.")
        
        for item in unique_items:
            if not self.is_valid_rule(item):
                self.logger.warning(f"Invalid rule found: {item}")

    def is_valid_rule(self, item):
        # Validate a single rule for URLs, domains, or keywords
        # Add your validation logic here (e.g., check for valid regex)
        try:
            re.compile(item)
            return True
        except re.error:
            return False

    def setup_logger(self):
        # Setup logging configuration
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        return logger

# Usage example:
proxy_firewall = ProxyFirewall()

# Load configuration from a file
proxy_firewall.load_configuration('config.json')

# Validate the rules
proxy_firewall.validate_rules()

# Add an item to the blacklist
proxy_firewall.add_to_blacklist("example.com")

# Save configuration to a file
proxy_firewall.save_configuration('config.json')

# Test content filtering
print(proxy_firewall.content_filtering("https://example.com/page"))  # Blocked
