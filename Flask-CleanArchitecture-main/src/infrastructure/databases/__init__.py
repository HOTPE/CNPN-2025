# src/infrastructure/databases/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

# Lấy connection string từ biến môi trường, nếu không có thì fallback sang SQLite
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///default.db"   # fallback khi chưa config
)

# Khởi tạo engine
engine = create_engine(
    DATABASE_URL,
    echo=True,   # log query ra console (bỏ nếu không cần)
    future=True
)

# Session local cho repository/service sử dụng
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Khởi tạo database (tạo bảng nếu chưa có)."""
    import infrastructure.models  # import tất cả model để Base biết
    Base.metadata.create_all(bind=engine)
