#Napisz program, który drukuje nazwę dnia tygodnia dla danego numeru dnia. 
#Następnie, korzystając ze zdefiniowanej funkcji, wydrukuj nazwę dnia tygodnia dla następujących numerów dni: 1, 4, 7.
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"] #nasza lista siedmiu dni tygodnia
    return weekdays[n-1] #n-1 bo indeks rozpoczyna sie od 0

print(weekday(1))
print(weekday(4))
print(weekday(7))
