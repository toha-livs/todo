from db import get_connection
from request import Request


async def tasks_view(request: Request):
    data = {}
    async with get_connection() as conn:
        if request.method == 'GET':
            values = await conn.fetchall('SELECT id, name FROM tasks;')
            data = {'data': [{'id': _id, 'name': name} for _id, name in values]}
        elif request.method == 'POST':
            name = request.json['name']
            sql = f'INSERT INTO tasks(name) VALUES ("{name}");'
            await conn.fetchval("""
                    INSERT INTO tasks (name)
                    VALUES ($1)
                    RETURNING id""", name)
            result = conn.fetchval(sql)
            data = {'id': result[0], 'name': name}
    return data, 'success', 200


async def detail_task_view(request: Request):
    pass