import csv


def save(path, field_names, data_list):
    try:
        with open(path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            # writer.writeheader()
            for data in data_list:
                writer.writerow(data)
    except IOError:
        print("I/O error")
