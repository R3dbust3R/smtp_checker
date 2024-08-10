import smtplib
from os import path


print('''
          ________ ___ ______ ____         
         / ___|   |   |      |    \\        
        (   \\_| _   _ |      |  o  )       
         \\__  |  \\_/  |_|  |_|   _/        
         /  \\ |   |   | |  | |  |          
         \\    |   |   | |  | |  |          
    __ __ \\___|___|___|_|__| |__|___ ____  
   /  |  |  | /  _]  /  |  |/ ] /  _|    \\ 
  /  /|  |  |/  [_  /  /|  ' / /  [_|  D  )
 /  / |  _  |    _]/  / |    \\|    _|    / 
/   \\_|  |  |   [_/   \\_|     |   [_|    \\ 
\\     |  |  |     \\     |  .  |     |  .  \\
 \\____|__|__|_____|\\____|__|\\_|_____|__|\\_|

             SMTP checker v1.0

Make sure your SMTP file follows this structure:

    [ domain|port|email|password ]
    [ eq: smtp.dom.com|465|ex@domain.com|Password123 ]

''')


def check_smtp_account(domain, port, email, password):
    try:
        # Use SMTP_SSL if the port is 465, otherwise use SMTP and start TLS
        if port == 465:
            server = smtplib.SMTP_SSL(domain, port, timeout=5)
        else:
            server = smtplib.SMTP(domain, port, timeout=5)
            server.starttls()
        
        server.login(email, password)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to connect to {email} ({domain}:{port}) - {str(e)}")
        return False

def main():
    working_SMTPs_counter = 0
    working_SMTPs = []
    smtp_file = ''
    while 1:
        smtp_file = input('Enter your SMTPs file path: ')
        if path.isfile(smtp_file): break
        print('[!] No such file or directory!')

    with open(smtp_file, 'r') as file:
        smtp_accounts = file.readlines()

    try:
        for smtp_account in smtp_accounts:
            domain, port, email, password = smtp_account.strip().split('|')
            port = int(port)
            if check_smtp_account(domain, port, email, password):
                print(f"[+] SMTP account {email} is working.")
                working_SMTPs.append(f"{domain}|{port}|{email}|{password}")
                working_SMTPs_counter +=1
            else:
                print(f"[!] SMTP account {email} failed.")

    except KeyboardInterrupt: print('\n[*] Exiting...')

    print(f'\n[*] {working_SMTPs_counter} Working SMTPs found.')
    for smtp in working_SMTPs: print(f'[+] {smtp}')

if __name__ == "__main__":
    main()
