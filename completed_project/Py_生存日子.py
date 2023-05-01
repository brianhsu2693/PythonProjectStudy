# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
good_age_y = 90 - int(age)
good_age_m = int(good_age_y) * 12
good_age_w = int(good_age_y) * 52
good_age_d = int(good_age_y) * 365

print(f'You have {good_age_d} days, {good_age_w} weeks, and {good_age_m} months left.')