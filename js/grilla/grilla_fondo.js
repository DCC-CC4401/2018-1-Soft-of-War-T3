var width = 1200;
var height = 400;

var canvas = d3.select("#abc")
				.append("svg")
				.attr("width", width)
				.attr("height", height);

var grupo_lineas_base = canvas.append("g");
var grupo_texto_dias = canvas.append("g").attr("class", "titulo_grilla");
					
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


//Lineas Verticales Días

for(i = 3; i <= 9; i+=2)
{
	grupo_lineas_base.append("line")
					.attr("x1", width*i/12)
					.attr("x2", width*i/12)
					.attr("y1", height*3/20)
					.attr("y2", height*(1 + 7*14/6)/20)
					.attr("stroke", "black")
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
