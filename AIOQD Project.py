#!/usr/bin/env python
# coding: utf-8

# In[48]:


#!pip install pytess#eract
#!pip install pypdf#


# In[38]:


import pytesseract
from PIL import Image
import numpy as np

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the image file
filename = r'D:\gradcommerce.com\invoice file\6965292.jpg'

# Open the image using PIL
img = Image.open(filename)

# Convert the image to a NumPy array (optional)
img_array = np.array(img)

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(img_array)

# Print the extracted text
print(text)


# In[42]:


lines = text.split('\n')
data = {
    'Field': [],
    'Value': []
}

# Example parsing logic
for line in lines:
    if ':' in line:
        field, value = line.split(':', 1)
        data['Field'].append(field.strip())
        data['Value'].append(value.strip())

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("Parsed Data:")
print(df)


# In[47]:


import pytesseract
from PIL import Image
import re

# Set the path to the Tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from an image using Tesseract
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Dictionary to store field patterns
field_patterns = {
    'Invoice Number': r'Invoice # (\d+)',
    'Date': r'Date (\d{2}/\d{2}/\d{4})',
    'Customer Name': r'Invoice to:\s*([\w\s]+)',
    'Address': r'1700 Biscayne Blvd, Miami,\s*(FL \d{5}, United States)',
    'Subtotal': r'Subtotal \$([0-9,]+\.\d{2})',
    'Email': r'Email us:\s*([\w@.]+)',
    'Phone': r'Call us:\s*(\+\d{2} \d{4} \d{3} \d{2})',
    'Account #': r'Account #:\s*(\d{4} \d{4} \d{4} \d{4})',
    'A/C Name': r'A/C Name:\s*([\w\s]+)',
    'Bank Details': r'Bank Details:\s*([\w\s]+)'
}

# Function to parse the extracted text and retrieve relevant fields
def parse_invoice_text(text, field_patterns):
    data = {}
    for field, pattern in field_patterns.items():
        match = re.search(pattern, text)
        data[field] = match.group(1) if match else None
    return data

# Function to add a new field pattern
def add_field_pattern(field_name, pattern):
    field_patterns[field_name] = pattern

# Function to remove an existing field pattern
def remove_field_pattern(field_name):
    if field_name in field_patterns:
        del field_patterns[field_name]

# Main execution
image_path = 'D:/gradcommerce.com/invoice file/6965292.jpg'
text = extract_text_from_image(image_path)
parsed_data = parse_invoice_text(text, field_patterns)

# Add or remove fields as needed
add_field_pattern('New Field', r'New Field Pattern')
remove_field_pattern('Phone')

print(parsed_data)


# In[ ]:





# In[ ]:





# In[ ]:




