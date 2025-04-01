name = input()
phone = input()
email=input()
vcard = (
    "FN:" name,
    "TEL:" phone,
    "EMAIL:" email,
)
with open("contact.vcf","w") as file:
    file.write(vcard)
    
