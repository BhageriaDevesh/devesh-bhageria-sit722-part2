import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://task6_i4ny_user:k43vJY2e0dxIUPVq8vOX8nwM98a5Ki1O@dpg-crnut4m8ii6s73f0ai00-a.oregon-postgres.render.com:5432/task6_i4ny")

settings = Settings()
