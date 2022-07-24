email = input("Enter your email address: ")

if '@' in email:
    print(f"Your username is: {email[:email.index('@')]}")
    print(f"Your domain is: {email[email.index('@')+1:]}")