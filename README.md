# 8630-Project
Final Iterative Project for Graduate Data Visualization Class

## Get Data
1. Download the data file using the `data.py` program in the root of this repository. 
    - `python3 -m venv .venv` 
    - `source .venv/bin/activate`
    - `pip install --upgrade pip` Optional, but good practice
    - `pip install -r requirements.txt` Note that the requirements.txt file does not lock library versions. I did it this way because the program and dependencies are simple, and leaving the library versions unlocked enables support for a wider range of python3 versions. 
    - `python data.py`
2. Your file should be saved in the root of this repository as a `data.zip`. This file is saved in the .gitignore, and will not be pushed back to your respository
3. Run the `dictionary-builder.py` script: `python dictionary-builder.py`. This script will unzip `data.zip` and place all the extracted files into an `extracted_files` subdirectory. Like `data.zip` itself, the contents of this subdirectory, and any other .csv or .json files in this repository will be included in the `.gitignore` file and not pushed back to the GitHub repository. 

## Updated Get Data

