var filtros = canvas.append("g")
					.attr("transform", "translate(0," + height.toString() + ")");

// agregar_filtro: str, str(#xxx,#xxxxxx), int(0-14) -> None
// Agrega un filtro abajo de la grilla con el nombre, el color y la poscision indicadas
function agregar_filtro(nombre_sala, color, pos)
{
	var grupo = filtros.append("g")
						.attr("class", "filtro");
						
	var r = 10;
	var cx = width*(1 + 2*(pos%5))/12 + r;
	var cy = r/2 + parseInt(pos/5)*3*r;


	var grupo_fig = grupo.append("g").attr("class", "boton");
	anillo(grupo_fig, cx, cy, '#ffffff', r, 0);
	anillo(grupo_fig, cx, cy, color, r, 0.8*r);
	tick(grupo_fig, cx, cy, color, r).attr("id", nombre_sala.replace(/ /g,"_")+"_filtro");

	grupo_fig.on("click", function() {trigger_filter(nombre_sala);} )
	
	grupo.append("text")
			.attr("x",cx + 15)
			.attr("y",cy)
			.text(nombre_sala);
}

// enable_filter: str -> None
// Prende el tick del filtro asignado a nombre_sala
function enable_filter(nombre_sala)
{
	canvas.select("#" + nombre_sala.replace(/ /g,"_") + "_filtro").attr("opacity", 1.0);
    mostrar_reservas_sala(nombre_sala);
}

// disable_filter: str -> None
// Apaga el tick del filtro asignado a nombre_sala
function disable_filter(nombre_sala)
{
	canvas.select("#" + nombre_sala.replace(/ /g,"_") + "_filtro").attr("opacity", 0.0);
    ocultar_reservas_sala(nombre_sala);
}

function trigger_filter(nombre_sala)
{
    if(canvas.select("#" + nombre_sala.replace(/ /g,"_") + "_filtro").attr("opacity") < 0.5)
        enable_filter(nombre_sala);
    else
        disable_filter(nombre_sala);
}
