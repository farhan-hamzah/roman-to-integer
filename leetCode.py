roman_values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}
roman_numeral = input("Masukkan angka Romawi: ").upper()
total = 0
prev_value = 0
for char in reversed(roman_numeral):  
    value = roman_values[char]
    if value < prev_value:
        total -= value  
    else:
        total += value
    prev_value = value
print(f"Bilangan desimal: {total}")
