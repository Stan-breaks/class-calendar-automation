import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

# Define your Google Calendar ID (usually your email address associated with Google Calendar).
calendar_id = 'niyonizigiyekayla@gmail.com'

# Load service account credentials (replace 'your-credentials.json' with your actual JSON key file).
credentials = service_account.Credentials.from_service_account_file('myinfo.json', scopes=['https://www.googleapis.com/auth/calendar'])

# Create a service object for interacting with the Google Calendar API.
service = build('calendar', 'v3', credentials=credentials)

with open('kayla.json','r')as file:
    schedule=json.load(file)

recurrence_rule = [
    'RRULE:FREQ=WEEKLY;COUNT=18',  # This example sets a limit of 20 occurrences
]  
for event_data in schedule:
    event_data['recurrence'] = recurrence_rule  # Add the recurrence rule to the event data
    event = service.events().insert(calendarId=calendar_id, body=event_data).execute()
    print(f'Event created: {event.get("htmlLink")}')

print('Recurring events added to your Google Calendar.')





