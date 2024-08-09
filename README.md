# Financial-Data-Extraction-with-Pytesseract-and-Regex


## Project Overview
This project is designed to extract key financial data from several years of auditor's reports in PDF format, spanning the years 2013 to 2021. the extracted data be used for analysis.
The extracted data includes values for revenue, expenses, net surplus, and net assets from the Balance Sheets and Income Statements embedded in lengthy auditor's reports. 
The data is then stored in an Excel file for further analysis. The process involves converting the PDF documents into text using 
Optical Character Recognition (OCR) and applying regular expressions to extract the relevant financial data. 
Here are the steps taken:

- Import all the pdf audit reports from the folder where they were stored (see notebook)  
- Combine all of them into one pdf in my local machine (see notebook). This pdf will be used as input in FastAPI (main.py)  
- Convert the merged pdf file to images  
- Convert the images to text using tesseract engine  
- Applying regular expression to extract Revenue, Expenses, Net Surplus and Net Assets from the the income statements and balance sheets found in the text.  
- Storing all this data into an Excel file from which analysis will be done.  

## Objectives
- Automatically parse and extract financial data from multiple auditor's reports in PDF format.
- Store the extracted data in a structured Excel file for analysis.
- Ensure accurate data extraction through the use of OCR and regular expressions.
- Facilitate the analysis of financial trends over multiple years.

## Technologies Used
- **Python**: The core programming language used for scripting and automation.
- **FastAPI**: A modern web framework for building APIs, used to handle the PDF processing.
- **PyPDF2**: A Python library used to merge PDF files.
- **Tesseract OCR**: An open-source optical character recognition engine used to convert images to text.
- **Regular Expressions (regex)**: Used to accurately extract financial data from the text.
- **Pandas**: A Python library used for data manipulation and storage in Excel format.
- **Excel**: The final format for storing and analyzing the extracted data.

## Installation and Usage
1. **Clone the Repository**:
   - git clone "https://github.com/mngembu/Financial-Data-Extraction-with-Pytesseract-and-Regex.git"
   - cd Financial-Data-Extraction-with-Pytesseract-and-Regex

2. **Set Up the Virtual Environment** 
- python -m venv venv
- source venv/bin/activate    (On Windows, use `venv\Scripts\activate`)

3. **Install Dependencies**:
- python -m pip install -r requirements.txt

4. **Prepare the PDF Files:**:
- Store all the auditor's reports (PDF files) for the years 2013 to 2021 in a designated folder.
- Refer to the provided notebook (data_extraction.ipynb) for details on importing and merging the PDF files.

5. **Run the Application**:
- main.py

6. **Data Exported to Excel**:
- he extracted data is automatically stored in an Excel file (financial_data.xlsx) in the project directory.

## Dependencies
- FastAPI: A modern, fast (high-performance) web framework for Python.
- PDF2toImage: Used for converting the PDF files to image.
- pytesseract: Python wrapper for Google's Tesseract-OCR Engine.
- Pillow: Python Imaging Library used for image processing.
- pandas: Used for manipulating the extracted data and exporting it to Excel.
- openpyxl: Used for writing data to Excel files.
- re: Built-in Python library for regular expressions.
- uvicorn: ASGI server implementation used with FastAPI.


Note:
Ensure Tesseract-OCR is installed on your system and properly configured in your environment 


## Contact

If you have any questions, feel free to reach out to me at ara.ngembu@yahoo.com.

Author: Mary Ara Ngembu










