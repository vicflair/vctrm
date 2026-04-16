from flask import Flask, render_template
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

app = Flask(__name__)

ACTIVITY_ID = 'B0KovYOcQun1mA4VowDq0'
VENUE_ID = 'pJtsNwSdC2fgSg5oWPdf1'
DAYS_AHEAD = 12
SG_TZ = ZoneInfo('Asia/Singapore')
SITE_TZ = ZoneInfo('Asia/Singapore')  # ActiveSG encodes timestamps in SGT (UTC+8)


BASE_URL = (
    f"https://activesg.gov.sg/facility-bookings/activities/{ACTIVITY_ID}"
    f"/venues/{VENUE_ID}/timeslots"
    f"?activityId={ACTIVITY_ID}&venueId={VENUE_ID}"
)


@app.route('/')
def index():
    today = datetime.now(SG_TZ).date()
    target_date = today + timedelta(days=DAYS_AHEAD)
    date_str = target_date.strftime('%Y-%m-%d')

    slots = [
        {
            'label': f'{h - 12}pm',
            'ts': int(datetime(target_date.year, target_date.month, target_date.day, h, 0, tzinfo=SITE_TZ).timestamp() * 1000),
        }
        for h in range(17, 22)  # 5pm to 9pm
    ]

    return render_template('index.html', date=date_str, slots=slots,
                           base_url=BASE_URL, activity_id=ACTIVITY_ID, venue_id=VENUE_ID)


if __name__ == '__main__':
    app.run(debug=True)
