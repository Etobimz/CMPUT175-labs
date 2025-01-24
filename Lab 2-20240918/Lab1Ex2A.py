def read_rainfall_data(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            city, rainfall = line.strip().split(None, 1)
            data[city] = float(rainfall)
    return data

def categorize_rainfall(data):
    categories = {
        '[50-60 mm)': [],
        '[60-70 mm)': [],
        '[70-80 mm)': [],
        '[80-90 mm)': [],
        '[90-100 mm]': []
    }
    for city, rainfall in data.items():
        if 50 <= rainfall < 60:
            categories['[50-60 mm)'].append((city, rainfall))
        elif 60 <= rainfall < 70:
            categories['[60-70 mm)'].append((city, rainfall))
        elif 70 <= rainfall < 80:
            categories['[70-80 mm)'].append((city, rainfall))
        elif 80 <= rainfall < 90:
            categories['[80-90 mm)'].append((city, rainfall))
        elif 90 <= rainfall <= 100:
            categories['[90-100 mm]'].append((city, rainfall))
    
    for category in categories:
        categories[category].sort(key=lambda x: x[1])
    
    return categories

def write_formatted_data(categories, output_filename):
    with open(output_filename, 'w') as file:
        for category, cities in categories.items():
            file.write(f"{category}\n")
            for city, rainfall in cities:
                file.write(f"{city.upper():^25}{rainfall:>5.1f}\n")
            file.write("\n")

input_file = "rainfall.txt"
output_file = "rainfallfmt.txt"

rainfall_data = read_rainfall_data(input_file)
categorized_data = categorize_rainfall(rainfall_data)
write_formatted_data(categorized_data, output_file)

print(f"Processed data has been written to {output_file}")
