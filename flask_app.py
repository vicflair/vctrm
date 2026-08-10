from flask import Flask, render_template
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

app = Flask(__name__)

ACTIVITY_ID = 'B0KovYOcQun1mA4VowDq0'
DAYS_AHEAD = 12
SG_TZ = ZoneInfo('Asia/Singapore')
SITE_TZ = ZoneInfo('Asia/Singapore')  # ActiveSG encodes timestamps in SGT (UTC+8)

VENUES = [
    {'name': 'Kallang', 'id': 'pJtsNwSdC2fgSg5oWPdf1'},
    {'name': 'Heartbeat', 'id': 'qFjN7QRByrxM5Ikhv9UQm'},
]

BASE_URL_TEMPLATE = (
    "https://activesg.gov.sg/facility-bookings/activities/{activity_id}"
    "/venues/{venue_id}/timeslots"
    "?activityId={activity_id}&venueId={venue_id}"
)


@app.route('/')
def index():
    today = datetime.now(SG_TZ).date()
    target_date = today + timedelta(days=DAYS_AHEAD)
    date_param = target_date.strftime('%Y-%m-%d')
    date_str = target_date.strftime('%A, %Y-%m-%d')

    slots = [
        {
            'label': f'{h - 12}pm',
            'ts': int(datetime(target_date.year, target_date.month, target_date.day, h, 0, tzinfo=SITE_TZ).timestamp() * 1000),
        }
        for h in range(17, 22)  # 5pm to 9pm
    ]

    return render_template('index.html', date=date_str, date_param=date_param, slots=slots,
                           activity_id=ACTIVITY_ID, venues=VENUES,
                           base_url_template=BASE_URL_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True)
