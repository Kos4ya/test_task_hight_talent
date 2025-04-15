# Restaurant Table Reservation API

Сервис FastAPI для управления бронированием столиков в ресторанах с использованием базы данных PostgreSQL.
## Для запуска


### Загрузка
```bash
git clone https://github.com/Kos4ya/test_task_hight_talent.git
cd restaurant-reservation-api
```

### .env
Для работы сервиса, необходимо создать .env в корне проекта, например:

````dotenv
POSTGRES_USER=booking_user
POSTGRES_PASSWORD=booking_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=db
DATABASE_URL=postgresql://booking_user:booking_password@db:5432/db
````

### Для запуска
```bash
docker-compose up -d --build
```