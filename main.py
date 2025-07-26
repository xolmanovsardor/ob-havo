#asosiy boshqaruv, foydalanuvchi bilan muloqat
import sys 
from ob_havo.menyu import print_menu
from ob_havo.wather import show_all_weather , search_weather

def main():
    while True:
        print_menu()
        choice = input("> ")

        if choice == '1':
            show_all_weather()
        elif choice == '2':
            search_weather()
        elif choice == '3':
            print("Dasturdan chiqildi. Xayr!")
            sys.exit(0)
        else:
            print(" Noto‘g‘ri tanlov! Qayta urinib ko‘ring.")

if __name__ == '__main__':
    main()