# Implementacion de una metodologia para la adquisicion de señales GNSS bajo condiciones ruidosas utlizando metodos de estimacion espectral no convencionales bajo el paradigma de Radio Definida por Software

En este trabajo, se presenta una metodología que permite un estudio de evaluación del rendimiento de diferentes técnicas de estimación espectral para la detección del espectro con el fin de detectar señales GPS débiles transmitidas en condiciones de alto ruido. Tradicionalmente, se ha utilizado la Transformada Rápida de Fourier como mecanismo para realizar operaciones de correlación en el dominio de la frecuencia para la adquisición de señales GNSS. Sin embargo, la implementación de técnicas no convencionales aumenta la capacidad de detección en entornos de baja SNR (Relación señal-ruido).

Se implementó un receptor de señales GPS en MATLAB para el estudio comparativo de técnicas de estimación espectral no convencionales, como Burg, Yule-Walker y Correlograma, con el fin de detectar señales GNSS reales en condiciones de mayor ruido. Mediante el uso del software receptor de señales GNSS de código abierto GNSS-SDR para grabar señales GPS, luego, el procesamiento de la señal GPS y las pruebas con los distintos métodos de estimación espectral se realizó con el programa SoftGNSS v3.0 codificado en MATLAB, así como plataformas de hardware de diferentes costos, con los cuales se lograron conseguir distintos tipos de resultados y desempeños con señales reales. Adicionalmente, también se implementó en GNU-Radio un barrido de frecuencia con el cual en un trabajo futuro se espera complementar más a fondo la investigación de señales GNSS y su adquisición.

# Archivos del repositorio:

* ## Archivos de configuracion GNSS-SDR:

  En este apartado se presenta el código utilizado en el HardWare (HackRF y RTL-SDR) para obtener las coordenadas GPS en la terminal del sistema operativo Linux. Para hacer uso de estos comandos se es necesario tener el archivo de texto previamente descargado, abrir la terminal desde la ubicación en la que se guardo, e ingresar el siguiente comando: ``` gnss-sdr --config_file=./nombre_del_archivo.conf ```. 
  
  El tiempo de ejecución para obtener las coordenadas de la ubicación actual dependerá en gran medida del sitio en el que se encuentre puesto que al estar en un lugar cerrado el ruido de los objetos e inclusive la cantidad de nubes que se presenta en el cielo atenuara la señal GPS hasta el punto de llegar a tener un tiempo completamente indefinido.

# Requerimiento:

Esta documentación se divide de la siguiente forma:

