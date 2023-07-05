import os
from bs4 import BeautifulSoup

# Specify the directory containing the downloaded HTML files
html_directory = 'path/to/your/html/files'

def extract_details(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    education_section = soup.find('section', {'id': 'education-section'})
    education_details = []
    if education_section:
        for education_item in education_section.find_all('li'):
            education_details.append(education_item.get_text(strip=True))

    # Extract experience details
    experience_section = soup.find('section', {'id': 'experience-section'})
    experience_details = []
    if experience_section:
        for experience_item in experience_section.find_all('li', {'class': 'pv-entity__position-group-pager'}):
            role = experience_item.find('h3').get_text(strip=True)
            company = experience_item.find('p', {'class': 'pv-entity__secondary-title'}).get_text(strip=True)
            experience_details.append({'role': role, 'company': company})

    return {'education': education_details, 'experience': experience_details}

for filename in os.listdir(html_directory):
    if filename.endswith('.html'):
        file_path = os.path.join(html_directory, filename)
        profile_details = extract_details(file_path)
        print(f"Profile: {filename}")
        print(f"Educational Details: {profile_details['education']}")
        print(f"Experience Details: {profile_details['experience']}")
        print()
