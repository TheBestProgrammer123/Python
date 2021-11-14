import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from phonenumbers.phonenumberutil import PhoneNumberFormat, PhoneNumberType
PhoneNumber = input("What Is The Phone Number?\n")
phoneNumber = phonenumbers.parse(PhoneNumber)
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')
timeZone = timezone.time_zones_for_number(phoneNumber)
Validity = (phonenumbers.is_possible_number(phoneNumber))
International_Number = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
National_Number = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.NATIONAL)
if Validity == True:
    print("Phone Number Data:")
    print("Carrier: " + str(Carrier))
    print("Country: " + str(Region))
    print("TimeZone: " + str(timeZone))
    print("International Number: " + str(International_Number))
    print("National Number: " + str(National_Number))

else:
    print("The Phone Number Is Not Valid")