class Phone():
    def __init__(self, phone_number):
        self.number = phone_number
        self.call_history = []
        self.messages = []

    def phone_call(self, other_phone):
        call_string = f'Call from: {self.number} to: {other_phone.number}'
        self.call_history.append(call_string)

    def show_call_history(self):
        for record in self.call_history:
            print(f'{record}')

    def send_message(self, destination, content):
        message = {
            'to': destination,
            'from': self.number,
            'content': content
        }
        self.messages.append(message)
        print(self.messages)
    def show_outgoing_messages(self):
        for message in self.messages:
            if message['from'] == self.number:
                print(message)
    def show_incoming_messages(self):
        for message in self.messages:
            if message['to'] == self.number:
                print(message)


phone1 = Phone('0521231231')
phone2 = Phone('0523453455')
phone1.phone_call(phone2)
phone1.show_call_history()
text = 'hello friend,wanna hangout?'
phone1.send_message(phone2,text)
phone1.show_outgoing_messages()
phone1.show_incoming_messages()