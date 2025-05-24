
# Importa los módulos necesarios de Python y PyQt5
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QIcon


# Clase principal de la aplicación, hereda de QMainWindow
class BlocDeNotas(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crea un área de texto editable en el centro de la ventana
        self.texto = QTextEdit()
        self.setCentralWidget(self.texto)

        # Configura la ventana principal
        self.setWindowTitle("Bloc de Notas")  # Título de la ventana
        self.setGeometry(100, 100, 800, 600)  # Posición y tamaño de la ventana

        # Llama a la función que crea el menú
        self._crear_menu()

    def _crear_menu(self):
        # Crea la barra de menú superior
        menu = self.menuBar()

        # Agrega el menú "Archivo"
        archivo = menu.addMenu("Archivo")

        # Opción: Nuevo archivo (limpia el texto)
        nuevo = QAction("Nuevo", self)
        nuevo.triggered.connect(self.nuevo_archivo)
        archivo.addAction(nuevo)

        # Opción: Abrir archivo
        abrir = QAction("Abrir", self)
        abrir.triggered.connect(self.abrir_archivo)
        archivo.addAction(abrir)

        # Opción: Guardar archivo
        guardar = QAction("Guardar", self)
        guardar.triggered.connect(self.guardar_archivo)
        archivo.addAction(guardar)

        # Opción: Salir de la aplicación
        salir = QAction("Salir", self)
        salir.triggered.connect(self.close)
        archivo.addAction(salir)

    def nuevo_archivo(self):
        # Borra el contenido actual del editor de texto
        self.texto.clear()

    def abrir_archivo(self):
        # Abre un cuadro de diálogo para seleccionar un archivo de texto
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Textos (*.txt);;Todos (*.*)")
        if ruta:
            try:
                # Abre el archivo seleccionado y carga su contenido en el editor
                with open(ruta, 'r', encoding='utf-8') as archivo:
                    self.texto.setPlainText(archivo.read())
            except Exception as e:
                # Muestra un mensaje de error si no se puede abrir el archivo
                QMessageBox.warning(self, "Error", f"No se pudo abrir el archivo:\n{e}")

    def guardar_archivo(self):
        # Abre un cuadro de diálogo para seleccionar dónde guardar el archivo
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Textos (*.txt);;Todos (*.*)")
        if ruta:
            try:
                # Guarda el contenido del editor en el archivo seleccionado
                with open(ruta, 'w', encoding='utf-8') as archivo:
                    archivo.write(self.texto.toPlainText())
            except Exception as e:
                # Muestra un mensaje de error si no se puede guardar el archivo
                QMessageBox.warning(self, "Error", f"No se pudo guardar el archivo:\n{e}")


# Código principal que inicia la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea la aplicación
    ventana = BlocDeNotas()       # Crea la ventana principal
    ventana.show()                # Muestra la ventana
    sys.exit(app.exec_())         # Inicia el bucle de eventos
