from qgis.PyQt import QtWidgets

class StructurePage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)

        info = QtWidgets.QLabel(
            "<h3>Plugin structure</h3>"
            "<p>In this section you can choose which components will be included in your plugin. "
            "The base plugin provides the essential framework and is recommended in almost all cases. "
            "A Processing provider allows you to expose algorithms in the QGIS Processing Toolbox. "
            "A DockWidget adds a dockable panel inside the QGIS interface, ideal for tools that require persistent controls. "
            "A Map Tool enables interactive actions directly on the map canvas, useful for drawing, selecting or inspecting features. "
            "Select only the components you need; the wizard will automatically generate all the required files and structure.</p>"
        )
        info.setWordWrap(True)

        self.base_cb = QtWidgets.QCheckBox("Base plugin (recommended)")
        self.base_cb.setChecked(True)

        self.proc_cb = QtWidgets.QCheckBox("Processing provider (optional)")
        self.dock_cb = QtWidgets.QCheckBox("DockWidget (optional)")
        self.maptool_cb = QtWidgets.QCheckBox("Map Tool (optional)")

        layout.addWidget(info)
        layout.addWidget(self.base_cb)
        layout.addWidget(self.proc_cb)
        layout.addWidget(self.dock_cb)
        layout.addWidget(self.maptool_cb)
        layout.addStretch()

    def get_structure(self):
        return {
            "base": self.base_cb.isChecked(),
            "processing": self.proc_cb.isChecked(),
            "dockwidget": self.dock_cb.isChecked(),
            "maptool": self.maptool_cb.isChecked(),
        }
