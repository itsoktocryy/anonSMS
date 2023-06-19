import requests
import click

class SMS:
    def __init__(self, number, text, api_key):
        self.number = number
        self.text = text
        self.url = "https://textbelt.com/text"
        self.data = {"phone": number, "message": text, "key": api_key}

    def sendSMS(self):
        res = requests.post(self.url, data=self.data).json()
        if res['success']:
            click.secho("[+] Message sent successfully!")
        else:
            click.secho("[-] Couldn't send message!")
            if 'error' in res:
                click.secho('[-] ' + res['error'])
            else:
                click.secho('[-] Unknown error occurred!')

def main():
    try:
        number = click.prompt('Enter number (Include country code, ex. +1)', type=str)
        text = str(input("Enter message: "))
        api_key = click.prompt('Enter API', type=str) # TextBelt API
    except:
        click.secho("\n[-] Quitting")
        exit(0)

    process = SMS(number, text, api_key)
    if click.confirm('Do you want to send the message?'):
        process.sendSMS()
    else:
        click.secho("[-] Quitting")
        exit(0)

if __name__ == '__main__':
    main()

