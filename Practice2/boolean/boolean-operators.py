age = 20
has_id = True

#operator AND
can_enter = age >= 18 and has_id
print(can_enter)  # True

#operator OR
is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)  # True

#operator NOT
is_logged_in = False
print(not is_logged_in)  # True

#Combining operators
score = 85
passed = score >= 50 and score <= 100
print(passed)  # True
