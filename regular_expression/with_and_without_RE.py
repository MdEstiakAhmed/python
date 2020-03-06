print("\n--------------------Without regular expression--------------------\n")

country_name = "Benin, Bhutan, Greenland, Bolivia, England, Netherlands, Brazil, Iceland, New Zealand"
country_list = country_name.split(", ")
country_list1 = [country for country in country_list if country.endswith("land") or country.endswith("land")]	# list comprehension
print("countries which ends with \"land\":", country_list1)

print("\n--------------------With regular expression--------------------\n")

import re
country_name1 = "Benin, Bhutan, Greenland, Bolivia, England, Netherlands, Brazil, Iceland, New Zealand"
country_list2 = re.findall(r'(\w+land*)', country_name1)	# regular expression
print("countries which ends with \"land\":", country_list2)
