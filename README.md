En la carpeta de Pruebas-Pasos, se muestra como se debe de operar los programas. a continuas una descripcion escrita de como ocuparlos
1.- Revisar que las 2 maquinas estan conectadas a la misma subred y que hay conexion entre ellas y que tienen la misma salida del router con ip route | grep default
2.- Revisar las ips de cada una de las maquinas para saber a que maquina se va a atacar y cual es la que atacara
3.- Iniciar primero el programa detectarARP.py con el comando sudo para que funcione correctamente, este se ejecuta en la maquina que sera atacada
4.- Ejecutar el programa ARPPoof.py con comando sudo para el correcto funcionamiento en la maquina que atacara
5.- Esperar a que el programa de la maquina atacada detecte el ARP.

Posibles problemas
Puede que el programa que detecta el detectarARP.py no optenga la MAC del router, si esto sucede solo se tiene que hacer un ping al 8.8.8.8, dejar que envie 2 a 4 paquetes y que sean exitosos, despues
comprobar la tabla arp y si en esta ya se carga la MAC del router volver a probar el programa
