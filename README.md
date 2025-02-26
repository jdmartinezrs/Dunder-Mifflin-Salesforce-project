
# Dunder Mifflin Salesforce-project


![Logo](https://i.pinimg.com/1200x/67/86/f9/6786f97adcc99b077454dd46c587f05b.jpg)


##  Estructura de los Objetos

 **Cliente**

-  **Nombre de la Empresa** *(Texto)*
-  **Tipo de Cliente** *(Picklist: Pequeña Empresa, Mediana Empresa, Corporativo, Gobierno)*
-  **Ubicación** *(Texto)*
-  **Ejecutivo de Cuenta** *(Lookup → Empleado)*
-  **Volumen de Compra Mensual ($)** *(Moneda)*

 **Empleado**

-  **Nombre del Empleado** *(Texto)*
-  **Cargo** *(Picklist: Ejecutivo de Ventas, Gerente, Soporte, Contabilidad)*
-  **Sucursal** *(Picklist: Scranton, Utica, Nashua, Stamford)*
-  **Teléfono** *(Texto)*

  **Producto**

-  **Nombre del Producto** *(Texto)*
-  **Categoría** *(Picklist: Papel, Carpetas, Esferos, Toners, Material de Oficina)*
-  **Precio Unitario ($)** *(Moneda)*
-  **Stock Disponible** *(Número)*
-  **Proveedor** *(Texto)*

 **Pedido**

-  **Número de Pedido** *(Auto Number)*
-  **Cliente** *(Lookup → Cliente)*
-  **Fecha del Pedido** *(Fecha)*
-  **Monto Total ($)** *(Moneda)*
-  **Estado del Pedido** *(Picklist: Pendiente, Procesado, Enviado, Entregado, Cancelado)*
-  **Ejecutivo Responsable** *(Lookup → Empleado)*
-  **Productos Comprados** *(Lookup → Producto o relación de muchos a muchos con un objeto intermedio)*

## Dunder Mifflin necesita tomar mejores decisiones basadas en datos.


→ Lista de los clientes más grandes según monto total de compra. 

![Logo](
https://i.pinimg.com/1200x/5e/6b/d2/5e6bd2a62edf979f9a6e70b678c15090.jpg)


→ Todos los pedidos que aún no han sido entregados. 

![Logo](https://i.pinimg.com/1200x/11/07/5f/11075fef1ee72b750c5ca45472acc8ea.jpg)

→ Análisis de ventas por mes y ubicación.
![Logo](https://i.pinimg.com/1200x/71/ce/17/71ce17ac2dca0f2ed279b7bd3ecd1de6.jpg)

→ Lista de productos con stock menor a 10 unidades.

![Logo](https://i.pinimg.com/1200x/bc/21/2b/bc212b399858ca3fd4c8b973074b4fa4.jpg)

→ Ranking de productos con más ventas en el último trimestre.
![Logo](https://i.pinimg.com/1200x/c1/1e/d3/c11ed33d2a5aa7f611e3f363543a6f73.jpg)

→ Ventas generadas por cada empleado.
![Logo](https://i.pinimg.com/1200x/7a/66/bd/7a66bdb208a70639c739fe0cb6bd12b5.jpg)

 → Comparación de ingresos entre las oficinas de Scranton, Utica, Nashua y Stamford.
![Logo](https://i.pinimg.com/1200x/e6/4d/08/e64d08e7882e58728467377fe5cdd4c2.jpg)

## Personaliza el dashboard con filtros por fechas y empleados.

→ Filtro por fecha "between 6/10/2024-2/27/2025
![Logo](https://i.pinimg.com/1200x/4b/4a/36/4b4a365b07df00656ee0a770c2a023fd.jpg)

![Logo](https://i.pinimg.com/1200x/19/5c/3e/195c3ec79fc1bf45125237ba7aeea69f.jpg)

→ Filtro por empleado "a02aj000008MD5H"
![Logo](https://i.pinimg.com/1200x/2b/d2/57/2bd25716c281a9420a801d5589f7fdde.jpg)
![Logo](https://i.pinimg.com/1200x/70/c1/e8/70c1e8ea00967d0724c65db8943826ec.jpg)

## Flows
→ Cuando un pedido cambia a "Entregado", se envía un email automático al cliente

![Logo](https://i.pinimg.com/1200x/63/1f/cc/631fcc3f2a9eaec5d1815afccfc94434.jpg)

→ Si un cliente ha comprado más de $10,000 en el último trimestre, recibe un 10% de descuento en su próximo pedido.

![Logo](https://i.pinimg.com/736x/28/dc/1b/28dc1b22a04502e132f378122c173523.jpg)

→ Si un producto tiene menos de 5 unidades en stock, se notifica automáticamente al equipo de compras.

![Logo](https://i.pinimg.com/1200x/59/5a/e5/595ae51de38cca88b739d303de49170e.jpg)

## Peguntas

**¿Cuáles fueron los mayores desafíos en la limpieza de datos?**

El principal desafío fue ajustar el volumen de datos a la capacidad del storage de la versión gratuita de Salesforce. Por lo tanto, tuve que idear una estrategia para reducir los datos de manera que pudieran ser cargados en Salesforce sin perder las relaciones entre ellos ni dejar datos incompletos

Se leen cuatro archivos CSV:

clientes_filtrados.csv
pedidos_filtrados.csv
EMPLEADOS.csv
PRODUCTOS.csv

**Empleados:**

Se identifican los empleados que están referenciados en la lista de clientes y pedidos.
Solo se conservan esos empleados.
Se reduce el número de empleados en un 25%, seleccionando aleatoriamente el 75% (frac=0.75).


```python
empleados_referenciados = set(df_clientes["Ejecutivo de Cuenta"]).union(set(df_pedidos["Ejecutivo Responsable"]))
df_empleados = df_empleados[df_empleados["Nombre del Empleado"].isin(empleados_referenciados)]

df_empleados = df_empleados.sample(frac=0.75, random_state=42)
```
**clientes:**

Se eliminan los clientes cuyo Ejecutivo de Cuenta no esté en la lista filtrada de empleados.
Se reduce la cantidad de clientes en un 15% (frac=0.85).

```python
df_clientes = df_clientes[df_clientes["Ejecutivo de Cuenta"].isin(df_empleados["Nombre del Empleado"])]
df_clientes = df_clientes.sample(frac=0.85, random_state=42)
```
**pedidos:**

Se eliminan los pedidos cuyos clientes o ejecutivos no sean válidos.
Se reduce el número de pedidos en un 20% (frac=0.8).

```python
df_pedidos = df_pedidos[df_pedidos["Cliente"].isin(df_clientes["Nombre de la Empresa"]) & 
                        df_pedidos["Ejecutivo Responsable"].isin(df_empleados["Nombre del Empleado"])]

df_pedidos = df_pedidos.sample(frac=0.8, random_state=42)
```
**productos:**

Se extraen los productos comprados en los pedidos.
Solo se conservan esos productos en df_productos.
Se reduce la cantidad de productos en un 17% (frac=0.83).

```python
productos_referenciados = set(df_pedidos["Producto Comprado"].str.split(", ").explode())
df_productos = df_productos[df_productos["Nombre del Producto"].isin(productos_referenciados)]

df_productos = df_productos.sample(frac=0.83, random_state=42)
```
**¿Cómo mejoraron los reportes la toma de decisiones en Dunder Mifflin?**

Los reportes mejoraron la toma de decisiones en Dunder Mifflin al permitir consultas especializadas que proporcionan información detallada y relevante sobre diversas áreas de la empresa. A través de estos reportes, es posible consultar el estado de los pedidos, identificar los productos más comprados, analizar el rendimiento de cada empleado y realizar balances financieros entre las distintas sucursales. Esto facilita la identificación de oportunidades de mejora, optimización de recursos y toma de decisiones informadas, contribuyendo a una gestión más eficiente y efectiva en todos los niveles de la compañía.

Estar informado sobre el stock de los productos es crucial para una gestión eficiente en Dunder Mifflin. Los reportes permiten monitorear en tiempo real la disponibilidad de inventario, lo que facilita la toma de decisiones sobre reabastecimiento y optimización de los recursos. Esto no solo asegura que siempre haya suficiente stock para satisfacer la demanda de los clientes, sino que también permite identificar productos de bajo rendimiento y ajustar las estrategias de ventas o producción, evitando sobrestock o desabastecimiento. Esta información contribuye a una mejor planificación y mejora la capacidad de respuesta ante cambios en las necesidades del mercado.

**¿Cómo automatizarías más procesos para reducir errores humanos?**

Para automatizar más procesos y reducir errores humanos, lo primero sería analizar los reportes y detectar las tareas repetitivas o aquellas que son propensas a errores. A través de un análisis detallado de los flujos de trabajo, se pueden identificar actividades que, si se automatizan, mejorarían la eficiencia y disminuirían la probabilidad de fallos. Esto puede incluir tareas como la actualización de inventarios, la asignación de pedidos.

Una vez identificadas estas oportunidades, se pueden utilizar flujos de trabajo automatizados, Estos sistemas pueden realizar tareas como el procesamiento de pedidos, la actualización de stock y la creación de informes financieros sin intervención manual, lo que asegura una mayor precisión y consistencia en los resultados. Al automatizar estos procesos, no solo se ahorra tiempo, sino que también se mejora la calidad de la información, optimizando la toma de decisiones y permitiendo a los empleados enfocarse en actividades de mayor valor estratégico.