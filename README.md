# HubSpot Timezone Updater

This project automatically updates the timezone property of HubSpot contacts based on their country and city information using Llama 3.2 for to produce timezones
## Table of Contents 
- [Setup](#setup) 
- [Usage](#usage) 
- [Testing](#testing) 
- [Note](#note)

## Setup
To set up this project, follow these steps:

 1. **Clone the repository**
```bash git clone https://github.com/your-username/hubspot-timezone-updater.git```

 2. **Install dependencies**
```pip install -r requirements.txt```

 3. **Create a HubSpot Private App**
Go to your HubSpot account, navigate to **Settings > Integrations >
   Private Apps**, and create a new private app. Then Copy the API key/token
   generated.

4. **Set up your HubSpot API Key in AWS SSM Parameter Store**
   Use AWS CLI or console to store the HubSpot API key securely in AWS SSM.
   ```aws ssm put-parameter --name "HubSpotAPIKey" --value "your-hubspot-api-key" --type "String"```

5. **Deploy the serverless function**
```serverless deploy```

## Usage

Once deployed, the function will run daily to update timezones for contacts with missing timezone information, leveraging location data (country and city) for timezone prediction.

## Testing

Run tests with:
```python -m unittest discover tests```

## Note

-   This project uses the Llama 2 (3.2B) model for timezone prediction. Ensure your serverless environment has sufficient resources to run this model.
-   For troubleshooting or configuration tips, refer to the documentation or HubSpot API support.

