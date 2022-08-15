def menu(url):
  itmes = [
    {'name': 'Home', 'url': '/', 'active': False},
    {'name': 'Formulario', 'url': '/formulario', 'active': False},
    {'name': 'Demo', 'url': '/demo', 'active': False},
  ]
  for item in itmes:
    if item['url'] == url:
      item['active'] = True
  return itmes
