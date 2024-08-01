Invoice Data Extraction and Processing
This project automates the extraction and processing of invoice data using OCR (Optical Character Recognition) and dynamic field extraction techniques. 
The solution is designed to handle invoices with varying structures, providing flexibility to add or remove fields as needed.

Features
OCR Integration: Uses Tesseract OCR to extract text from invoice images.
Dynamic Field Extraction: Allows for flexible extraction of invoice fields using customizable regex patterns.
Data Parsing: Parses extracted text to retrieve relevant invoice information.
Field Management: Functions to add or remove fields dynamically based on different invoice structures.
Structured Output: Stores extracted information in a structured dictionary format.
Requirements
Python 3.6+
Tesseract OCR
Pillow
pytesseract
