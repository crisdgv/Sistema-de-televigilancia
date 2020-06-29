# Sistema-de-televigilancia
Proyecto 2 - Taller de Sistemas Embebidos

En el presente repositorio se presentan los archivos y directorios que configuran la imagen minima creada usando Yocto Project para una placa Raspberry Pi 3.

* En el directorio Python esta el codigo realizado para la deteccion de intrusiones humanas o animales y para la interfaz grafica.
* En el directorio Meta-Custom, como la capa personalizada creada, se encuentran las recetas creadas para aprender a usar el flujo de capas y recetas de Yocto Project y las que permiten la conexion remota, manejo de ventanas y visualizacion de un video, desde y con la placa que tiene una camara USB concectada.
Mediante un cable de red, la placa se conecta a internet y x11 mediante el protocolo ssh permite el control desde una computadora concetada a la red local. La imagen se instala en una memoria microSD y se inserta en la placa.

En Meta-custom/recipes-test/python-camtest_1.0.bb se encuentra la receta en la que se incluyen los archivos necesarios para la construccion de la imagen. En Meta-custom/recipes-test/python-camtest-1.0/python-camtest.py se encuentra el codigo necesario para el reconocimiento de humanos y animales, si embargo para la demostracion en el video part1 y part2 solo se uso el codigo para que abra la camara y se pueda ver la transmision en tiempo
