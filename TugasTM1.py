# Djonathan Paulsen Manik
# 242410101087
# ALGO 2 A

# Latihan 1
def print_menu(menu_items, parent_id=0, level=0):
    for item in menu_items:
        if item['Parent'] == parent_id:
            print('....' * level + item['Label'])
            print_menu(menu_items, item['Id'], level + 1)

def main():
    menu_items = []
    n = int(input("Masukkan jumlah menu: "))

    for i in range(n):
        print(f"\nMasukkan detail menu ke-{i+1}:")
        id = int(input("id: "))
        parent = int(input("Parent: "))
        label = input("Label: ")
        menu_items.append({'Id': id, 'Parent': parent, 'Label': label}) #disini terkumpul semua data id parent dan labelny

    print("\nDatabase Menu:")
    print_menu(menu_items)


main()
input()
    
# LATIHAN 2
def palindrom(string):
    if len(string) <= 1 :
        return string
    elif not string[0].isalpha() :  
        return palindrom(string[1:])
    elif not string[-1].isalpha():
        return palindrom(string[:-1])
    elif string[0] == string[-1]:
        return palindrom(string[1:-1]) #manggil index sebelum terakhir dan setelah awal

str = input("Masukkan Kata: ").lower()
if palindrom(str):
    print(f"{str} adalah Palindrom")
else:
    print(f"{str} bukan Palindrom")