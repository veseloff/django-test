"""Создание пула соеднений"""
import asyncpg
from config import HOST, DB_PASS, DB_NAME, DB_USER, PORT


async def create_pool():
    """
    Создание пула соединений
    Returns:

    """
    return await asyncpg.create_pool(user=DB_USER, password=DB_PASS, host=HOST, port=PORT, database=DB_NAME)
