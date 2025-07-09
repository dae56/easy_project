from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.app.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    date_of_birth: Mapped[date]
    email: Mapped[str] = mapped_column(String(254))
    is_active: Mapped[bool]
