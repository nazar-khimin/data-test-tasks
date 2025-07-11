from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from task2.models.base import Base
from task2.repr_generator import generate_repr


@generate_repr()
class Departments(Base):
    __tablename__ = "departments"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))