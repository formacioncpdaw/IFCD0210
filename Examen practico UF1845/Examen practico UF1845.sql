Ejercicios SQL sobre la base de datos jardineria.

1. Obtener el nombre y precio de venta de todos los productos.

SELECT nombre, precio_venta
FROM producto;

2. Mostrar los clientes que pertenecen a España.

SELECT *
FROM cliente
WHERE pais = 'Spain';

3. Mostrar los productos ordenados por precio de venta de mayor a menor.

SELECT nombre, precio_venta
FROM producto
ORDER BY precio_venta DESC;

4. Mostrar el nombre del cliente y el código de los pedidos que ha realizado.

SELECT cliente.nombre_cliente, pedido.codigo_pedido
FROM cliente
JOIN pedido
ON cliente.codigo_cliente = pedido.codigo_cliente;

5. Mostrar el nombre del cliente, el código del pedido y el nombre del producto comprado.

SELECT cliente.nombre_cliente, pedido.codigo_pedido, producto.nombre
FROM cliente
JOIN pedido ON cliente.codigo_cliente = pedido.codigo_cliente
JOIN detalle_pedido ON pedido.codigo_pedido = detalle_pedido.codigo_pedido
JOIN producto ON detalle_pedido.codigo_producto = producto.codigo_producto;

6. Contar cuántos clientes hay registrados en la base de datos.

SELECT COUNT(*) AS total_clientes
FROM cliente;

7. Calcular el precio medio de venta de los productos.

SELECT AVG(precio_venta) AS precio_medio
FROM producto;

8. Mostrar cuántos productos hay en cada gama de productos.

SELECT gama, COUNT(*) AS cantidad_productos
FROM producto
GROUP BY gama;

9. Actualizar el teléfono del cliente con código 10 a '600123456'.

UPDATE cliente
SET telefono = '600123456'
WHERE codigo_cliente = 10;

10. Eliminar los pagos realizados antes del 1 de enero de 2005.

DELETE FROM pago
WHERE fecha_pago < '2005-01-01';
