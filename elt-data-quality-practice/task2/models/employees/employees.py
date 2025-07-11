from datetime import date

from sqlalchemy import String, Date, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Text
from task2.models.base import Base
from task2.repr_generator import generate_repr


@generate_repr()
class Employees(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text)
    date_of_birth: Mapped[date] = mapped_column(Date)
    salary: Mapped[int] = mapped_column(Integer)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey('departments.id'))