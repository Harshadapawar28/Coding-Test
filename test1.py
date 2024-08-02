# 1. Write a Python program to read a CSV file and display its contents.				
import csv

def read_csv(file_path):
    """
    Read a CSV file and display its contents.

    Parameters:
    file_path (str): The path to the CSV file.
    """
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = '"C:\Users\kadam\Downloads\customers-100.zip"'  # Replace with your CSV file path
read_csv(file_path)

