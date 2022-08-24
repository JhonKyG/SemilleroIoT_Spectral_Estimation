# Implementacion de una metodologia para la adquisicion des señales GNSS bajo condiciones ruidosas utlizando metodos de estimacion espectral no convencionales bajo el paradigma de Radio Definida por Software

En este trabajo, se presenta una metodología que permite un estudio de evaluación del rendimiento de diferentes técnicas de estimación espectral para la detección del espectro con el fin de detectar señales GPS débiles transmitidas en condiciones de alto ruido. Tradicionalmente, se ha utilizado la Transformada Rápida de Fourier como mecanismo para realizar operaciones de correlación en el dominio de la frecuencia para la adquisición de señales GNSS. Sin embargo, la implementación de técnicas no convencionales aumenta la capacidad de detección en entornos de baja SNR (Relación señal-ruido).

Se implementó un receptor de señales GPS en MATLAB para el estudio comparativo de técnicas de estimación espectral no convencionales, como Burg, Yule-Walker y Correlograma, con el fin de detectar señales GNSS reales en condiciones de mayor ruido. Mediante el uso del software receptor de señales GNSS de código abierto GNSS-SDR para grabar señales GPS, luego, el procesamiento de la señal GPS y las pruebas con los distintos métodos de estimación espectral se realizó con el programa SoftGNSS v3.0 codificado en MATLAB, así como plataformas de hardware de diferentes costos, con los cuales se lograron conseguir distintos tipos de resultados y desempeños con señales reales. Adicionalmente, también se implementó en GNU-Radio un barrido de frecuencia con el cual en un trabajo futuro se espera complementar más a fondo la investigación de señales GNSS y su adquisición.

Esta documentación se divide de la siguiente forma:

1. [Hardware utilizado](#Hardwareutilizado)
2. [Instalacion](#Instalacion)

## 1. Hardware utilizado <a name="Hardwareutilizado"></a>

* Antena GPS:

Las antenas GPS permiten la aplicación de sistemas de navegación por satélite (GNSS) permitiendo un rastreo y localizacion de la ubicacion de cualquier objeto que se encuentre en el rango de los satélites. Estas antenas captan las señales de banda L transmitidas del espacio y las transfieren a una unidad de procesamiento para determinar la ubicación de los respectivos receptores.

* HackRF One:

Dispositivo auxiliar e independiente utilizado por SDR para transmitir o recibir señales de radio desde 1 MHZ hasta 6 GHZ. Diseñado para facilitar el desarrollo de las tecnologías de la comunicación tanto actuales como en el desarrollo de las nuevas generaciones de tecnologías de radio junto con sus correspondientes protocolos de comunicación.

* Nooelec Tiny TCX0: 

Complemento de 10 MHz para HackRF, este mide 0,58” x 0,4”. Tiene la capacidad establecer un ruido de fase ultra bajo y una estabilidad de frecuencia en casi cualquier condicion. Este es un excelente complemento para realizar experimentaciones con alta precision con el HackRF en cuanto a proyectos relaciones con el GPS

## 2. Instalación <a name="Instalacion"></a>

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

 
