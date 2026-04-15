import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout
from docx2pdf import convert

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word to PDF Converter")

        self.button = QPushButton("Select Word File")
        self.button.clicked.connect(self.convert_file)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def convert_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Word Files (*.docx)")
        if file_path:
            output = file_path.replace(".docx", ".pdf")
            convert(file_path, output)
            print("Converted:", output)

app = QApplication(sys.argv)
window = ConverterApp()
window.show()
sys.exit(app.exec_())