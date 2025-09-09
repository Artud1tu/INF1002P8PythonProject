# INF1002P8PythonProject
Python Project

whitelist = ['gmail.com', 'yahoo.com', 'icloud.com', 'outlook.com']

print('Welcome to safe email checker, please input your email')

emails_to_check = []
user_email = input('Enter your email: ')
emails_to_check.append(user_email.lower())

for email in emails_to_check:
       if "@" not in email or email.count("@") != 1:
            print(f'{email} invalid email format')
       else:
             safe_domain = email.split('@')[1]
             if safe_domain in whitelist:
                print(f'{email} is safe')
             else:
                print(f'{email} is not safe')
