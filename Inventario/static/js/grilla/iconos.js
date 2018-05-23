function triangulo_derecha(d3_component, cx, cy, color, triangle_radious)
{
	triangle_angle = 0;
	d3_component.append("path")
				.attr("d", "M " + (cx + (triangle_radious * Math.cos(Math.PI*4/3 + triangle_angle))) + " " + (cy + (triangle_radious * Math.sin(Math.PI*4/3 + triangle_angle))) + " L " + (cx + (triangle_radious * Math.cos(triangle_angle))) + " " + (cy + (triangle_radious * Math.sin(triangle_angle))) + " L " + (cx + (triangle_radious * Math.cos(Math.PI*2/3 + triangle_angle))) + " " + (cy + (triangle_radious * Math.sin(Math.PI*2/3 + triangle_angle))) + " L " + (cx + (triangle_radious * Math.cos(Math.PI*4/3 + triangle_angle))) + " " + (cy + (triangle_radious * Math.sin(Math.PI*4/3 + triangle_angle))) )
				.attr("fill", color);
}

function triangulo_izquierda(d3_component, cx, cy, color, triangle_radious)
{
	triangle_angle = Math.PI;
	d3_component.append("path")
				.attr("d", "M " + (cx + (triangle_radious * Math.cos(Math.PI*4/3 + triangle_angle))) + " " + (cy + (triangle_radious * Math.sin(Math.PI*4/3 + triangle_angle))) + " L " + (cx + (triangle_radious * Math.cos(triangle_angle))) + " " + (cy + (triangle_radious * Math.sin(triangle_angle))) + " L " + (cx + (triangle_radious * Math.cos(Math.PI*2/3 + triangle_angle))) + " " + (cy + (triangle_radious * Math.sin(Math.PI*2/3 + triangle_angle))) + " L " + (cx + (triangle_radious * Math.cos(Math.PI*4/3 + triangle_angle))) + " " + (cy + (triangle_radious * Math.sin(Math.PI*4/3 + triangle_angle))) )
				.attr("fill", color);
}

function doble_triangulo_derecha(d3_component, cx, cy, color, triangle_radious)
{
	triangulo_derecha(d3_component, cx-triangle_radious/4, cy, color, triangle_radious);
	triangulo_derecha(d3_component, cx+triangle_radious/4, cy, color, triangle_radious);
}

function doble_triangulo_izquierda(d3_component, cx, cy, color, triangle_radious)
{
	triangulo_izquierda(d3_component, cx-triangle_radious/4, cy, color, triangle_radious);
	triangulo_izquierda(d3_component, cx+triangle_radious/4, cy, color, triangle_radious);
}

function anillo(d3_component, cx, cy, color, inRadious, outRadious)
{
	var group = d3_component.append("g")
								.attr("transform", "translate(" + cx.toString() +  "," + cy.toString() +  ")");
	var arc = d3.svg.arc()
					.innerRadius(inRadious)
					.outerRadius(outRadious)
					.startAngle(0);
					
	group.append("path")
			.datum({endAngle: 2*Math.PI})
			.style("fill", color)
			.attr("d", arc);
			
	return group;
}

function tick(d3_component, cx, cy, color, radious)
{
	var group = d3_component.append("g");
	
	y_linea1 = cy + radious*5/8;
	x_linea1 = cx - radious/2;
	
	group.append("line")
		.attr("y1", y_linea1 - radious/4)
		.attr("y2", y_linea1 - radious)
		.attr("x1", x_linea1 + radious/4)
		.attr("x2", x_linea1 + radious)
		.attr("stroke", color)
		.attr("stroke-width", 2);
		
	group.append("line")
		.attr("y1", y_linea1 - radious/4)
		.attr("y2", y_linea1 - radious/2)
		.attr("x1", x_linea1 + radious/4)
		.attr("x2", x_linea1)
		.attr("stroke", color)
		.attr("stroke-width", 2);
		
	return group;
}