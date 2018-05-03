
//-----------------------------------------------------------------------------------------------------------------//
//Funciones

function agregar_reserva(nombre_sala, estado, dia, horario_inicio, horario_termino, color_sala)
{
	var reserva = canvas.append("g").attr("class", "reserva_grilla");
	
	var alto = (hora2minutos(horario_termino) - hora2minutos(horario_inicio))/7200*7*height;
	var inicio = (hora2minutos(horario_inicio) - 600)/7200*7*height + height*(1 + 14/3)/20;
	
	reserva.append("rect")
				.attr("fill", color_sala)
				.attr("height", alto)
				.attr("width", width/7)
				.attr("x", (2*dia - 0.95) * width/12)
				.attr("y", inicio);
	
	var texto_titulo = nombre_sala + " " + entero2string(horario_inicio.hora,2) + ":" + entero2string(horario_inicio.minuto,2) + " - " + entero2string(horario_termino.hora,2) + ":" + entero2string(horario_termino.minuto,2);
	
	reserva.append("text")
				.attr("x", (2*dia - 0.92) * width/12)
				.attr("y", inicio+height/80)
				.text(texto_titulo);
				
	reserva.append("text")
				.attr("x", (2*dia - 0.92) * width/12)
				.attr("y", inicio+height*5/80)
				.text(estado);
}

function hora2minutos(hora)
{
	return hora.hora*60 + hora.minuto;
}

function entero2string(val, numero_caracteres)
{
	if(numero_caracteres == 1)
		return (val%10).toString();
	else
		return entero2string(parseInt(val/10), numero_caracteres - 1) + (val%10).toString();
}

//------------------------------------------------------------------------------------------------------------------------//
