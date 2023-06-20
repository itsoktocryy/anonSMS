import requests

class SMS:
    def __init__(self, number, text, api_key):
        self.number = number
        self.text = text
        self.url = "https://textbelt.com/text"
        self.data = {"phone": number, "message": text, "key": api_key}

    def sendSMS(self):
        res = requests.post(self.url, data=self.data).json()
        if res['success']:
            print("[+] Message sent successfully!")
        else:
            print("[-] Couldn't send message!")
            if 'error' in res:
                print('[-]', res['error'])
            else:
                print('[-] Unknown error occurred!')

def main():
    try:
        number = input('Enter number (Include country code, ex. +1): ')
        text = input("Enter message: ")
        api_key = input('Enter API: ')  # TextBelt API
    except KeyboardInterrupt:
        print("\n[-] Quitting")
        exit(0)

    process = SMS(number, text, api_key)
    if input('Do you want to send the message? (y/n): ').lower() == 'y':
        process.sendSMS()
    else:
        print("[-] Quitting")
        exit(0)

if __name__ == '__main__':
    main()
