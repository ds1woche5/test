import matplotlib.pyplot as plt  # Import war an falscher stelle

def merge_sort(unsorted_list):   #Zu langer Variablen Name + Funktionen in Snake Case und lowercase
    if (len(unsorted_list) > 1): # Selbe spezifizierungen
        middle = len(unsorted_list) // 2 # ausgeschrieben
        left_half = unsorted_list[:middle] #Varaiablen Name der genauer ist
        right_half = unsorted_list[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_index = 0 # wofuer die Variablen stehen
        right_index = 0
        final_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                unsorted_list[final_index] = left_half[left_index]     # Assignment Funktion war überflüssig
                left_index += 1
            else:
                unsorted_list[final_index] = right_half[right_index]
                right_index += 1
            final_index += 1

        while left_index < len(left_half):
            unsorted_list[final_index] = left_half[left_index]
            left_index += 1
            final_index += 1

        while right_index < len(right_half):
            unsorted_list[final_index] = right_half[right_index]
            right_index += 1
            final_index += 1

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

x = range(len(my_list)) # x-Vorher 2mal definiert
plt.plot(x, my_list)
plt.show()

y = merge_sort(my_list)
plt.plot(x, my_list)
plt.show()