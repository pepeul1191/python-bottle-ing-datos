% include('_header.tpl')
  <h2>{{locals['form_title']}}</h2>
  <div>
    <form action="/state/save" method="post">
      <input type="hidden" name="id" value="{{locals['state']['id']}}"><br>
      <label for="name">Nombre:</label><br>
      <input type="text" id="name" name="name" value="{{locals['state']['name']}}"><br>
      <br>
      <button class="btn">Guardar Cambios</button>
    </form> 
  </div>
  <script type="text/javascript">
  </script>
% include('_footer.tpl')