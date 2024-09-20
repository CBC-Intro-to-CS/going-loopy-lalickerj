# first you must declare a function
def testfunc():
    fname = "Jacob"
    lname = "Lalicker"
    print(F"Hello, {fname} {lname}")

testfunc()
print("Hello")

def flattened_cans(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print(f"Week {week} = {total_cans} cans")

flattened_cans(2)

def silly_age_joke(age):
    age = int(input("What is your age?"))
    if age >=10 and age <= 13:
       print('What is 13 + 40 + 155 + 97? A headache')
else:
    print('Huh?')
