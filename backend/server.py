import asyncio
import json

from exceptions import BaseRequestError
from request import Request
from utils import make_response
from views import tasks_view, detail_task_view, not_found_view
from http import HTTPStatus
from tasks import delete_tasks


async def request_handler(raw_request: str):
    request = Request(raw_request)
    data, message, code = {}, 'Page not found', HTTPStatus.NOT_FOUND
    if 'tasks/' in request.path:
        url_path = request.path[request.path.find('tasks'):]
        if url_path.endswith('tasks/'):
            view = tasks_view
        elif url_path.count('/') == 3:
            view = detail_task_view
        else:
            view = not_found_view
        try:
            data, message, code = await view(request)
        except BaseRequestError as ex:
            message, code = ex.message, ex.code
        except Exception:
            # print(traceback.format_exc())
            message, code = 'Something went wrong', HTTPStatus.INTERNAL_SERVER_ERROR
    data['message'] = message
    res = make_response(path=request.path, body=json.dumps(data), status=code)
    return res


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


loop = asyncio.get_event_loop()
loop.create_task(run_server())
loop.create_task(delete_tasks())
loop.run_forever()
