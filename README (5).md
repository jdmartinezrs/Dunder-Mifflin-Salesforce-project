
# Dunder Mifflin Salesforce-project

Por favor realizar el siguiente caso de estudio, unido a un informe sobre cómo realizo su implementación en Salesforce ORG:


En Salesforce , debes crear los siguientes objetos personalizados:
Nombre de la Empresa (Texto)
Tipo de Cliente (Picklist: [Pequeña Empresa, Mediana Empresa, Corporativo, Gobierno])
Ubicación (Texto)
Ejecutivo de Cuenta (Lookup a "Empleado")
Volumen de Compra Mensual ($) (Moneda)
Nombre del Producto (Texto)
Categoría (Picklist: [Papel, Carpetas, Esferos, Toners, Material de Oficina])
Precio Unitario ($) (Moneda)
Stock Disponible (Número)
Proveedor (Texto)
Número de Pedido (Auto Number)
Cliente (Lookup a "Cliente")
Fecha del Pedido (Fecha)
Monto Total ($) (Moneda)
Estado del Pedido (Picklist: [Pendiente, Procesado, Enviado, Entregado, Cancelado])
Ejecutivo Responsable (Lookup a "Empleado")
Nombre del Empleado (Texto)
Cargo (Picklist: [Ejecutivo de Ventas, Gerente, Soporte, Contabilidad])
Sucursal (Picklist: [Scranton, Utica, Nashua, Stamford])
Teléfono (Texto)
Descarga los siguientes archivos CSV para importar a :
✅ → Contiene 2000 registros de empresas clientes con información de compras mensuales.
⚠️ → Contiene 5000 registros con errores en fechas, estados mal escritos y valores vacíos.
⚠️ → Contiene 300 registros con precios en diferentes formatos y stock incorrecto.


Antes de importar los datos erróneos, debes la información.
📌
✅ Convierte todas las fechas al formato YYYY-MM-DD.
✅ Corrige estados mal escritos (Pendientee → Pendiente, Entregadoo → Entregado).
✅ Reemplaza valores vacíos en "Monto Total" con $50.00 por defecto.
✅ Estandariza los precios a formato numérico ($10.00, 10.00, 10,00 → 10.00).
✅ Corrige valores negativos de stock reemplazándolos por 0.
✅ Elimina duplicados basados en "Nombre del Producto" y "Proveedor".

Dunder Mifflin necesita tomar mejores decisiones basadas en datos. → Lista de los clientes más grandes según monto total de compra. → Todos los pedidos que aún no han sido entregados. → Análisis de ventas por mes y ubicación. → Lista de productos con stock menor a 10 unidades. → Ranking de productos con más ventas en el último trimestre. → Ventas generadas por cada empleado. → Comparación de ingresos entre las oficinas de Scranton, Utica, Nashua y Stamford.
📌 Genera cada uno de estos reportes y captura los resultados.
📈
🔹 → Gráfico de barras.
🔹 → Gráfico de pastel.
🔹 → Gráfico de embudo.
🔹 → Línea de tendencia.
📌 Personaliza el dashboard con filtros por fechas y empleados. → Cuando un pedido cambia a "Entregado", se envía un email automático al cliente. → Si un cliente ha comprado más de $10,000 en el último trimestre, recibe un 10% de descuento en su próximo pedido. → Si un producto tiene menos de 5 unidades en stock, se notifica automáticamente al equipo de compras.
📌 Implementa estos Flows y prueba su funcionamiento.
Responde las siguientes preguntas:¿Cuáles fueron los mayores desafíos en la limpieza de datos?¿Cómo mejoraron los reportes la toma de decisiones en Dunder Mifflin?¿Cómo automatizarías más procesos para reducir errores humanos?


![Logo](https://i.pinimg.com/1200x/67/86/f9/6786f97adcc99b077454dd46c587f05b.jpg)


## Dunder Mifflin necesita tomar mejores decisiones basadas en datos.



→ Lista de los clientes más grandes según monto total de compra. 

![Logo](https://i.pinimg.com/1200x/05/1b/75/051b758df4593e0619a54ad0103e1f37.jpg)
Filtro de tipo Row Limit, para vizualizar solo las 10 primeras filas

![Logo](https://i.pinimg.com/1200x/07/77/3b/07773bf0694c3f5c477bcb73ac11e640.jpg)

Resultado de el reporte 
![Logo](https://i.pinimg.com/1200x/42/c4/c4/42c4c47b855a8ebd75968b0dd732fdde.jpg)

→ Todos los pedidos que aún no han sido entregados. 

![Logo](https://i.pinimg.com/1200x/42/c4/c4/42c4c47b855a8ebd75968b0dd732fdde.jpg)

→ Análisis de ventas por mes y ubicación.
![Logo](https://i.pinimg.com/1200x/f2/b0/62/f2b062848b80772f4c71df061d82184f.jpg)

