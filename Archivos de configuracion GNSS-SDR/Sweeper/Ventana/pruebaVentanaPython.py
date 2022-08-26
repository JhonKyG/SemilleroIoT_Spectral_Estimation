###################################################################
#############       Universidad Sergio Arboleda       #############
#############              Semillero IoT              #############
#############       Felipe Osorio - Jhon Garcia       #############
###################################################################


###################################################################
# Modulos utilizados
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

###################################################################
# Entorno

ventana = Tk() # Creando Objeto de tkinder
ventana.title("Ingreso de Datos") #Cambiar el nombre de la ventana
ventana.geometry("450x170") #Configurar tamaño
#mi_Frame = Frame(ventana, wigth=500, height=300)
#mi_Frame.pack()
#ventana.iconbitmap("LogoSergioArboleda.png") #Cambiar el icono
ventana.config(bg="darkblue") #Cambiar color de fondo

###################################################################
# Contenido

image = Image.open("Ventana/LogoSergioArboleda.png")
resize_image = image.resize((50, 30))
img = ImageTk.PhotoImage(resize_image)
logo = Label(ventana, image=img)
logo.config(bg="darkblue") #Cambiar color de fondo
logo.place(x=60, y=10)


# Titulo

titulo = Label(ventana,text="Universidad Sergio Arboleda")
titulo.place(x=120, y=13)
titulo.config(bg="darkblue") #Cambiar color de fondo
titulo.config(fg="white") #Cambiar color del texto
titulo.config(font=('Arial', 15)) #Cambiar tipo y tamaño de fuente

# Frecuencia Inicial

LabelFreqI = Label(ventana,text="Frecuencia Inicial (Hz):")
LabelFreqI.place(x=10, y=60)
LabelFreqI.config(bg="darkblue") #Cambiar color de fondo
LabelFreqI.config(fg="white") #Cambiar color del texto
LabelFreqI.config(font=('Arial', 10)) #Cambiar tipo y tamaño de fuente

LabelFreqF = Label(ventana,text="Frecuencia Final (Hz):")
LabelFreqF.place(x=10, y=90)
LabelFreqF.config(bg="darkblue") #Cambiar color de fondo
LabelFreqF.config(fg="white") #Cambiar color del texto
LabelFreqF.config(font=('Arial', 10)) #Cambiar tipo y tamaño de fuente

LabelStep = Label(ventana,text="Step (Hz):")
LabelStep.place(x=10, y=120)
LabelStep.config(bg="darkblue") #Cambiar color de fondo
LabelStep.config(fg="white") #Cambiar color del texto
LabelStep.config(font=('Arial', 10)) #Cambiar tipo y tamaño de fuente

###################################################################
# Ingreso de datos

# Entrada de datos
freqI = ttk.Entry(ventana, textvariable="88e6", width=5)
freqI.place(x=150, y=60)

freqF = ttk.Entry(ventana, textvariable="108e6", width=5)
freqF.place(x=150, y=90)

step = ttk.Entry(ventana, textvariable="1e5", width=5)
step.place(x=150, y=120)

# Llenado de valores por defecto

#freqF.set("88e6"); freqI.set("108e6"); step.set("1e5")

###################################################################
# Boton de ejecución 

button = ttk.Button(text="Guardar y Ejecutar", command=lambda: ModificarArchivo())
button.place(x=220, y=60) 

print("Ejecutando...")

###################################################################

#def ModificarArchivo():
# print("\n -> Frecuencia Inicial: ", freqI.get(), 
# "\n -> Frecuencia Final: ", freqF.get(), 
# "\n -> Step: ", step.get(), "\n")

# fr=open('Ventana/TempGNURadio.txt','r') 
# codigo = fr.read()

 
# fw=open('Ventana/CodigoGNU.py','w')
# fw.write("var = {'f1':"+str(freqI.get())+", 'f2':"+str(freqF.get())+", 'step':"+str(step.get())+"}")
# fw.write(codigo)
# fw.close()
# fr.close() 
 
 #f = open ('TempGNURadio.py','w')
 #f.write('hola mundo')
 #f.close()

# Creando ventana emergente
#ventana.mainloop()
