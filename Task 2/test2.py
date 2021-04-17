from aiohttp import web
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://user:Kranvagn13@cluster0.du8uq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster['test']
collection = db['ips']

async def history(request):
    #getting requested value from address string
    ip = request.match_info['ip'].strip()
    #looking for value in collection
    data = collection.find({'ip':f'{ip}'})
    result = []
    #iterating through found values
    for el in data:
        result.append(el)
    #if nothing found, returning message
    if not result:
        return web.Response(text = f'No data about {ip}')
    #otherwise, returning result
    return web.json_response({'result':result})

async def noticed(request):
    result = []
    #iterating through all collection documents (way 2)
    for el in collection.find({}):
        result.append(el['ip'])
    #if nothing found, returning message
    if not result:
        return web.Response(text = 'No activity')
    #otherwise, returing result
    return web.json_response({'result': list(set(result))})

#creating application
app = web.Application()
#adding routes
app.add_routes([web.get('/history/{ip}', history),
                web.get('/noticed', noticed)])

if __name__ == "__main__":
    #running it
    web.run_app(app, port = 8000)