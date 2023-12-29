# Google Calendar Event Creator

This script allows you to create recurring events in your Google Calendar using event data from a JSON file.

## Requirements

- Python 3
- `google-auth`, `google-auth-httplib2`, `google-auth-oauthlib`, `google-api-python-client`, and `oauthlib` Python libraries. You can install these using pip:
    ```bash
    pip install --upgrade google-auth google-auth-httplib2 google-auth-oauthlib google-api-python-client oauthlib
    ```
- A Google account with Calendar enabled
- A service account key file (in JSON format) from Google Cloud Console

## Usage

1. Replace `'************'` with your Google Calendar ID in the `calendar_id` variable. This is usually the email address associated with your Google Calendar.

2. Replace `'myinfo.json'` with the path to your service account key file in the `from_service_account_file` function.

3. Replace `'kaylaPersonal.json'` with the path to your JSON file containing the event data in the `open` function.

4. Run the script:
    ```bash
    python script.py
    ```

The script will create recurring events in your Google Calendar using the event data from the specified JSON file. The recurrence rule is set to create weekly events for a total of 18 occurrences.

After each event is created, the script will print the URL of the event. Once all events have been created, the script will print "Recurring events added to your Google Calendar."
