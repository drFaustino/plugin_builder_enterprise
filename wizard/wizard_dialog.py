import os
from qgis.PyQt import QtCore, QtGui, QtWidgets

from .pages.intro_page import IntroPage
from .pages.metadata_page import MetadataPage
from .pages.structure_page import StructurePage
from .pages.options_page import OptionsPage
from .pages.summary_page import SummaryPage
from ..core.generator import PluginGenerator

class PluginWizardDialog(QtWidgets.QDialog):
    def __init__(self, iface=None, parent=None):
        super().__init__(parent)

        # UI
        from .ui.wizard_ui import Ui_WizardDialog
        self.ui = Ui_WizardDialog()
        self.ui.setupUi(self)

        self.iface = iface

        # Stylesheet (opzionale)
        style_path = os.path.join(os.path.dirname(__file__), "..", "resources", "style.qss")
        if os.path.exists(style_path):
            with open(style_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())

        # Pagine del wizard
        self.pages = [
            IntroPage(),
            MetadataPage(),
            StructurePage(),
            OptionsPage(),
            SummaryPage(),
        ]
        for p in self.pages:
            self.ui.Stack.addWidget(p)

        # Sidebar
        self.ui.StepList.addItems([
            "Introduction",
            "Metadata",
            "Structure",
            "Options",
            "Summary",
        ])
        self.ui.StepList.currentRowChanged.connect(self.ui.Stack.setCurrentIndex)
        self.ui.StepList.setCurrentRow(0)

        # Navigazione
        self.ui.Back.clicked.connect(self.prev_page)
        self.ui.Next.clicked.connect(self.next_page)
        self.ui.Finish.clicked.connect(self.finish_and_generate)

        # Cartella di salvataggio
        self.ui.BrowseButton.clicked.connect(self.choose_folder)
        self.ui.SavePath.textChanged.connect(self.update_buttons)

        # Close
        self.ui.Close.clicked.connect(self.close)

        self.update_buttons()

    # ─────────────────────────────────────────────
    # Navigazione
    # ─────────────────────────────────────────────
    def next_page(self):
        row = self.ui.StepList.currentRow()
        if row < len(self.pages) - 1:
            self.ui.StepList.setCurrentRow(row + 1)
        self.update_buttons()
        self.update_summary_if_needed()

    def prev_page(self):
        row = self.ui.StepList.currentRow()
        if row > 0:
            self.ui.StepList.setCurrentRow(row - 1)
        self.update_buttons()

    def choose_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select output folder")
        if folder:
            self.ui.SavePath.setText(folder)

    def update_buttons(self):
        row = self.ui.StepList.currentRow()
        has_path = bool(self.ui.SavePath.text().strip())

        self.ui.Back.setEnabled(row > 0)
        self.ui.Next.setEnabled(row < len(self.pages) - 1 and has_path)
        self.ui.Finish.setEnabled(row == len(self.pages) - 1 and has_path)

    # ─────────────────────────────────────────────
    # Summary
    # ─────────────────────────────────────────────
    def update_summary_if_needed(self):
        row = self.ui.StepList.currentRow()
        if row != len(self.pages) - 1:
            return

        meta = self.pages[1].get_metadata()
        structure = self.pages[2].get_structure()
        options = self.pages[3].get_options()
        save_dir = self.ui.SavePath.text().strip()

        summary_lines = [
            f"Output folder: {save_dir}",
            "",
            f"Plugin name: {meta['name']}",
            f"Version: {meta['version']}",
            f"Author: {meta['author']} <{meta['email']}>",
            f"Homepage: {meta['homepage']}",
            f"Repository: {meta['repository']}",
            f"Tracker: {meta['tracker']}",
            "",
            "Structure:",
            f"  Base plugin: {structure['base']}",
            f"  Processing provider: {structure['processing']}",
            f"  DockWidget: {structure['dockwidget']}",
            f"  Map Tool: {structure['maptool']}",
            "",
           "Options:",
            f"  License type: {options['license_type']}",
            f"  CHANGELOG.md: {options['changelog']}",
            f"  Experimental: {options['experimental']}",
            f"  Create base UI: {options['create_ui']}",
            f"  Icon path: {options['icon_path'] or 'default icon.png'}",
            f"  Icon name: {options['icon_name']}",
            f"  Create base UI: {options['create_ui']}",
        ]

        self.pages[-1].set_summary("\n".join(summary_lines))

    # ─────────────────────────────────────────────
    # Generazione
    # ─────────────────────────────────────────────
    def finish_and_generate(self):
        save_dir = self.ui.SavePath.text().strip()
        if not save_dir:
            QtWidgets.QMessageBox.warning(self, "Missing folder", "Please select an output folder.")
            return

        # 1. Recupera metadata, struttura e opzioni
        meta = self.pages[1].get_metadata()
        structure = self.pages[2].get_structure()
        options = self.pages[3].get_options()

        # 2. Sovrascrivi create_ui con la checkbox principale (se serve)
        # options["create_ui"] = self.ui.CreateBaseUiCheckBox.isChecked()

        # 3. Percorsi
        paths = {
            "save_dir": save_dir,
        }

        # 4. Generazione plugin
        generator = PluginGenerator(save_dir)
        log = generator.generate(meta, structure, options, paths)

        # 5. Mostra log nella pagina Summary
        self.pages[-1].set_log(log)

        QtWidgets.QMessageBox.information(
            self,
            "Plugin generated",
            f"Plugin '{meta['name']}' generated in:\n{save_dir}"
        )


