# Apache Log Aggregator

## Установка

1. Клонируйте репозиторий:
    
    git clone https://github.com/Denoff13333/apache-log-aggregator.git
    cd C:\Users\Denil\apache\apache-log-aggregator
    

2. Установите виртуальное окружение и зависимости:
    
    python3 -m venv venv
    Set-ExecutionPolicy RemoteSigned -Scope Process
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Настройте конфигурацию в `C:\Users\Denil\apache\apache-log-aggregator\config/settings.py`.

4. Инициализируйте базу данных:
    
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Запустите парсинг логов:
    
    python scripts/parse_logs.py
    

6. Запустите сервер:
    
    flask run
    

## Использование

- Для просмотра логов через консоль:
    
    flask view-logs --start-date YYYY-MM-DD --end-date YYYY-MM-DD --ip-address x.x.x.x
    

- API доступно по адресу `http://localhost:5000/api/logs`.
