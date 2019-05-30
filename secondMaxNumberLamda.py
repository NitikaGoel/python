user_input = input("Enter a list of comma separated numbers: ")
intlist_from_csv_string = lambda x: int(x)
try:
  array_of_number_strings = user_input.split(",")
  second_max_val = max(filter(lambda x: x != max(map(intlist_from_csv_string,array_of_number_strings)), map(intlist_from_csv_string,array_of_number_strings)))
  print(second_max_val)
except ValueError:
  print("That's not an int!")