import csv
from front.models import MockTest


def import_csv_data(csv_file_path):
    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            text = row["text"]
            test_number = int(row["test_number"])
            # Create a MockTest object and save it to the database
            mock_test = MockTest(text=text, test_number=test_number)
            mock_test.save()

    print("Data imported successfully!")


# Usage:
# Replace 'your_csv_file.csv' with the path to your CSV file.
import_csv_data("csv/front_mocktest.csv")
