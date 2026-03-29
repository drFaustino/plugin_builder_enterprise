from qgis.PyQt import QtWidgets

class IntroPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)

        title = QtWidgets.QLabel("<h2>Welcome to Plugin Builder Enterprise</h2>")

        desc = QtWidgets.QLabel(
            "<p>This wizard guides you through the creation of a complete, Qt6‑ready QGIS plugin.</p>"

            "<h3>Plugin name syntax</h3>"
            "<p>The plugin name must follow these rules:</p>"
            "<li>Begin with a letter (A–Z or a–z)</li>"
            "<li>Contain only letters, numbers, and underscores</li>"
            "<li>No spaces, hyphens, accented characters, or symbols</li>"
            "<p><b>Valid examples:</b> <i>MyPlugin</i>, <i>raster_tools</i>, <i>GeoAnalyzer2</i><br>"
            "<b>Invalid examples:</b> <i>my plugin</i>, <i>plugin-name</i>, <i>analisi©</i></p>"

            "<h3>Plugin dependencies</h3>"
            "<p>You may declare optional dependencies required by your plugin. Allowed cases:</p>"
            "<li>Other QGIS plugins (e.g., <i>processing</i>)</li>"
            "<li>Python packages available via qpip (e.g., <i>numpy</i>, <i>matplotlib</i>)</li>"
            "<li>Versioned dependencies (e.g., <i>qpip==1.1.1</i>)</li>"
            "<p><b>Not allowed:</b> local paths, standard Python modules, QGIS built‑in modules.</p>"

            "<h3>Structure</h3>"
            "<p>You can choose which components to include in your plugin, such as a base plugin, "
            "a Processing provider, a DockWidget or a Map Tool. Selected elements will be generated automatically.</p>"

            "<h3>Options</h3>"
            "<p>Here you can choose: license type (MIT or GPL v3)</li>, whether to generate a CHANGELOG,"
            "whether the plugin is experimental, whether to generate a base UI (.ui) file, "
            "a custom plugin icon.</p>"

            "<h3>Summary</h3>"
            "<p>The final page provides a complete overview of your choices and displays the generation log. "
            "Review the information carefully before completing the process.</p>"

            "<p>Once finished, Plugin Builder Enterprise will generate a fully structured, ready‑to‑use QGIS plugin.</p>"
        )
        desc.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch()
