# Apache Log Aggregator

## Установка

1. Клонируйте репозиторий:
    
    git clone https://github.com/Denoff13333/apache-log-aggregator.git
   
    cd C:\Users\Denil\apache\apache-log-aggregator
    

3. Установите виртуальное окружение и зависимости:
    
    python3 -m venv venv
   
    Set-ExecutionPolicy RemoteSigned -Scope Process
   
    venv\Scripts\activate
   
    pip install -r requirements.txt
    

5. Настройте конфигурацию в `C:\Users\Denil\apache\apache-log-aggregator\config/settings.py`.

6. Инициализируйте базу данных:
    
    flask db init
   
    flask db migrate
   
    flask db upgrade
    

8. Запустите парсинг логов:
    
    python parse_logs.py
    
( Надо находиться в нужной дериктории )

9. Запустите сервер:
    
    flask run
    

## Использование

- Для просмотра логов через консоль:
    
    flask view-logs --start-date YYYY-MM-DD --end-date YYYY-MM-DD --ip-address x.x.x.x
    

- API доступно по адресу `http://localhost:5000/api/logs`.
