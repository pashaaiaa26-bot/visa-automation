import pandas as pd
import os

def update_visa_data():
    # Aap yahan apna data update kar sakte hain
    # Is structure mein aap jitni chahein countries aur categories add kar sakte hain
    data = [
        {'Country': 'Malaysia', 'Visa_Type': 'Visit Visa', 'Requirements': 'Passport, Photo, Bank Statement, Ticket', 'Official_Link': 'https://malaysiavisa.imi.gov.my'},
        {'Country': 'Malaysia', 'Visa_Type': 'Business Visa', 'Requirements': 'Passport, Invitation Letter, Company NTN, Bank Statement', 'Official_Link': 'https://malaysiavisa.imi.gov.my'},
        {'Country': 'Thailand', 'Visa_Type': 'Tourist Visa', 'Requirements': 'Passport, Photos, Hotel Booking, Return Ticket', 'Official_Link': 'https://www.thaievisa.go.th'},
        {'Country': 'Thailand', 'Visa_Type': 'Business Visa', 'Requirements': 'Passport, Company Invitation Letter, Bank Statement', 'Official_Link': 'https://www.thaievisa.go.th'},
        {'Country': 'Turkey', 'Visa_Type': 'Study Visa', 'Requirements': 'Acceptance Letter, Passport, Biometric Photos, Fee Receipt', 'Official_Link': 'https://www.visa.gov.tr'}
    ]
    
    df = pd.DataFrame(data)
    
    # Directory check aur file creation
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df.to_csv('data/master_visa_data.csv', index=False)
    print("Visa data file updated successfully.")

if __name__ == "__main__":
    update_visa_data()