1. [Hardware](#Hardwareutilizado)
2. [Instalacion de software](#Instalacion)
3. [Puesta a punto y uso de GNSS-SDR](#GNSS_SDR)
4. [Procesamiento de la señal en MATLAB](#Matlab)
5. [Barrido de frecuencia en GNU Radio](#GNU_Radio)

## 1. Hardware <a name="Hardwareutilizado"></a>

* Antena GPS:

Las antenas GPS permiten la aplicación de sistemas de navegación por satélite (GNSS) permitiendo un rastreo y localizacion de la ubicacion de cualquier objeto que se encuentre en el rango de los satélites. Estas antenas captan las señales de banda L transmitidas del espacio y las transfieren a una unidad de procesamiento para determinar la ubicación de los respectivos receptores.

* HackRF One:

Dispositivo auxiliar e independiente utilizado por SDR para transmitir o recibir señales de radio desde 1 MHZ hasta 6 GHZ. Diseñado para facilitar el desarrollo de las tecnologías de la comunicación tanto actuales como en el desarrollo de las nuevas generaciones de tecnologías de radio junto con sus correspondientes protocolos de comunicación.

* Nooelec Tiny TCX0: 

Complemento de 10 MHz para HackRF, este mide 0,58” x 0,4”. Tiene la capacidad establecer un ruido de fase ultra bajo y una estabilidad de frecuencia en casi cualquier condicion. Este es un excelente complemento para realizar experimentaciones con alta precision con el HackRF en cuanto a proyectos relaciones con el GPS

## 2. Instalación de software <a name="Instalacion"></a>

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

## 3. Puesta a punto y uso de GNSS-SDR <a name="GNSS_SDR"></a>

Una vez instalado GNSS-SDR es necesario el uso de archivos de configuraciòn para correr GNSS-SDR. Los archivos de configuracion y la documentacion se pueden encontrar en la pagina oficial de [GNSS-SDR](https://gnss-sdr.org/docs/overview/). En este repositorio se pueden encontrar archivos de configuracion de GNSS-SDR para los dispositivos RTL-SDR, HackRF One y Ettus USRP B210.

En una terminal se procede a insertar el siguiente comando ```$ gnss-sdr --config_file=./nombreArchivo.conf```. Cabe acalarar que la terminal debe estar direccionada a la carpeta donde se encuentre el archivo de configuracion. 

Cuando se ejecute el comando debe verse algo parecido a esto: 
```
$ gnss-sdr --config_file=./nombreArchivo.conf
Initializing GNSS-SDR v0.0.17 ... Please wait.
Logging will be done at "/tmp"
Use gnss-sdr --log_dir=/path/to/log to change that.
-- X300 initialization sequence...
-- Determining maximum frame size... 8000 bytes.
-- Setup basic communication...
-- Loading values from EEPROM...
-- Setup RF frontend clocking...
-- Radio 1x clock:200
-- Initialize Radio0 control...
-- Performing register loopback test... pass
-- Initialize Radio1 control...
-- Performing register loopback test... pass
Sampling Rate for the USRP device: 4000000.000000 [sps]...
UHD RF CHANNEL #0 SETTINGS
Actual USRP center freq.: 1575420000.010133 [Hz]...
PLL Frequency tune error 0.010133 [Hz]...
Actual daughterboard gain set to: 37.500000 dB...
Setting RF bandpass filter bandwidth to: 2000000.000000 [Hz]...
Check for front-end LO: locked ... is Locked
Using Volk machine: avx2_64_mmx
Starting a TCP Server on port 2101
The TCP Server is up and running. Accepting connections ...
Current input signal time = 49 [s]
Current input signal time = 50 [s]
Current input signal time = 51 [s]
Current input signal time = 52 [s]
NAV Message: received subframe 1 from satellite GPS PRN 27 (Block IIF)
NAV Message: received subframe 1 from satellite GPS PRN 10 (Block IIF)
NAV Message: received subframe 1 from satellite GPS PRN 08 (Block IIF)
NAV Message: received subframe 1 from satellite GPS PRN 16 (Block IIR)
NAV Message: received subframe 1 from satellite GPS PRN 18 (Block IIR)
```

Con algo mas de un minuto de ejecucion seria suficiente para que GNSS-SDR arroje resultados de navegacion.

```
Position at 2016-Aug-11 14:23:19 UTC is Lat = 41.2751 [deg], Long = 1.98765 [deg], Height= 68.9893 [m]
Position at 2016-Aug-11 14:23:19 UTC is Lat = 41.2751 [deg], Long = 1.98765 [deg], Height= 72.1068 [m]
Current input signal time = 66 [s]
Position at 2016-Aug-11 14:23:20 UTC is Lat = 41.2751 [deg], Long = 1.9877 [deg], Height= 67.0216 [m]
Position at 2016-Aug-11 14:23:20 UTC is Lat = 41.2751 [deg], Long = 1.9877 [deg], Height= 84.7445 [m]
Current input signal time = 67 [s]
Position at 2016-Aug-11 14:23:21 UTC is Lat = 41.2751 [deg], Long = 1.98771 [deg], Height= 70.0031 [m]
Position at 2016-Aug-11 14:23:21 UTC is Lat = 41.2751 [deg], Long = 1.98767 [deg], Height= 63.1242 [m]
Current input signal time = 68 [s]
```
Y ya esta, tenemos posicionamiento en tiempo real.

Los archivos de configuracion proporcionados en este repositorio estan parametrizados para funcionar y detectar solamente señales GPS en banda L1 (1575.42Mhz). Ademas, los archivos de configuracion tambien tienen habilita la opcion de grabado de la señal, es decir que se genera un archivo con extencion **.dat**,lo cual es util para el proximo paso en MATLAB.

## 4. Procesamiento de la señal en MATLAB. <a name="Matlab"></a>

Descargamos el codigo fuente de SoftGNSS desde este repositorio. Si no tenias MATLAB previamente instalado es necesario la instalacion de **pwelch**, es posible encontrarla en la seccion de instalacion de plugins de MATLAB.

Despues de la ejecucion de GNSS-SDR veremos en la carpeta donde esta el archivo de configuracion un fichero con extencion **.dat**, copiamos la ruta del fichero y la pegamos en el archivo ## Pendiente tal y como se muestra en la siguiente imagen.

Ejecutamos el archivo **init.m**, veremos algo parecido a:
## Imagenes de ejecucion

Si se tienen grabaciones de señales GPS de otras fuentes distintas a GNSS-SDR y se quieren procesar en MATLAB, es posible que necesitemos hacer un leve cambio de parametros en el archivo ## Pendiente, 
## Imagen aqui
las modificaciones mas comunes son:

El proposito de usar MATLAB para procesar señales GPS tiene como fin facilitar la implementacion de metodos de estimacion espectral no convencionales, ya que vienen incluidos como funciones de MATLAB.

## 5. Barrido de frecuencia en GNU Radio. <a name="GNU_Radio"></a>

Se debe descargar todos los archivos de la siguiente carpeta: [Barrido GNU](https://github.com/JhonKyG/SemilleroIoT_Spectral_Estimation/tree/production/Archivos%20de%20configuracion%20GNSS-SDR/Sweeper%20RF). En esta carpeta se encuentran:

* **__pycache__**: Carpeta de archivos generado por GNU Radio tras su ejecución

* **GrabadoSweeper.grc**: Archivo de GNU Radio que contiene todos los bloques necesarios para llevar a cabo la ejecución del barrido junto con las conexiones que tiene cada bloque, es decir, toda la parte que el usuario puede ver y modificar.

* **PruebasSweeper.py**: En esta carpeta se encuentra el ejecutable del archivo .grc, este archivo de python se encarga de procesar las configuraciones puestas en pantalla por el usuario y de igual forma llama e importa otras carpetas necesarias para llevar a cabo su respectivo funcionamiento.

* **epy_module_0.py**: Este archivo contiene las funciones necesarias para modificar la frecuencia en el lenguaje de Python.





 
