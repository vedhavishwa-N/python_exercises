"""Write a class called "Mail".
It should have the following attributes/properties
- subject, sender_name, sender_address, recipient_name, recipient_gender,
subject, body, signature. It should have one method called "compose",
 which should return a neatly formatted mail body based on the attributes.
Hints:
Please use the 'format' method.
Please find out how to create multi line strings easily
"""
import Class_mail
mail1 = Class_mail.Mail ("this is a test mail",
                      "vedha",
                      """vanniar meetu street,
                      iyapanthangal,
                      chrnnai.""",
                      "vishwa",
                      "male",
                      """Write a class called Mail 
                      It should have the following attributes/properties -
                      subject, sender_name, sender_address, recipient_name,
                      recipient_gender, subject, body, signature.
                      It should have one method called "compose", 
                      which should return a neatly formatted mail body based on the attributes. """,
                      "VEDHAVISHWA N")
print ( mail1.compose ())
