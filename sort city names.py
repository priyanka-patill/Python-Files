def sort_city_names(input_filename, output_filename):
    
    with open(input_filename, 'r') as infile:
        city_names = infile.readlines()
    
    city_names = [city.strip() for city in city_names]
    
    city_names.sort()
    
    with open(output_filename, 'w') as outfile:
        for city in city_names:
            outfile.write(city + '\n')

input_filename = 'cities.txt'  
output_filename = 'sorted_cities.txt'  

sort_city_names(input_filename, output_filename)
