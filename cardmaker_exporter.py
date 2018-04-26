import csv

def export(data):
    sample_data = data[0]
    fieldnames = ['Quantity']
    for key in sample_data:
        fieldnames.append(key)
    with open('exported_file.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for dictionary in data:
            dictionary['Quantity'] = 1
            csv_writer.writerow(dictionary)
