
#original_list = [1,2,3,4,5]

#def filter_three(number):
#  return number > 3

#filtered = filter(filter_three, original_list)

#filtered_list = list(filtered)

#print(filtered_list)
## Returns [4,5]

#filtered_list2=[number1 for number1 in original_list if number1 > 3]
#print(filtered_list2)

#sqrt= [x**x for x in original_list]
#print(sqrt)

#def square(number):
#	return number**2

#squares= map(square, original_list)
#squares_list=list(squares)

#print(squares_list)


#sqrts=[sqrtlist**2 for sqrtlist in original_list]
#print(sqrts)


# ZIP() function

numbers=[1,2,3]
letters=['a','b','c']

combined=zip(numbers, letters)
combined_list=list(combined)
print(combined_list)

#################################################
games = ['Yankees', 'Yankees', 'Cubs', 'Blue Jays', 'Giants']

def isin(item, list_name):
  if item in list_name: print(f"{item} is in the list!")
  else: print(f"{item} is not in the list!")

isin('Blue Jays', games)
isin('Angels', games) 

# Returns
# Blue Jays is in the list!
# Angels is not in the list!

#################################################
games = ['heads', 'heads', 'tails', 'heads', 'tails']
items = set(games)
print(max(items, key = games.count))
print(min(items, key = games.count))

##################################################
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

flat_list = [i for j in nested_list for i in j]

print(flat_list)

# Returns [1, 2, 3, 4, 5, 6, 7, 8, 9]




def get_speed(final, init, time_taken):
    speed = (final - init) / time_taken # simple equation could return negative value if init > final.
    #assert speed >= 0 # will raise an AssertionError exception if speed is less than 0. 
    if speed < 10 :
        try:
            if x < 0 :
                print("Minus checking : " ,speed)
            else: print("Plus checking : " ,speed)
        except NameError:
          print("Variable x is not defined")
        except:
          print("Something else went wrong")
    return speed

print(get_speed(5, 2, 1)) # will return 3 as expected 
print(get_speed(2, 5, 1)) # will raise AssertionError exception


