# Day 5 - Level 2 Exercises
# Resul Shafili
# 1. Ages list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Siyahını çeşidlə
ages.sort()
print("Sorted:", ages)

# Min və max yaş
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

# Min və max yaşı yenidən əlavə et
ages.append(min_age)
ages.append(max_age)
print("After append:", ages)

# Orta element (median)
ages.sort()
mid = len(ages) // 2
if len(ages) % 2 == 0:
    median = (ages[mid - 1] + ages[mid]) / 2
else:
    median = ages[mid]
print("Median:", median)

# Orta yaş (mean)
mean_age = sum(ages) / len(ages)
print("Mean age:", mean_age)

# Yaş aralığı
age_range = max_age - min_age
print("Age range:", age_range)

# (min - orta) vs (maks - orta) müqayisəsi
print("abs(min - mean):", abs(min_age - mean_age))
print("abs(max - mean):", abs(max_age - mean_age))

print("---")

# 2. Ölkələr siyahısında orta ölkə(lər)i tap
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
    'Bangladesh', 'Belgium', 'Brazil', 'Canada', 'China',
    'Colombia', 'Croatia', 'Cuba', 'Denmark', 'Egypt'
]

mid = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[mid - 1:mid + 1]
else:
    middle_countries = [countries[mid]]
print("Middle country/countries:", middle_countries)

# 3. Siyahını iki bərabər hissəyə böl
mid = len(countries) // 2
first_half = countries[:mid]
second_half = countries[mid:]
print("First half:", first_half)
print("Second half:", second_half)

# 4. İlk 3 vs Skandinaviya ölkələri
country_list = ['Çin', 'Rusiya', 'ABŞ', 'Finlandiya', 'İsveç', 'Norveç', 'Danimarka']

first_three = country_list[:3]
scandinavian = country_list[3:]

print("First three:", first_three)
print("Scandinavian countries:", scandinavian)
