from flask import Flask, request, Response
import json

app = Flask(__name__)

# تقویم نمونه
try:
    with open('calendar.json', 'r', encoding='utf-8') as f:
        calendar = json.load(f)
except FileNotFoundError:
    calendar = {
                        "1404-01-16": "جلسه با دوستان",
                                "1404-01-17": "کار روی پروژه"
                                    }

@app.route('/api/calendar', methods=['GET'])
def get_calendar():
    return jsonify(calendar)

@app.route('/api/calendar/add', methods=['POST'])
def add_event():
    data = request.json
    date = data.get('date')
    event = data.get('event')
    if date and event:
        calendar[date] = event
        with open('calendar.json', 'w', encoding='utf-8') as f:
            json.dump(calendar, f, ensure_ascii=False)
        return Response(json.dumps({"message": "رویداد با موفقیت ثبت شد", "calendar": calendar}, ensure_ascii=False), mimetype='application/json')
    return Response(json.dumps({"error": "تاریخ یا رویداد وارد نشده است"}, ensure_ascii=False), mimetype='application/json', status=400)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)