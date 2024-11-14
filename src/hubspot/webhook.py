import requests

def create_webhook(app_id, api_key, webhook_url):
    url = f"https://api.hubapi.com/webhooks/v3/app/{app_id}/subscriptions"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "eventType": "contact.propertyChange",
        "propertyName": "country",
        "active": True,
        "webhookUrl": webhook_url
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()