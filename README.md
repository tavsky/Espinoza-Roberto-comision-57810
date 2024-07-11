# Espinoza-Roberto-comision-57810
Repositorio del proyecto final relacionado al curso python de comisión 57810 CoderHouse. 


  <h1>Dir-t Sauce - Sistema de Gestión de Ventas e Inventario</h1>

  <p>Dir-t Sauce es un sistema web desarrollado con Django que permite gestionar las ventas, el inventario, los clientes y el stock de un set de productos, en este caso, salsas. Con Dir-t Sauce, podrás realizar un seguimiento de las ventas, mantener actualizado el inventario, administrar la información de los clientes y gestionar el stock de las salsas de manera eficiente.</p>

  <h2>Información relevante</h2>
  <ul>
    <li>El usuario administrador es roberto y la clave es 1234.</li>
    <li>El modelo cuenta con 5 modelos que se mencionan a continuación</li>
     <ul>
        <li>IngresoStock: Este modelo busca definir las principales variables para gestionar el Stock, donde sus atributos son: SKU, Cantidad, nombre del encargado (quien registra el producto)y nombre del producto  </li>
        <li>Cliente: Este modelo busca consolidar la información relacionada a los clientes, donde sus atributos son: nombre, email, dirección y fecha de nacimiento</li>
        <li>Empleado: Este modelo busca consolidar la información relacionada a los empleados, donde sus atributos son: nombre, cargo (definido en 3 opciones cerradas)</li>
        <li>IngresoVenta: Este modelo busca definir las principales variables para gestionar las ventas, donde sus atributos son: SKU, Cantidad, nombre del encargado (quien registra el producto), precio y nombre del cliente  </li>
        <li>Avatar: Este modelo solamente se utiliza para la gestión de la imagen relacionada a cada usuario.</li>

<h2>Requisitos</h2>

  <ul>
    <li>Python 3.7 o superior</li>
    <li>Django 3.2.5 o superior</li>

<h2>Instalación</h2>

  <ol>
    <li>Clona o descarga el repositorio de Dir-t Sauce desde GitHub: <a href="https://github.com/tu-usuario/dir-t-sauce">https://github.com/tu-usuario/dir-t-sauce</a></li>
    <li>Crea un entorno virtual para el proyecto: <code>python -m venv env</code></li>
    <li>Activa el entorno virtual:
      <ul>
        <li>En Windows: <code>env\Scripts\activate</code></li>
        <li>En macOS y Linux: <code>source env/bin/activate</code></li>
      </ul>
    </li>
    <li>Instala las dependencias del proyecto: <code>pip install -r requirements.txt</code></li>
    <li>Realiza las migraciones de la base de datos: <code>python manage.py migrate</code></li>
    <li>Crea un superusuario para acceder al panel de administración: <code>python manage.py createsuperuser</code></li>
    <li>Inicia el servidor de desarrollo: <code>python manage.py runserver</code></li>
  </ol>

<h2>Uso</h2>

  <ol>
    <li>Explora las diferentes pestañas disponibles para gestionar las ventas, el inventario, los clientes y el stock de las salsas.</li>
    <li>En cada pestaña, encontrarás formularios para ingresar datos y también podrás visualizar la información almacenada en la base de datos.</li>
    <li>Utiliza el panel de administración de Django para realizar tareas adicionales de gestión, como la creación de usuarios y la modificación de configuraciones.</li>
  </ol>

