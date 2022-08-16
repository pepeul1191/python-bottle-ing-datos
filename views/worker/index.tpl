% include('_header.tpl')
  <h2>Gestión de Empleados</h2>
  <table style="width:100%">
    <thead>
      <tr>
        <th>Apellidos</th>
        <th>Nombres</th>
        <th>Correo</th>
        <th>Teléfono</th>
        <th>Posición</th>
        <th class="text-center">Operaciones</th>
      </tr>
    </thead>
    <tbody>
      % for worker in locals['workers']:
        <tr>
          <td>{{worker['last_names']}}</td>
          <td>{{worker['names']}}</td>
          <td>{{worker['email']}}</td>
          <td>{{worker['phone']}}</td>
          <td>{{worker['position_name']}}</td>
          <td class="text-center">
            <a class="btn" href="/worker/edit?id={{worker['id']}}">Editar</a>
            <a class="btn" href="/worker/delete?id={{worker['id']}}">Eliminar</a>
          </td>
        </tr>
      % end
    </tbody>
    <tfoot>
      <a class="btn" href="/worker/create">Agregar Empleado</a>
      <br>
      <br>
      % if locals['page'] != 1: 
        <a class="btn" href="/worker?step=10&page=1">Primero</a>&nbsp;&nbsp;
        <a class="btn" href="/worker?step=10&page={{locals['page'] - 1}}">Anterior</a>&nbsp;&nbsp;
      % end
      {{locals['page']}}/ {{locals['pages']}}&nbsp;&nbsp;
      % if locals['page'] != locals['pages']: 
        <a class="btn" href="/worker?step=10&page={{locals['page'] + 1}}">Siguiente</a>&nbsp;&nbsp;
        <a class="btn" href="/worker?step=10&page={{locals['pages']}}">Último</a>
      % end
      <br>
      <br>
    </tfoot>
  </table>

% include('_footer.tpl')