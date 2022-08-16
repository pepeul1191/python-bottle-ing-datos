% include('_header.tpl')

<h2>{{locals['form_title']}}</h2>
<div>
  <form action="/worker/save" method="post">
    <input type="hidden" name="id" value="{{locals['worker']['id']}}"><br>
    <label for="name">Nombres:</label><br>
    <input type="text" id="names" name="names" value="{{locals['worker']['names']}}"><br>
    <label for="name">Apellidos:</label><br>
    <input type="text" id="last_names" name="last_names" value="{{locals['worker']['last_names']}}"><br>
    <label for="name">Correo:</label><br>
    <input type="text" id="email" name="email" value="{{locals['worker']['email']}}"><br>
    <label for="name">Teléfono:</label><br>
    <input type="text" id="phone" name="phone" value="{{locals['worker']['phone']}}"><br>
    <label for="position_id">Tipo de Empleado:</label><br>
    <select name="position_id" id="position_id">
      % for position in locals['position_list']:
        % if int(locals['worker']['position_id']) == int(position['id']): 
          <option selected value="{{position['id']}}">{{position['name']}}</option>
        % else:
          <option value="{{position['id']}}">{{position['name']}}</option>
        % end
      % end
    </select>
    <br><br>
    <button class="btn">Guardar Cambios</button>
  </form> 
</div>

% include('_footer.tpl')