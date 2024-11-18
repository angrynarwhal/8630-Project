import csv
import os
import zipfile

def unzip_file(zip_path, extract_to):
    """
    Unzips a .zip file into a specified directory.
    
    :param zip_path: str - Path to the .zip file.
    :param extract_to: str - Directory where the contents will be extracted.
    """
    try:
        # Ensure the target directory exists
        os.makedirs(extract_to, exist_ok=True)
        
        # Extract the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted files to: {extract_to}")
    except FileNotFoundError:
        print(f"Error: The file {zip_path} does not exist.")
    except zipfile.BadZipFile:
        print(f"Error: The file {zip_path} is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred while unzipping: {e}")

def enumerate_columns_in_directory(directory_path):
    """
    Enumerates the column names for all .csv files in a directory.
    
    :param directory_path: str - Path to the directory containing .csv files.
    """
    try:
        # Check if the directory exists
        if not os.path.isdir(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist.")
            return
        
        # List all .csv files in the directory
        csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
        
        if not csv_files:
            print(f"No CSV files found in directory: {directory_path}")
            return
        
        for csv_file in csv_files:
            file_path = os.path.join(directory_path, csv_file)
            print(f"\nProcessing file: {csv_file}")
            
            try:
                # Open and read the CSV file
                with open(file_path, mode='r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    headers = next(reader)  # Read the first row (header)
                    
                    print("Columns:")
                    for idx, column in enumerate(headers, start=1):
                        print(f"  {idx}. {column}")
            except Exception as e:
                print(f"  Error reading {csv_file}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the zip file
    zip_file_path = "data.zip"
    
    # Directory to extract files to
    extraction_dir = "./extracted_files"
    
    # Unzip the file
    unzip_file(zip_file_path, extraction_dir)
    
    # Enumerate columns in CSV files within the extracted directory
    enumerate_columns_in_directory(extraction_dir)