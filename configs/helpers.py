def menu(url):
  itmes = [
    {'name': 'Home', 'url': '/', 'active': False},
    {'name': 'Gestión de Sedes', 'url': '/branch', 'active': False},
    {'name': 'Gestión de Posiciones', 'url': '/position', 'active': False},
    {'name': 'Gestión de Prioridades', 'url': '/priority', 'active': False},
    {'name': 'Gestión de Estados', 'url': '/state', 'active': False},
    {'name': 'Gestión de Empleados', 'url': '/employee?step=10&page=1', 'active': False},
    {'name': 'Gestión de Tickets', 'url': '/ticket?step=10&page=1', 'active': False},
    {'name': 'Demo', 'url': '/demo', 'active': False},
  ]
  proceed = True
  for item in itmes:
    if url == item['url']:
      item['active'] = True
      proceed = False
    else :
      if proceed and url in item['url']:
        item['active'] = True
  return itmes
