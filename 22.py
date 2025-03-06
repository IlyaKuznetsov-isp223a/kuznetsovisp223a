import re
class Validator:
    def isEmail(self, string):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, string))
    def isDomain(self, string):
        pattern = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
        return bool(re.match(pattern, string))
    def isNumber(self, string):
        return string.isdigit()
validator = Validator()
email_to_check = "test@example.com"
domain_to_check = "example.com"
number_to_check = "12345"
invalid_email = "invalid-email"
invalid_domain = "invalid_domain"
non_number = "abc123"
print(f"'{email_to_check}' is valid email: {validator.isEmail(email_to_check)}")
print(f"'{domain_to_check}' is valid domain: {validator.isDomain(domain_to_check)}")
print(f"'{number_to_check}' is valid number: {validator.isNumber(number_to_check)}")
print(f"'{invalid_email}' is valid email: {validator.isEmail(invalid_email)}")
print(f"'{invalid_domain}' is valid domain: {validator.isDomain(invalid_domain)}")
print(f"'{non_number}' is valid number: {validator.isNumber(non_number)}")
