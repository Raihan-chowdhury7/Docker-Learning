import pytz 
from flask import Flask, render_template
import redis, os
from datetime import datetime, timedelta

app = Flask(__name__)
r = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=int(os.getenv('REDIS_PORT', 6379)))

@app.route('/')
def welcome():
    return render_template("index.html")


@app.route('/count')
def count():
    total = r.incr('visits')

    now = datetime.utcnow()
    hour_key = now.strftime('visits:%Y-%m-%d:%H')
    r.incr(hour_key)

    local_tz = pytz.timezone("Europe/London")

    labels = []
    values = []
    for i in range(23, -1, -1):
        hour = now - timedelta(hours=i)
        key = hour.strftime('visits:%Y-%m-%d:%H')

        local_hour = hour.replace(tzinfo=pytz.utc).astimezone(local_tz)
        label = local_hour.strftime('%H:00')

        labels.append(label)
        values.append(int(r.get(key) or 0))


    return render_template("count.html", count=total, labels=labels, values=values)

@app.route('/reset')
def reset():
    # Reset total visit count
    r.set('visits', 0)

    # Delete all hourly keys
    for key in r.scan_iter("visits:*:*"):
        r.delete(key)

    return "Visit counter and chart data have been reset."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
    
