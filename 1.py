from sys import argv
script_name, output_in_hours, rate_per_hour, prize = argv
print((int(output_in_hours) * int(rate_per_hour)) + int(prize))
