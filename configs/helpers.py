def menu(url):
  itmes = [
    {'name': 'Home', 'url': '/', 'active': False},
    {'name': 'Gestión de Sedes', 'url': '/branch', 'active': False},
    {'name': 'Gestión de Posiciones', 'url': '/position', 'active': False},
    {'name': 'Gestión de Tickets', 'url': '/ticket?step=10&page=1', 'active': False},
    {'name': 'Demo', 'url': '/demo', 'active': False},
  ]
  for item in itmes:
    if url in item['url']:
      item['active'] = True
  return itmes
