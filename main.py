# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none

#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None

#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None

#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None

#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',

#                 (Optional) A string 'reverse' to reverse the order

#      Returns: a list of all the services for which the user has a password
#               in the order specified

#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime

class PasswordManager2:
    def __init__(self):
        self.password = {}

    def add(self, service_name, password):
        if self._is_valid_password(password) and service_name not in self.password:
            if all(password != existing_password[0] for existing_password in self.password.values()):
                self.password[service_name] = (password, datetime.now())

    def list_services(self):
        return list(self.password.keys())
    
    def _is_valid_password(self, password):
        if len(password) >= 8 and any(special_chars in password for special_chars in '!@$%&'):
            return True
        else:
            return None
    
    def remove(self, service_name):
        if service_name in self.password:
            del self.password[service_name]

    def update(self, service_name, password):
        if self._is_valid_password(password):
            if service_name in self.password:
                unique_password = all(existing_password != password for existing_service, (existing_password, _) in self.password.items() if existing_service != service_name)
            if unique_password:
                self.password[service_name] = (password, datetime.now())

    def get_for_service(self, service_name):
        return self.password.get(service_name, (None, None))[0]
    
    def sort_services_by(self, key, service=None):
        if key == 'service':
            sorted_services = sorted(self.password.keys())
        elif key == 'added_on':
            sorted_services = sorted(self.password.keys(), key=lambda x: self.password[x][1])
        
        if service == 'reverse':
            sorted_services.reverse()
        return sorted_services