class Email:
    def __init__(self,sender,receiver,content) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


commands = []
emails_list = []

while True:
    input_data = input()
    if input_data == 'Stop':
        break
    else:
        email_data = input_data.split(' ')
        emails_list.append(Email(email_data[0],email_data[1],email_data[2]))

sent_indices = list(map(int,input().split(', ')))

for i,email in enumerate(emails_list):
    if i in sent_indices:
        email.send()
        print(email.get_info())