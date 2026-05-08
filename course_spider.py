import pandas as pd
import requests
import os
from bs4 import BeautifulSoup

# Read the CSV file with semicolon as separator
df = pd.read_csv('20230912-courselist-MASTER.csv', sep=';')

# Create a directory for the downloaded pages
if not os.path.exists('course_descriptions'):
    os.makedirs('course_descriptions')

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Replace spaces and slashes in the course name with underscores and hyphens respectively
    course_name = row['Course name'].replace(' ', '_').replace('/', '-')
    
    # Replace slashes in the university name with hyphens
    uni_name = row['Uni'].replace('/', '-')
    
    # Create the filename
    filename = f"{uni_name}_{course_name}.txt"
    
    # Get the URL
    url = row['URL']
    
    # Download the page
    response = requests.get(url)
    
    # Parse the HTML content of the page with Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the text content of the page
    text = soup.get_text()
    
    # Save the text content to a file
    with open(os.path.join('course_descriptions', filename), 'w') as f:
        f.write(text)

