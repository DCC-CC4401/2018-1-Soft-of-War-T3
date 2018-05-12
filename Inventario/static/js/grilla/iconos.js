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