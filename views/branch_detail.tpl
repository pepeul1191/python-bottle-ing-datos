% include('_header.tpl')
  <h2>{{locals['form_title']}}</h2>
  <div>
    <form action="/branch_detail/save" method="post">
      <input type="hidden" name="id" value="{{locals['branch']['id']}}"><br>
      <label for="name">Nombre:</label><br>
      <input type="text" id="name" name="name"><br>
      <label for="name">Teléfono:</label><br>
      <input type="text" id="phone" name="phone"><br>
      <label for="name">WhatsApp:</label><br>
      <input type="text" id="whastapp" name="whastapp"><br>
      <label for="branch_type_id">Tipo de Sede:</label><br>
      <select name="branch_type_id" disabled id="branch_type_id">
        % for branch_type in locals['branch_type_list']:
          % if int(locals['branch_type_id']) == int(branch_type['id']): 
            <option selected value="{{branch_type['id']}}">{{branch_type['name']}}</option>
          % else:
            <option value="{{branch_type['id']}}">{{branch_type['name']}}</option>
          % end
        % end
      </select>
      <br><br>
      <button class="btn">Guardar Cambios</button>
    </form> 
  </div>
% include('_footer.tpl')