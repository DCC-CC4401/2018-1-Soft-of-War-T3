var grupo_lineas_base = canvas.append("g");
var grupo_botones = canvas.append("g");

//Botones

var y_botones = (height*(1 + 7*14/6)/20 + height*19/20)/2;

var boton_semana_siguiente = grupo_botones.append("a").attr("id", "boton_semana_siguiente_grilla").append("g");
var boton_semana_anterior = grupo_botones.append("a").attr("id", "boton_semana_anterior_grilla").append("g");

triangulo_derecha(boton_semana_siguiente, width*7/12, y_botones, "#333", height/40);
triangulo_izquierda(boton_semana_anterior, width*5/12, y_botones, "#333", height/40);

var boton_mes_siguiente = grupo_botones.append("a").attr("id", "boton_mes_siguiente_grilla").append("g");
var boton_mes_anterior = grupo_botones.append("a").attr("id", "boton_mes_anterior_grilla").append("g");

doble_triangulo_derecha(boton_mes_siguiente, width*9/12, y_botones, "#333", height/40);
doble_triangulo_izquierda(boton_mes_anterior, width*3/12, y_botones, "#333", height/40);


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

//Lineas Horizontales Marco
grupo_lineas_base.append("line")
					.attr("x1", width/12)
					.attr("x2", width*11/12)
					.attr("y1", height*3/20)
					.attr("y2", height*3/20)
					.attr("stroke", "black")
					.attr("stroke-width", 2);
					
grupo_lineas_base.append("line")
					.attr("x1", width/12)
					.attr("x2", width*11/12)
					.attr("y1", height*19/20)
					.attr("y2", height*19/20)
					.attr("stroke", "black")
					.attr("stroke-width", 2);

grupo_lineas_base.append("line")
					.attr("x1", width/12)
					.attr("x2", width*11/12)
					.attr("y1", height*(1 + 7*14/6)/20)
					.attr("y2", height*(1 + 7*14/6)/20)
					.attr("stroke", "black")
					.attr("stroke-width", 2);

//Lineas Verticales	Marco				
grupo_lineas_base.append("line")
					.attr("x1", width/12)
					.attr("x2", width/12)
					.attr("y1", height*3/20)
					.attr("y2", height*19/20)
					.attr("stroke", "black")
					.attr("stroke-width", 2);
					
grupo_lineas_base.append("line")
					.attr("x1", width*11/12)
					.attr("x2", width*11/12)
					.attr("y1", height*3/20)
					.attr("y2", height*19/20)
					.attr("stroke", "black")
					.attr("stroke-width", 2);


					
