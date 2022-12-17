import asyncio
import json
import traceback

from request import Request
from utils import make_response
from views import tasks_view, detail_task_view


async def request_handler(raw_request: str):
    request = Request(raw_request)
    # print(f'"{request}"')

    data, message, code = {}, 'Page not found', 404
    if 'tasks/' in request.path:
        if request.path.endswith('tasks/'):
            view = tasks_view
        elif request.path.count('/') == 2:
            view = detail_task_view
        else:
            async def not_found(r):
                return {}, message, code
            view = not_found
        try:
            data, message, code = await view(request)
        except Exception:
            print(traceback.format_exc())
            message, code = 'Something went wrong', 500
    data['message'] = message
    return make_response(path=request.path, body=json.dumps(data), status_code=code)


async def server_flow(reader, writer):
    raw_request = (await reader.read(5000)).decode('utf8')
    if raw_request:
        response = await request_handler(raw_request)
        writer.write(response.encode())
        writer.close()


async def run_server():
    server = await asyncio.start_server(server_flow, '0.0.0.0', 8000)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())
