var grupo_lineas_base = canvas.append("g");
var grupo_texto_dias = canvas.append("g").attr("class", "titulo_grilla");

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

					
