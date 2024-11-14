import os
from hubspot.api import HubSpotAPI
from timezone.finder import TimezoneFinder

def lambda_handler(event, context):
    HUBSPOT_API_KEY = os.environ['HUBSPOT_API_KEY']
    
    hubspot_api = HubSpotAPI(HUBSPOT_API_KEY)
    timezone_finder = TimezoneFinder()
    
    # Get contacts with missing timezones
    contacts = hubspot_api.get_contacts_with_no_timezone()
    
    updated_contacts = 0
    for contact in contacts:
        country = contact['properties'].get('country')
        city = contact['properties'].get('city')
        
        # Predict timezone using Llama 2
        predicted_timezone = timezone_finder.predict_timezone(country, city)
        
        # Update contact in HubSpot
        if predicted_timezone:
            success = hubspot_api.update_contact_timezone(contact['id'], predicted_timezone)
            if success:
                updated_contacts += 1
    
    return {
        'statusCode': 200,
        'body': f'Updated timezones for {updated_contacts} contacts'
    }