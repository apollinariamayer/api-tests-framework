from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """Модель пользователя"""
    id: Optional[int] = None
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None

    def to_dict(self) -> dict:
        """Преобразует объект в словарь"""
        return {k: v for k, v in self.__dict__.items() if v is not None}

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        """Создаёт объект из словаря"""
        return cls(**data)