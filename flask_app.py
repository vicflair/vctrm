from flask import Flask, render_template
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

app = Flask(__name__)

ACTIVITY_ID = 'B0KovYOcQun1mA4VowDq0'
VENUE_ID = 'pJtsNwSdC2fgSg5oWPdf1'
DAYS_AHEAD = 12
SG_TZ = ZoneInfo('Asia/Singapore')
SITE_TZ = ZoneInfo('Asia/Tokyo')  # ActiveSG encodes timestamps in UTC+9


@app.route('/')
def index():
    today = datetime.now(SG_TZ).date()
    target_date = today + timedelta(days=DAYS_AHEAD)
    date_str = target_date.strftime('%Y-%m-%d')

    ts_6pm = int(datetime(target_date.year, target_date.month, target_date.day, 18, 0, tzinfo=SITE_TZ).timestamp() * 1000)
    ts_7pm = int(datetime(target_date.year, target_date.month, target_date.day, 19, 0, tzinfo=SITE_TZ).timestamp() * 1000)

    url = (
        f"https://activesg.gov.sg/facility-bookings/activities/{ACTIVITY_ID}"
        f"/venues/{VENUE_ID}/timeslots"
        f"?activityId={ACTIVITY_ID}&venueId={VENUE_ID}"
        f"&date={date_str}&timeslots={ts_6pm}&timeslots={ts_7pm}"
    )

    return render_template('index.html', url=url, date=date_str)


if __name__ == '__main__':
    app.run(debug=True)
