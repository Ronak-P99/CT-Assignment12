import re
def extract_emails():
    # Read the file and use regex to find and return all email addresses
    with open('contacts.txt', 'w') as file_object:
        contents = file_object.write("\nJohn Doe - john.doe@example.com\nJane Smith - jane.smith@gmail.com\n\nFor inquiries, please contact info@example.com")
    with open('contacts.txt', 'r') as file_object:
        contents = file_object.read()
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", contents)        
        print(contents)
    print(f"\nPulled Emails are:\n{emails}\n")
    


extract_emails()