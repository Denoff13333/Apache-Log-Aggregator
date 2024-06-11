import os
import glob
from datetime import datetime
from app.models import db, AccessLog
from config.settings import config
from app import create_app

app = create_app()
app.app_context().push()

def parse_log_line(line):
    parts = line.split()
    ip_address = parts[0]
    timestamp = datetime.strptime(parts[3][1:], '%d/%b/%Y:%H:%M:%S')
    request_method = parts[5][1:]
    request_path = parts[6]
    status_code = int(parts[8])
    user_agent = ' '.join(parts[11:])
    return ip_address, timestamp, request_method, request_path, status_code, user_agent

def parse_logs():
    log_files = glob.glob(os.path.join(config.LOG_DIR, config.LOG_MASK))
    for log_file in log_files:
        with open(log_file, 'r') as file:
            for line in file:
                ip_address, timestamp, request_method, request_path, status_code, user_agent = parse_log_line(line)
                access_log = AccessLog(
                    ip_address=ip_address,
                    timestamp=timestamp,
                    request_method=request_method,
                    request_path=request_path,
                    status_code=status_code,
                    user_agent=user_agent
                )
                db.session.add(access_log)
        db.session.commit()

if __name__ == '__main__':
    parse_logs()
