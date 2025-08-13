import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+986757646546")
phone_number2 = phonenumbers.parse("+988768765647")
phone_number3 = phonenumbers.parse("+987653568970")
phone_number4 = phonenumbers.parse("+985758765488")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number4, "en"))