from exceptions import BadRequestError, NotFoundRequestError
from db import get_connection
from request import Request


async def not_found_view(request):
    return {}, 'Page not found', 404


async def tasks_view(request: Request):
    data = {}
    async with get_connection() as conn:
        if request.method == 'GET':
            values = await conn.fetch('SELECT id, name FROM tasks;')
            data = [{'id': _id, 'name': name} for _id, name in values]
        elif request.method == 'POST':
            name = request.json['name']
            result = await conn.fetchval("""
                    INSERT INTO tasks (name)
                    VALUES ($1)
                    RETURNING id""", name)
            data = {'id': result, 'name': name}
    data = {'data': data}
    return data, 'success', 200


async def detail_task_view(request: Request):
    data = {}
    task_id = int(request.path.split('/')[-2])
    async with get_connection() as conn:
        task_name = await conn.fetchval(f'select name from tasks where id = {task_id};')
        if not task_name:
            raise NotFoundRequestError()

        if request.method == 'GET':
            data = {'name': task_name, 'id': task_id}

        if request.method == 'PUT':
            if name := request.json.get('name'):
                await conn.execute(f"update tasks set name = '{name}' where id = {task_id};")
                data = {'name': name, 'id': task_id}
            else:
                raise BadRequestError()
        elif request.method == 'DELETE':
            await conn.execute(f'delete from tasks where id = {task_id};')

    data = {'data': data}
    return data, 'success', 200
