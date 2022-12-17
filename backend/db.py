import os
from contextlib import asynccontextmanager

import asyncpg


@asynccontextmanager
async def get_connection():
    username = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    database_name = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_HOST', default='localhost')
    connection = await asyncpg.connect(user=username, password=password, database=database_name, host=host)
    yield connection
    await connection.close()
