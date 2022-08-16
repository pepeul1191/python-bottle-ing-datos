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
% if locals['worker']['id'] != 'E': 
  <h3>Asociar a Sedes de Lima</h3>
  <form action="/worker/branch" method="post" id="limaBranchForm">
    <input type="hidden" name="worker_id" value="{{locals['worker']['id']}}">
    <input type="hidden" name="url" value="/worker/edit?id={{locals['worker']['id']}}">
    <select multiple="multiple" id="lima_branches" style="height: 200px; width: 300px;">
      % for branch in locals['lima_branchs']:
        % if branch['exist'] == 1: 
          <option selected value="{{branch['id']}}">{{branch['name']}}</option>
        % else:
          <option value="{{branch['id']}}">{{branch['name']}}</option>
        % end
      % end
    </select>
    <br><br><input class="btn" type="submit" onclick="sendMultiple(event,'lima_branches', 'limaBranchForm')" value="Asociar Sedes de Lima" />
  </form>
  <h3>Asociar a Sedes de Provincia</h3>
  <form action="/worker/branch" method="post" id="provinceBranchForm">
    <input type="hidden" name="worker_id" value="{{locals['worker']['id']}}">
    <input type="hidden" name="url" value="/worker/edit?id={{locals['worker']['id']}}">
    <select multiple="multiple" id="province_branches" style="height: 200px; width: 300px;">
      % for branch in locals['province_branchs']:
        % if branch['exist'] == 1: 
          <option selected value="{{branch['id']}}">{{branch['name']}}</option>
        % else:
          <option value="{{branch['id']}}">{{branch['name']}}</option>
        % end
      % end
    </select>
    <br><br><input class="btn" type="submit" onclick="sendMultiple(event,'province_branches', 'provinceBranchForm')" value="Asociar Sedes de Provincia" />
  </form>
% end

<script type="text/javascript">
  function sendMultiple(event, multipleId, formId){
    var selectBox = document.getElementById(multipleId);
    var branches = [];
    var inputExist = document.createElement('input');
    inputExist.setAttribute('type', 'hidden');
    inputExist.setAttribute('name', 'branches_id_exist');
    inputExist.setAttribute('value', '');
    var inputNotExist = document.createElement('input');
    inputNotExist.setAttribute('type', 'hidden');
    inputNotExist.setAttribute('name', 'branches_id_not_exist');
    inputNotExist.setAttribute('value', '');
    for(var i = 0; i < selectBox.options.length; i++){
      if(selectBox.options[i].selected){
        console.log('inputExist' + selectBox.options[i].value)
        console.log(inputExist.value)
        inputExist.value = inputExist.value + ',' + selectBox.options[i].value;
      }else{
        console.log('inputNotExist ' + selectBox.options[i].value)
        console.log(inputExist.value)
        inputNotExist.value = inputNotExist.value + ',' + selectBox.options[i].value;
      }
    }
    inputExist.value = inputExist.value.substr(1);
    inputNotExist.value = inputNotExist.value.substr(1);
    var form = document.getElementById(formId);
    form.appendChild(inputExist);
    form.appendChild(inputNotExist);
  }
</script>

% include('_footer.tpl')