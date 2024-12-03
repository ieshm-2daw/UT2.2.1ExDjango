# UT2.2.1ExDjango: Gestión de Biblioteca Musical con Django 

### **Instrucciones:**  
Desarrolla un sistema básico en Django para gestionar una biblioteca musical. Para ello deberás clonar este repositorio que tiene una estructura inicial del proyecto y completarlo con las siguientes tareas:

### **Tareas Prácticas (10 puntos)**  

1. **Modelos (3 puntos)**  
   Implementa los siguientes modelos:  
   - **Artista**: 
     - Campos: `nombre` (texto), `genero` (texto), `fecha_nacimiento` (fecha, opcional).  
   - **Álbum**: 
     - Campos: `titulo` (texto), `artista` (clave foránea a Artista), `fecha_lanzamiento` (fecha), `genero` (texto).  
   - **Canción**: 
     - Campos: `titulo` (texto), `album` (clave foránea a Álbum), `duracion` (duración).

  Deberás realizar la migración para reflejar los cambios en la base de datos.

2. **Administración (1 punto)**  
   Configura el panel de administración para mostrar los objetos anteriores: Artistas, álbumnes y canciones.  Crea un usuario administrador. 

3. **Vistas y URLs (4 puntos)**  
   Crea las siguientes vistas:  
   - Una vista para listar todos los artistas disponibles en la base de datos.  
   - Una vista para mostrar el detalle de un artista, incluyendo:  
     - Sus álbumes (títulos y fechas de lanzamiento).  
     - Sus canciones agrupadas por álbum.  
Configura las URLs correspondientes para estas vistas.  

4. **Plantillas (2 puntos)**  
   Diseña tres plantillas:
   - Una base.html con la estructura inicial del html y de la que extenderán el resto.
   - Otra para listar los artistas con enlaces al detalle de cada uno.  
   - Un última para mostrar el detalle de un artista con sus álbumes y canciones relacionados.  

---

### **Entrega**  
- Subir todo el código al respositorio correspondiente.  

---

### **Criterios de Evaluación**  
- Correcta implementación de modelos y relaciones.  
- Configuración adecuada del panel de administración.  
- Funcionalidad de las vistas y URLs.  
- Uso correcto del sistema de plantillas.  
- Calidad del código y documentación.
