from dataclasses import dataclass
from typing import Optional


@dataclass
class Post:
    """Модель поста"""
    id: Optional[int] = None
    userId: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None

    def to_dict(self) -> dict:
        """Преобразует объект в словарь"""
        return {k: v for k, v in self.__dict__.items() if v is not None}

    @classmethod
    def from_dict(cls, data: dict) -> 'Post':
        """Создаёт объект из словаря"""
        return cls(**data)