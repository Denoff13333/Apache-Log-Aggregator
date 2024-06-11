from flask import Flask, request, jsonify
from app.models import db, AccessLog
from config.settings import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
db.init_app(app)

@app.route('/api/logs', methods=['GET'])
def get_logs():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    ip_address = request.args.get('ip_address')
    
    query = AccessLog.query
    if start_date:
        query = query.filter(AccessLog.timestamp >= start_date)
    if end_date:
        query = query.filter(AccessLog.timestamp <= end_date)
    if ip_address:
        query = query.filter(AccessLog.ip_address == ip_address)

    logs = query.all()
    result = [{
        'ip_address': log.ip_address,
        'timestamp': log.timestamp,
        'request_method': log.request_method,
        'request_path': log.request_path,
        'status_code': log.status_code,
        'user_agent': log.user_agent
    } for log in logs]

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
