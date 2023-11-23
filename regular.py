import re
#stroka = 'Privet menya zovyt Kirill, mne 38, moi telefon 89110271345, a pochta kmmorozov@gmail.com, rab telefon 8987876868'

#result = re.match(r'Privet menya zovyt Kirill',stroka)

#print(result)
#print(result.group(0))
#print(result.start())
#print(result.end())
##########################################################
#result = re.search(r'telefon', stroka)
#print(result)
#print(result.group(0))
##########################################################
#result = re.split(r'moi', stroka)
#print(result)
######################################################
#result = re.findall(r'telefon', stroka)
#print(result)

stroka = 'Privet menya zovyt Kirill, mne 38, moi telefon 89110271345 , a pochta kmmorozov@gmail.com, rab telefon 8987876 '
#phones = re.findall(r'\d{7,11}',stroka)
phones = re.findall(r'\b\d\d\d\d\d\d\d\b|\b\d\d\d\d\d\d\d\d\d\d\d\b',stroka)
print(phones)
emails = re.findall(r'\w+@\w+\W\w+',stroka)
print(emails)