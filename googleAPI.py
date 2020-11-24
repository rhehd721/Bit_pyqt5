from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    DateList = []
    ScheduleList = []

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start, event['summary'],) # 나의 캘린더 이벤트 리스트를 보여준다 다수도가능
        #print(start) # 날짜하고 시간
        dataVar, timeVar = start.split('T') # T를 기준으로 자름
        print(dataVar + ' ' + timeVar, event['summary'])
        
        DateList.append(dataVar)
        ScheduleList.append(event['summary'])

    return DateList, ScheduleList


# if __name__ == '__main__':
#     main()





    # 프린트 에서 찍는게 어디인지 확인해보자


    # 스케쥴이 2개로 나온다  최대 10개 이벤트 까지 갖고왔을때 날짜와 시간과 이벤트내용의 이름을
    # 리스트로 저장을 해야 한다


    # 리스트를 갖고오면, def showDate 가지고 그 데이터를 갖고 검색을 할것이다.
    # for문을 돌려서 현재 갖고 온 날짜와 내가 스케쥴을 갖고 있는 날짜와 동일 한것이 있는지를
    # 확인하는것이다.
    # 리스트가 1개이면 1 여러개라면 여러개 다 찍어주면 된다.
