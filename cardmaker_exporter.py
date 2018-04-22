import csv

def export(data):
    sample_data = data[0]
    fieldnames = ['Quantity']
    for key in sample_data:
        fieldnames.append(key)
    with open('exported_file.csv', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for dictionary in data:
            dictionary['Quantity'] = 1
            writer.writerow(dictionary)
            
