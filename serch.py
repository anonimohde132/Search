import os

print("""
+====================================+
           ______________
          | HDE Products |
          |______________|
          
          HeHeHeHeHeHeHe
+====================================+

{1} Instalar ferramentas (Para kali linux apenas)
{2} Info Do site completa


""")


ask = int(input(' {Escolha} {> '))

if ask == '1':
  os.system('apt install parsero -y && apt install nikto -y && apt install dnsenum -y')
elif ask == '2':
           ask2 == str(input(' {Site} ==>> '))
           os.system('whois ' + ask2)
