import click
from app.models import db, AccessLog
from flask import Flask
from config.settings import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
db.init_app(app)

@app.cli.command('view-logs')
@click.option('--start-date', default=None, help='Start date in YYYY-MM-DD format')
@click.option('--end-date', default=None, help='End date in YYYY-MM-DD format')
@click.option('--ip-address', default=None, help='Filter by IP address')
def view_logs(start_date, end_date, ip_address):
    query = AccessLog.query
    if start_date:
        query = query.filter(AccessLog.timestamp >= start_date)
    if end_date:
        query = query.filter(AccessLog.timestamp <= end_date)
    if ip_address:
        query = query.filter(AccessLog.ip_address == ip_address)

    logs = query.all()
    for log in logs:
        click.echo(f'{log.timestamp} {log.ip_address} {log.request_method} {log.request_path} {log.status_code}')

if __name__ == '__main__':
    app.run(debug=True)
