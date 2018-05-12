var width = 1200;
var height = 400;
var height_filtros = 400;

var canvas = d3.select("#abc")
				.append("svg")
				.attr("width", width)
				.attr("height", height + height_filtros);

var grupo_lineas_base = canvas.append("g");
var grupo_texto_horas = canvas.append("g").attr("class", "horas_grilla");
var grupo_texto_dias = canvas.append("g").attr("class", "dias_grilla");
					
//Lineas Horizontales Horas

for(i = 2; i <= 6; i++)
{
	grupo_lineas_base.append("line")
					.attr("x1", width/12)
					.attr("x2", width*11/12)
					.attr("y1", height*(1 + i*14/6)/20)
					.attr("y2", height*(1 + i*14/6)/20)
					.attr("stroke", "#aaa")
					.attr("stroke-width", 1);
}					


// Dias de la Semana

var dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
for(i = 0; i < 5; i++)
{
	grupo_texto_dias.append("text")
						.attr("x", width*(i+1)/6)
						.attr("y", height/10)
						.text(dias[i]);
}


//Horas del dia

var horas = ["10:00","12:00","14:00","16:00","18:00"]
for(i = 2; i <= 6; i++)
{
	grupo_texto_horas.append("text")
					.attr("x", 15*width/192)
					.attr("y", height*(1 + i*14/6)/20)
					.text(horas[i-2]);
}	
