###
# Bubble sort
#
def bubble_sort(arr):
   n = len(arr)

   for i in range(n): #dla i w zakresie długości arr
      for j in range(0, n-i-1): #dla j w zakresie od 0 do długości arr - ilość powtórzeć - 1
         if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions) 
print(bank_transactions)