class Mail(object):
    def __init__(self,subject, sender_name, sender_address, recipient_name, recipient_gender, body, signature):
        self.subject=subject
        self.sender_name=sender_name
        self.sender_address=sender_address
        self.recipient_name=recipient_name
        self.recipient_gender=recipient_gender
        self.body=body
        self.signature=signature

    def compose(self):
         return """

                                              sub:({0})
         hi {3}({4}),

           {5}

                                               thank you,
                                                                                             {6}
           regards {1},
           {2}
           """.format(self.subject, self.sender_name, self.sender_address, self.recipient_name,
                      self.recipient_gender, self.body, self.signature)

