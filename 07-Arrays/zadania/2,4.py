#Poniższe dane zawierają tygodniowy plan posiłków. Napisz program, który drukuje tygodniowy plan posiłków wraz z nazwą dnia

# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n): #funkcja zwraca nazwe dnia dla danego numeru 1-7
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1] #n-1 bo python liczy od 0

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number): #funkcja laczy posilki z jednego dnia w napis
    meals = meal_plan[day_number - 1] #bierzemy wiersz z posilkami dla danego dnia
    result = "" #pusty napis do ktorego bedziemy dopisywac
    for meal in meals:
        if result != "": #jesli nasze result nie jest puste
            result += "," #to dopisujemy przecinek przed kolejnym posilkiem
        result += meal #dopisujemy nazwe posilku
    return result

# Prints weekly meal plan
for day in range(1,8):
    print(weekday(day),":", day_meal_plan(meal_plan, day))
