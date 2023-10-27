import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.constants import *
from ttkbootstrap.validation import add_regex_validation
from ttkbootstrap.tableview import Tableview
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(ttk.Frame):
    def __init__(self, master):
        self.master = master

        super().__init__(self.master)  # constructor de ventana

        self.ventana = master 
        self.colors = master.style.colors
        super().__init__(self.ventana,padding=(20,10))#constructor de ventana
        self.pack(fill=BOTH,expand=YES)
        self.costos_variables_unidad = ttk.IntVar(value="")
        self.costos_fijos = ttk.IntVar(value="")
        self.precio_venta_unidad = ttk.IntVar(value="")

        
        instrucciones_texo = "Por favor ingrese los siguientes datos"
        instrucciones = ttk.Label(self, text=instrucciones_texo, width=50)
        instrucciones.pack(fill=X, pady=10)


        self.creacion_formulario('Costos Variables Unidad', self.costos_variables_unidad)
        self.creacion_formulario('Gastos Fijos', self.costos_fijos)

        self.creacion_formulario('Precio venta Unidad', self.precio_venta_unidad)

        self.boton_graficar = ttk.Button(self, text="Graficar", command=self.graficacion)
        self.boton_graficar.pack(side=LEFT)

        self.label_resultado = ttk.Label(self, text="")
        self.label_resultado.pack(side=LEFT)





    def creacion_formulario(self,etiqueta, variable):
        self.contenedor_formulario = ttk.Frame(self)# crar un frame aparte
        self.contenedor_formulario.pack(fill=X,expand=YES,pady=5) #expandir formulario  y se expande en X

        contenedor_formulario_etiqueta = ttk.Label(master=self.contenedor_formulario, text=etiqueta, width=50)
        contenedor_formulario_etiqueta.pack(side=LEFT,padx=12)

        entrada_formulario = ttk.Entry(master=self.contenedor_formulario, textvariable=variable)
        entrada_formulario.pack(side=LEFT, padx=5, fill=X, expand=YES)#se expande de ambos lados


        return entrada_formulario
    

    def graficacion(self):
        try:
            costos_fijos = float(self.costos_fijos.get())
            costos_variables_por_unidad = float(self.costos_variables_unidad.get())
            precio_venta_por_unidad = float(self.precio_venta_unidad.get())
            
            punto_equilibrio_unidades = costos_fijos / (precio_venta_por_unidad - costos_variables_por_unidad)
            punto_equilibrio_quetzales = punto_equilibrio_unidades * precio_venta_por_unidad
            
            self.label_resultado.config(text=f"Punto de Equilibrio en Unidades: {punto_equilibrio_unidades}\nPunto de Equilibrio en Quetzales: {punto_equilibrio_quetzales}")
            
            # Crear una gráfica del punto de equilibrio
            unidades = [i for i in range(int(punto_equilibrio_unidades) + 1)]
            ingresos = [precio_venta_por_unidad * u for u in unidades]
            costos_fijos_lista = [costos_fijos] * len(unidades)
            costos_variables = [costos_fijos + costos_variables_por_unidad * u for u in unidades]

            
            plt.figure()
            plt.gcf().set_facecolor("#212121")

            plt.plot(unidades, ingresos, label='Ingresos')
            plt.plot(unidades, costos_fijos_lista, label='Costos Fijos')
            plt.plot(unidades, costos_variables, label='Costos Totales')
            plt.axvline(x=punto_equilibrio_unidades, color='r', linestyle='--', label='Punto de Equilibrio')
            plt.xlabel('Unidades')
            plt.ylabel('Quetzales')
            plt.legend()

            # Integrar la gráfica de Matplotlib en Tkinter
            canvas = FigureCanvasTkAgg(plt.gcf(), self)
            canvas.get_tk_widget().pack()
            canvas.draw()

        except ValueError:
            self.label_resultado.config(text="Por favor, ingrese números válidos.")




        
            



root = ttk.Window("Punto de equilibro", "darkly",resizable=(False, False))
root.geometry("800x700") 
app = App(root)  

root.mainloop()












        