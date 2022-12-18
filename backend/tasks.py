import asyncio

from db import get_connection


async def delete_tasks():
    while True:
        async with get_connection() as conn:
            sql = 'delete from tasks;'
            await conn.execute(sql)
        print('Tasks deleted successfully')
        await asyncio.sleep(120)

