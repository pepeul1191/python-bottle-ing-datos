% include('_header.tpl')
  <h2>Gestión de Posiciones</h2>
  <table style="width:100%">
    <thead>
      <tr>
        <th>Nombre</th>
        <th class="text-center">Operaciones</th>
      </tr>
    </thead>
    <tbody>
      % for position in locals['positions']:
        <tr>
          <td>{{position['name']}}</td>
          <td class="text-center">
            <a class="btn" href="/position/edit?id={{position['id']}}">Editar</a>
            <a class="btn" href="/position/delete?id={{position['id']}}">Eliminar</a>
          </td>
        </tr>
      % end
    </tbody>
    <tfoot>
      <a class="btn" href="/position/create?position_type_id=1">Agregar Posición</a>
      <br>
      <br>
    </tfoot>
  </table>

% include('_footer.tpl')