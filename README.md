# HubSpot Timezone Updater

This project automatically updates the timezone property of HubSpot contacts based on their country and city information using Llama 2 for prediction.

## **Setup**

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a HubSpot private app
4. Set up your HubSpot API key in AWS SSM Parameter Store
5. Deploy the serverless function: `serverless deploy`
   

## Usage

The function will run daily to update timezones for contacts with missing timezone information.

## Testing

Run tests using: `python -m unittest discover tests`

## Note

This project uses the Llama 2 (3.2B) model for timezone prediction. Ensure your serverless environment has sufficient resources to run this model.#   H u b s p o t - T i m e z o n e - U p d a t e r 
 
 
