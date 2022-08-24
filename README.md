# Implementacion de una metodologia para la adquisicion des señales GNSS bajo condiciones ruidosas utlizando metodos de estimacion espectral no convencionales bajo el paradigma de Radio Definida por Software

En este trabajo, se presenta una metodologia que permite un estudio de evaluacion del rendimiento
de diferentes tecnicas de estimacion espectral para la deteccion del espectro con el fin de detectar
señales GPS debiles transmitidas en condiciones de alto ruido. Tradicionalmente, se ha utilizado la Transformada Rapida de Fourier como mecanismo para realizar operaciones de correlacion en el dominio de la frecuencia para la adquisicion de se ̃nales GNSS. Sin embargo, la implementacion de tecnicas no convencionales aumenta la capacidad de deteccion en entornos de baja SNR (Relacion señal-ruido).

Se implemento un receptor de señales GPS en MATLAB para el estudio comparativo de tecnicas de estimacion espectral no convencionales, como Burg, Yule-Walker y Correlograma, con el fin de detectar señales GNSS reales en condiciones de mayor ruido. Mediante el uso del software receptor de señales GNSS de codigo abierto GNSS-SDR para grabar señales GPS, luego, el procesamiento de la señal GPS y las pruebas con los distintos metodos de estimacion espectral se realizo con el programa SoftGNSS v3.0 codificado en MATLAB, asi como plataformas de hardware de diferentes costos, con los cuales se lograron conseguir distintos tipos de resultados y desempeños con señales reales. Adicionalmente, tambien se implemento en GNU-Radio un barrido de frecuencia con el cual en un trabajo futuro se espera complementar mas a fondo la investigacion de señales GNSS y su adquisicion.


Esta documentacion se divide de la siguiente forma:

1. Instalacion

## 1. Instalacion

### Instalación del GNSS-SDR  y  GNU Radio 

Tanto el software del GNSS-SDR como el de GNU Radio se pueden instalar con el siguiente comando a partir del Sistema Operativo (SO) de Debian 9 o Ubuntu 16.04 Linux

``` 
$ sudo apt-get install gnss-sdr 
```

EL bloque Osmocom y bloque RTL-SDR no estan instalados por defecto en el GNU Radio, el proceso para instalarlos es el siguiente en la terminal de Linux

``` 
$ sudo apt-get install libportaudio2
$ sudo apt-get install git-core
$ sudo apt-get install gnuradio gr-somosdr
```

### Instalación de Matlab

Este software es compatible tanto para el sistema operativo de Linux y Windows, este se puede descargar mediante el siguiente enlace [Descargar Matlab](https://login.mathworks.com/embedded-login/landing.html?cid=getmatlab&s_tid=gn_getml).
