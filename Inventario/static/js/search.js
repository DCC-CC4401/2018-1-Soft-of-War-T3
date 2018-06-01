$('#busquedProyecto').keyup(function(e){
 consulta = $("#busqueda").val();
 $.ajax({
 data: {'title': consulta},
 url: '/productos/busqueda/',
 type: 'get',
 success : function(data) {
         console.log(data[0].title);
 },
 error : function(message) {
         console.log(message);
      }
 });
});
