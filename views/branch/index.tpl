% include('_header.tpl')
  <h2>Gestión de Sedes</h2>
  <h3>Sedes de Lima</h3>
  <table style="width:100%">
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Dirección</th>
        <th>Teléfono</th>
        <th>Whatsapp</th>
        <th class="text-center">Operaciones</th>
      </tr>
    </thead>
    <tbody>
      % for branch in locals['lima_branches']:
        <tr>
          <td>{{branch['name']}}</td>
          <td>{{branch['address']}}</td>
          <td>{{branch['phone']}}</td>
          <td>{{branch['whatsapp']}}</td>
          <td class="text-center">
            <a class="btn" href="/branch/edit?id={{branch['id']}}">Editar</a>
            <a class="btn" href="/branch/delete?id={{branch['id']}}">Eliminar</a>
          </td>
        </tr>
      % end
    </tbody>
    <tfoot>
      <a class="btn" href="/branch/create?branch_type_id=1">Agregar Sede de Lima</a>
      <br>
      <br>
    </tfoot>
  </table>
  <h3>Sedes de Provincia</h3>
  <table style="width:100%">
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Dirección</th>
        <th>Teléfono</th>
        <th>Whatsapp</th>
        <th class="text-center">Operaciones</th>
      </tr>
    </thead>
    <tbody>
      % for branch in locals['province_branches']:
        <tr>
          <td>{{branch['name']}}</td>
          <td>{{branch['address']}}</td>
          <td>{{branch['phone']}}</td>
          <td>{{branch['whatsapp']}}</td>
          <td class="text-center">
            <a class="btn" href="/branch/edit?id={{branch['id']}}">Editar</a>
            <a class="btn" href="/branch/delete?id={{branch['id']}}">Eliminar</a>
          </td>
        </tr>
      % end
    </tbody>
    <tfoot>
      <a class="btn" href="/branch/create?branch_type_id=2">Agregar Sede de Provincias</a>
      <br>
      <br>
    </tfoot>
  </table>
  <script type="text/javascript">
  </script>
% include('_footer.tpl')