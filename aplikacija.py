import time
ime = input("Vase ime:")
prezime = input("Vase prezime:")
br_godina = int(input("Broj godina:"))

if (br_godina < 18):
    print("Nazalost ne mozete ucestvovati u nagradnoj igri. Program ce se ugasiti za 5 sekundi.")
    time.sleep(5)
    exit()
    
else:
    print("Cestitamo", ime, prezime, "uspesno ste se registrovali kao punoletan gradjanin.")

prosek = float(input("Vas prosek:"))
if (prosek < 7.5):
    print("Nazalost ne mozete da aplicirate. Program ce se ugasiti za 5 sekundi.")
    time.sleep(5)
    exit()
    

fakultet = input("Vas fakultet:")
lista = ["privatni", "drzavni"]
pr_dr = input("Da li je vas fakultet privatni ili drzavni?")



while pr_dr not in lista:
        print("Pogresan unos.")
        pr_dr = input("Da li je vas fakultet privatni ili drzavni?")

if (pr_dr == "privatni"):
    print("Nazalost ne mozete da aplicirate. Program ce se ugasiti za 5 sekundi.")
    time.sleep(5)
    exit()
    
else:
    print("Uspesna aplikacija.")


    
    
    
    