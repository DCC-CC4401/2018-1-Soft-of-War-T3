var filtros = canvas.append("g")
					.attr("transform", "translate(0," + height.toString() + ")");

//Maximo 21 caracteres en el nombre
function agregar_filtro(nombre_sala, color, pos)
{
	var grupo = filtros.append("g")
						.attr("class", "filtro");
						
	var r = 10;
	var cx = width*(1 + 2*(pos%5))/12 + r;
	var cy = r/2 + parseInt(pos/5)*3*r;
	
	anillo(grupo, cx, cy, color, r, 0.8*r);
	tick(grupo, cx, cy, color, r).attr("id", nombre_sala.replace(/ /g,"_")+"_filtro");
	
	
	grupo.append("text")
			.attr("x",cx + 15)
			.attr("y",cy)
			.text(nombre_sala);
}

function enable_filter(nombre_sala)
{
	canvas.select("#" + nombre_sala.replace(/ /g,"_") + "_filtro").attr("opacity", 1.0)
}

function disable_filter(nombre_sala)
{
	canvas.select("#" + nombre_sala.replace(/ /g,"_") + "_filtro").attr("opacity", 0.0)
}