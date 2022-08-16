% include('_header.tpl')
  <h2>Gestión de Estados</h2>
  <table style="width:100%">
    <thead>
      <tr>
        <th>Nombre</th>
        <th class="text-center">Operaciones</th>
      </tr>
    </thead>
    <tbody>
      % for state in locals['states']:
        <tr>
          <td>{{state['name']}}</td>
          <td class="text-center">
            <a class="btn" href="/state/edit?id={{state['id']}}">Editar</a>
            <a class="btn" href="/state/delete?id={{state['id']}}">Eliminar</a>
          </td>
        </tr>
      % end
    </tbody>
    <tfoot>
      <a class="btn" href="/state/create?state_type_id=1">Agregar Posición</a>
      <br>
      <br>
    </tfoot>
  </table>
  <script type="text/javascript">
  </script>
% include('_footer.tpl')