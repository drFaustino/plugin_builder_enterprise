from qgis.PyQt import QtWidgets

class SummaryPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)

        self.summary = QtWidgets.QTextEdit()
        self.summary.setReadOnly(True)

        self.log = QtWidgets.QTextEdit()
        self.log.setReadOnly(True)

        layout.addWidget(QtWidgets.QLabel("<b>Summary of your choices</b>"))
        layout.addWidget(self.summary)

        layout.addWidget(QtWidgets.QLabel("<b>Generation log</b>"))
        layout.addWidget(self.log)

    def set_summary(self, text):
        self.summary.setPlainText(text)

    def set_log(self, lines):
        self.log.setPlainText("\n".join(lines))
