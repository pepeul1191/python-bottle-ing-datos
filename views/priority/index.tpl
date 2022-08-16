% include('_header.tpl')
  <h2>Gestión de Prioridades</h2>
  <table style="width:100%">
    <thead>
      <tr>
        <th>Nombre</th>
        <th class="text-center">Operaciones</th>
      </tr>
    </thead>
    <tbody>
      % for priority in locals['priorities']:
        <tr>
          <td>{{priority['name']}}</td>
          <td class="text-center">
            <a class="btn" href="/priority/edit?id={{priority['id']}}">Editar</a>
            <a class="btn" href="/priority/delete?id={{priority['id']}}">Eliminar</a>
          </td>
        </tr>
      % end
    </tbody>
    <tfoot>
      <a class="btn" href="/priority/create?priority_type_id=1">Agregar Posición</a>
      <br>
      <br>
    </tfoot>
  </table>
  <script type="text/javascript">
  </script>
% include('_footer.tpl')