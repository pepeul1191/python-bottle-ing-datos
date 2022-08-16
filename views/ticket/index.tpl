% include('_header.tpl')
  <h2>Gestión de Tickets</h2>
  <table style="width:100%">
    <thead>
      <tr>
        <th>N° Ticket</th>
        <th>Estado</th>
        <th>Prioridad</th>
        <th>Sede</th>
        <th>Creado</th>
        <th>Editado</th>
        <th>Reportado</th>
        <th>Resumen</th>
        <th class="text-center">Operaciones</th>
      </tr>
    </thead>
    <tbody>
      % for ticket in locals['tickets']:
        <tr>
          <td>{{ticket['id']}}</td>
          <td>{{ticket['state_name']}}</td>
          <td>{{ticket['priority_name']}}</td>
          <td>{{ticket['branch_name']}}</td>
          <td>{{ticket['created']}}</td>
          <td>{{ticket['edited']}}</td>
          <td>{{ticket['worker_name']}}</td>
          <td>{{ticket['resume']}}</td>
          <td class="text-center">
            <a class="btn" href="/ticket/edit?id={{ticket['id']}}">Editar</a>
            <a class="btn" href="/ticket/delete?id={{ticket['id']}}">Eliminar</a>
          </td>
        </tr>
      % end
    </tbody>
    <tfoot>
      <a class="btn" href="/ticket/create?ticket_type_id=1">Agregar Posición</a>
      <br>
      <br>
      % if locals['page'] != 1: 
        <a class="btn" href="/ticket?step=10&page=1">Primero</a>&nbsp;&nbsp;
        <a class="btn" href="/ticket?step=10&page={{locals['page'] - 1}}">Anterior</a>&nbsp;&nbsp;
      % end
      {{locals['page']}}/ {{locals['pages']}}&nbsp;&nbsp;
      % if locals['page'] != locals['pages']: 
        <a class="btn" href="/ticket?step=10&page={{locals['page'] + 1}}">Siguiente</a>&nbsp;&nbsp;
        <a class="btn" href="/ticket?step=10&page={{locals['pages']}}">Último</a>
      % end
      <br>
      <br>
    </tfoot>
  </table>
  <script type="text/javascript">
  </script>
% include('_footer.tpl')