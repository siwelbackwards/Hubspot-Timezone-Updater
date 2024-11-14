import requests

class HubSpotAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.hubapi.com/crm/v3/objects/contacts'

    def get_contacts_with_no_timezone(self):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.get(self.base_url, headers=headers, params={"properties": "country,city,timezone"})
        contacts = response.json().get('results', [])
        return [contact for contact in contacts if not contact['properties'].get('timezone') 
                and contact['properties'].get('country') and contact['properties'].get('city')]

    def update_contact_timezone(self, contact_id, timezone):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            "properties": {
                "timezone": timezone
            }
        }
        response = requests.patch(f'{self.base_url}/{contact_id}', headers=headers, json=data)
        return response.status_code == 200