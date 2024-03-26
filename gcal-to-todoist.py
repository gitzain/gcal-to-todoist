import datetime
import os
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from todoist_api_python.api import TodoistAPI
import json

# Environment variables
GOOGLE_SERVICE_KEY = os.environ.get('GOOGLE_SERVICE_KEY')
GOOGLE_CALENDAR_ID = os.environ.get('GOOGLE_CALENDAR_ID')
TODOIST_API_TOKEN = os.environ.get('TODOIST_API_TOKEN')
TODOIST_REFRESH_TOKEN = os.environ.get('TODOIST_REFRESH_TOKEN')
TODOIST_PROJECT_ID = os.environ.get('TODOIST_PROJECT_ID')

# Google Calendar API setup
google_service_key_contents = GOOGLE_SERVICE_KEY
credentials = Credentials.from_service_account_info(json.loads(google_service_key_contents), scopes=['https://www.googleapis.com/auth/calendar.readonly'])
service = build('calendar', 'v3', credentials=credentials)

# Today's date and time ranges
today = datetime.date.today().isoformat()
start_time = f"{today}T00:00:00Z"
end_time = f"{today}T23:59:59Z"

# Fetch events from today
events_result = service.events().list(
    calendarId=GOOGLE_CALENDAR_ID,
    timeMin=start_time,
    timeMax=end_time,
    singleEvents=True,
    orderBy='startTime'
).execute()
events = events_result.get('items', [])

api = TodoistAPI(TODOIST_API_TOKEN)  # Use todoist-api-python

# Process and add events to Todoist
if not events:
    print('No events found for today.')
else:
    for event in events:
        summary = event['summary']
        due_date = event['start'].get('dateTime')

        try:
            tasks = api.get_tasks(
                project_id=TODOIST_PROJECT_ID,
                due_datetime=due_date if due_date else None
            )

            already_exists = False
            for current_task in tasks:
                if current_task.content == summary and current_task.due.datetime == due_date:
                    already_exists = True

            
            if not already_exists:
                task = api.add_task(
                    content=summary,
                    project_id=TODOIST_PROJECT_ID,
                    due_datetime=due_date if due_date else None,
                    priority=1
                )
        except Exception as error:
            print(error)
