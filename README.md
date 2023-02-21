# Financial-Data-Extraction-with-Pytesseract-and-Regex
Extract financial data from auditor's reports and store them to an excel file to be used for analysis


This project parses the auditor's reports for the years 2013 to 2021 and extract the audited financial statements (Balance Sheets and Income Statements), from which it will extract values for revenue, expenses and net assets to be used for analysis. Here are the steps that will be taken:  

Import all the pdf audit reports from the folder where they were stored (see notebook)  
Combine all of them into one pdf in my local machine (see notebook). This pdf will be used as input in FastAPI (main.py)  
Convert the merged pdf file to images  
Convert the images to text using tesseract engine  
Applying regular expression to extract Revenue, Expenses, Net Surplus and Net Assets from the the income statements and balance sheets found in the text.  
Storing all this data into an Excel file from which analysis will be done.  
