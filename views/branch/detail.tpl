% include('_header.tpl')

<h2>{{locals['form_title']}}</h2>
<div>
  <form action="/branch/save" method="post">
    <input type="hidden" name="id" value="{{locals['branch']['id']}}"><br>
    <label for="name">Nombre:</label><br>
    <input type="text" id="name" name="name" value="{{locals['branch']['name']}}"><br>
    <label for="name">Dirección:</label><br>
    <input type="text" id="address" name="address" value="{{locals['branch']['address']}}"><br>
    <label for="name">Teléfono:</label><br>
    <input type="text" id="phone" name="phone" value="{{locals['branch']['phone']}}"><br>
    <label for="name">WhatsApp:</label><br>
    <input type="text" id="whatsapp" name="whatsapp" value="{{locals['branch']['whatsapp']}}"><br>
    <label for="branch_type_id">Tipo de Sede:</label><br>
    <select name="branch_type_id" id="branch_type_id">
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
<script type="text/javascript">
</script>

% include('_footer.tpl')