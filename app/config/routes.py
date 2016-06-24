
from system.core.router import routes

routes['default_controller'] = 'Pokes'
routes['POST']['/pokes/register'] = 'Pokes#register'
routes['POST']['/pokes/login'] = 'Pokes#login'
routes['POST']['/pokes/logout'] = 'Pokes#logout'
routes['/pokes'] = 'Pokes#show'
routes['POST']['/pokes/value/<id>'] = 'Pokes#get_pokes_by_id'
routes['POST']['/addpoke'] = 'Pokes#add_poke'

