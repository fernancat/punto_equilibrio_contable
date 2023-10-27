import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.constants import *
from ttkbootstrap.validation import add_regex_validation
from ttkbootstrap.tableview import Tableview

class App(ttk.Frame):
    def __init__(self, master):
        self.master = master

        super().__init__(self.master,padding=(20,10))  # constructor de ventana

        self.ventana = master 
        self.colors = master.style.colors
        super().__init__(self.ventana,padding=(20,10))#constructor de ventana
        self.pack(fill=BOTH,expand=YES)
        self.precio_venta = ttk.IntVar(value="")
        self.costo_unitario = ttk.IntVar(value=0)
        self.Gatos_fijos = ttk.IntVar(value="")
        self.Unidades_Minimas = ttk.IntVar(value=0)
        
        instrucciones_texo = "Por favor ingrese los siguientes datos"
        instrucciones = ttk.Label(self, text=instrucciones_texo, width=50)
        instrucciones.pack(fill=X, pady=10)


        self.creacion_formulario('Precio de Venta', self.precio_venta)
        self.creacion_formulario('Costo Unitario', self.costo_unitario)
        self.creacion_formulario('Gastos Fijos', self.Gatos_fijos)
        self.creacion_formulario('Unidades Minimas', self.Unidades_Minimas)





    def creacion_formulario(self,etiqueta, variable):
        self.contenedor_formulario = ttk.Frame(self)# crar un frame aparte
        self.contenedor_formulario.pack(fill=X,expand=YES,pady=5) #expandir formulario  y se expande en X

        contenedor_formulario_etiqueta = ttk.Label(master=self.contenedor_formulario, text=etiqueta, width=50)
        contenedor_formulario_etiqueta.pack(side=LEFT,padx=12)

        entrada_formulario = ttk.Entry(master=self.contenedor_formulario, textvariable=variable)
        entrada_formulario.pack(side=LEFT, padx=5, fill=X, expand=YES)#se expande de ambos lados


        return entrada_formulario


        
            




root = ttk.Window("Punto de equilibro", "darkly",resizable=(False, False))
root.geometry("800x700") 
app = App(root)  

root.mainloop()












        