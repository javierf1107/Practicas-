#============================================================
#1. CONSTANTE GLOBALES
#============================================================

NOTA_MINIMA_APROBACIÓN = 3.0
NOTA_MAXIMA = 5.0
NOTA_MINIMA = 2.0
CANTIDAD_NOTAS = 6

#============================================================
#2. FUNCIONES AUXILIARES
#============================================================

def funcion_mostrar_linea():
    """"Imprime una línea de separación, funcion sin parametros y sin retorno"""
    print("= " * 60)
   
def funcion_mostrar_encabezado(titulo):
    """"Imprime un encabezado con el título proporcionado, funcion con parametros y sin retorno"""
    funcion_mostrar_linea()
    print(f"{titulo}")
    funcion_mostrar_linea()

def funcion_pausar():
    """"Pausa la ejecución del programa hasta que el usuario presione Enter, funcion sin parametros y sin retorno"""
    input("Presione Enter para continuar...")
    
#============================================================
#3. FUNCIONES CON RETORNOS (operaciones y validaciones)
#============================================================

def funcion_leer_texto(mensaje, minimo, maximo):
    """"Lee un numero flotante y valida un rango."""
    while True:
        try:
            valor = float(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Advertencia: El valor debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            
def funcion_calcular_promedio(notas):
    if(len(notas) == 0):
        return 0.0
    return sum(notas) / len(notas)
        
def funcion_determinar_estado(promedio):
    """Determina el estado del estudiante según su promedio."""
    if promedio >= NOTA_MINIMA_APROBACIÓN:
        return "Aprobado"
    else:
        return "Reprobado"
    

def funcion_determinar_mencion(promedio):
    """Determina la mención del estudiante según su promedio."""
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy Bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= Nota_MINIMA_APROBACIÓN:
        return "Regular"
    else:
        return "En recuperación"
    

#===================================================================
#4. CLASE ESTUDIANTE (POO - encapsulamiento, herencia, polimorfismo)
#===================================================================
       
class Estudiante:
    """Clase que representa a un estudiante con sus atributos y métodos
    Encapsulamiento: Los atributos son privados y se accede a ellos mediante métodos públicos."""
    
    #Variable de clase
    _cantidad_estudiantes = 0
    
    def __init__(self, NombreCompleto, edad, grado):
        """Inicializa un objeto Estudiante con nombre y lista de notas.
        Contructor de la clase
        self hacer referencia al objeto que actual
        """
        Estudiante._cantidad_estudiantes += 1 
        self._id = Estudiante._cantidad_estudiantes + 1
        self._nombreCompleto = NombreCompleto
        self._edad = edad
        self._grado = grado
        self._notas = []
        self._promedio = 0.0
        self._estado = ""  
        self._mencion = ""
        self._rendimiento = ""
        
    ##=============== GETTERS (acceso) =========================
        
    @property
    def id(self):
        """Devuelve el ID del estudiante."""
        return self._id
    
    @property
    def NombreCompleto(self):
            """Devuelve el nombre completo del estudiante."""
            return self._nombreCompleto
        
    @property
    def edad(self):
            """Devuelve la edad del estudiante."""
            return self._edad

    @property
    def grado(self):
            """Devuelve el grado del estudiante."""
            return self._grado
        
    @property
    def notas(self):
            """Devuelve la lista de notas del estudiante."""
            return self._notas
    @property
    def promedio(self):
        """Devuelve el promedio del estudiante."""
        return self._promedio
    
    @property
    def estado(self):
            """Devuelve el estado del estudiante."""
            return self._estado
        
    @property
    def mencion(self):
        """Devuelve la mención del estudiante."""
        return self._mencion
    
    @property
    def rendimiento(self):
        """Devuelve el rendimiento del estudiante."""
        return self._rendimiento
         
    ##=============== SETTERS (modificadores) =========================
    @edad.setter
    def edad(self, valor):
        """Establece la edad del estudiante."""
        if 0 <= valor < 65:
         self._edad = valor
        else:
            raise ValueError("La edad debe ser un numero positivo.")