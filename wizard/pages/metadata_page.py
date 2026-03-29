from qgis.PyQt import QtWidgets, QtCore, QtGui

class MetadataPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QFormLayout(self)

        info = QtWidgets.QLabel(
            "<h3>Plugin metadata</h3>"
            "<p>These fields define how your plugin appears in QGIS and in its metadata.</p>"
        )
        info.setWordWrap(True)
        layout.addRow(info)

        self.name_edit = QtWidgets.QLineEdit()
        self.name_edit.setPlaceholderText("my_plugin_name")

        # VALIDAZIONE: solo lettere, numeri e underscore
        regex = QtCore.QRegularExpression("^[a-zA-Z][a-zA-Z0-9_]*$")
        validator = QtGui.QRegularExpressionValidator(regex)
        self.name_edit.setValidator(validator)

        self.about_edit = QtWidgets.QLineEdit()
        self.desc_edit = QtWidgets.QTextEdit()
        self.version_edit = QtWidgets.QLineEdit("1.0.0")
        self.author_edit = QtWidgets.QLineEdit()
        self.email_edit = QtWidgets.QLineEdit()
        self.homepage_edit = QtWidgets.QLineEdit()
        self.repo_edit = QtWidgets.QLineEdit()
        self.tracker_edit = QtWidgets.QLineEdit()
        self.tags_edit = QtWidgets.QLineEdit("plugin,template,builder")
        self.dep_edit = QtWidgets.QLineEdit("")

        self.qgis_min_edit = QtWidgets.QLineEdit("4.00")
        self.qgis_max_edit = QtWidgets.QLineEdit("4.99")

        layout.addRow("Plugin name:", self.name_edit)
        layout.addRow(QtWidgets.QLabel(
            "<i>The plugin name must start with a letter and contain only letters, numbers, and underscores.</i>"
        ))

        layout.addRow("About (short):", self.about_edit)
        layout.addRow("Description:", self.desc_edit)
        layout.addRow("Version:", self.version_edit)
        layout.addRow("Author:", self.author_edit)
        layout.addRow("Email:", self.email_edit)
        layout.addRow("Homepage:", self.homepage_edit)
        layout.addRow("Repository:", self.repo_edit)
        layout.addRow("Tracker:", self.tracker_edit)
        layout.addRow("Tags:", self.tags_edit)
        layout.addRow("Plugin dependencies:", self.dep_edit)
        layout.addRow("QGIS minimum version:", self.qgis_min_edit)
        layout.addRow("QGIS maximum version:", self.qgis_max_edit)

    def get_metadata(self):
        return {
            "name": self.name_edit.text().strip(),
            "about": self.about_edit.text().strip(),
            "description": self.desc_edit.toPlainText().strip(),
            "version": self.version_edit.text().strip(),
            "author": self.author_edit.text().strip(),
            "email": self.email_edit.text().strip(),
            "homepage": self.homepage_edit.text().strip(),
            "repository": self.repo_edit.text().strip(),
            "tracker": self.tracker_edit.text().strip(),
            "tags": self.tags_edit.text().strip(),
            "plugin_dependencies": self.dep_edit.text().strip(),
            "qgis_min": self.qgis_min_edit.text().strip(),
            "qgis_max": self.qgis_max_edit.text().strip(),
        }
