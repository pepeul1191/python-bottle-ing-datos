% include('_header.tpl')
  <h2>{{locals['form_title']}}</h2>
  <div>
    <form action="/position/save" method="post">
      <input type="hidden" name="id" value="{{locals['position']['id']}}"><br>
      <label for="name">Nombre:</label><br>
      <input type="text" id="name" name="name" value="{{locals['position']['name']}}"><br>
      <br>
      <button class="btn">Guardar Cambios</button>
    </form> 
  </div>
% include('_footer.tpl')