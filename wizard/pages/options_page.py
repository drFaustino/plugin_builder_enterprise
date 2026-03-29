import os
from qgis.PyQt import QtWidgets, QtGui, QtCore

class OptionsPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)
        form = QtWidgets.QFormLayout()
        layout.addLayout(form)

        info = QtWidgets.QLabel(
            "<h3>Documentation and licensing</h3>"
            "<p>In this section you can define how your plugin will be documented and distributed. "
            "You may choose the license to apply, generate optional documentation files and mark the plugin as experimental. "
            "The license determines how the plugin can be reused or modified by others. "
            "The CHANGELOG helps track the evolution of the project over time. "
            "You can also generate a minimal UI file to serve as a starting point for interface design, "
            "and optionally select a custom icon that will represent your plugin in QGIS. "
            "All selected elements will be created automatically during plugin generation.</p>"
        )
        info.setWordWrap(True)

        form.addRow(info)

        # LICENSE CHOICE
        self.license_choice = QtWidgets.QComboBox()
        self.license_choice.addItems(["MIT License", "GPL v3 License"])
        form.addRow("License type:", self.license_choice)

        # OTHER OPTIONS
        self.changelog_cb = QtWidgets.QCheckBox("Create CHANGELOG.md")
        self.experimental_cb = QtWidgets.QCheckBox("Mark plugin as experimental")

        self.changelog_cb.setChecked(True)

        form.addRow(self.changelog_cb)
        form.addRow(self.experimental_cb)

        self.create_ui_cb = QtWidgets.QCheckBox("Create base UI file (empty .ui template)")
        form.addRow(self.create_ui_cb)

        # ICON SELECTION
        icon_box = QtWidgets.QGroupBox("Plugin icon")
        icon_layout = QtWidgets.QHBoxLayout(icon_box)

        self.icon_path_edit = QtWidgets.QLineEdit()
        self.icon_browse_btn = QtWidgets.QPushButton("Select icon…")
        self.icon_preview = QtWidgets.QLabel()
        self.icon_preview.setFixedSize(64, 64)
        self.icon_preview.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.icon_preview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        icon_layout.addWidget(self.icon_path_edit)
        icon_layout.addWidget(self.icon_browse_btn)
        icon_layout.addWidget(self.icon_preview)

        layout.addWidget(icon_box)
        layout.addStretch()

        self.icon_browse_btn.clicked.connect(self.choose_icon)

    def choose_icon(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select plugin icon",
            "",
            "Images (*.png *.jpg *.jpeg *.svg)"
        )
        if path:
            self.icon_path_edit.setText(path)
            pix = QtGui.QPixmap(path)
            if not pix.isNull():
                self.icon_preview.setPixmap(
                    pix.scaled(
                        self.icon_preview.size(),
                        QtCore.Qt.AspectRatioMode.KeepAspectRatio,
                        QtCore.Qt.TransformationMode.SmoothTransformation
                    )
                )

    def get_options(self):
        icon_path = self.icon_path_edit.text().strip() or None
        icon_name = os.path.basename(icon_path) if icon_path else "icon.png"

        return {
            "license_type": self.license_choice.currentText(),
            "changelog": self.changelog_cb.isChecked(),
            "experimental": self.experimental_cb.isChecked(),
            "icon_path": icon_path,
            "icon_name": icon_name,
            "create_ui": self.create_ui_cb.isChecked(),
        }

