# 📘 Plugin Builder Enterprise — README
## 🧩 Overview
Plugin Builder Enterprise is an advanced generator for QGIS plugins, designed to produce fully structured, Qt6‑ready, QGIS‑4‑compatible plugin templates.
Through a guided wizard, it helps developers configure every aspect of a new plugin: metadata, internal structure, optional components, licensing, documentation, and resources.
The result is a clean, extensible, production‑ready plugin that follows QGIS best practices.

## 🚀 Features

✔ Complete plugin structure
Base plugin module
Main entry point: <plugin>_main.py
Standard folders:
resources/
i18n/
ui/
processing/ (optional)

✔ Optional components
Processing Provider  
Generates a ready‑to‑extend provider for QGIS Processing Toolbox.
DockWidget  
Creates a dockable panel with a Qt6 UI template.
Map Tool  
Provides a starting point for interactive map‑canvas tools.
Base UI (.ui)  
Empty Qt Designer file to accelerate interface development.

✔ Documentation & licensing
Automatically generates:
README.md
CHANGELOG.md
LICENSE (MIT or GPL v3)
metadata.txt compliant with QGIS standards

✔ Resources & internationalization
Custom plugin icon (PNG/JPG/SVG)

Translation files (.ts) for:
English
Italian
Spanish
French

✔ Detailed generation log
The final wizard page displays a complete log of all created files and folders.

🛠 Requirements
QGIS 4.x
Python 3.12
Qt6 / PyQt6
Write permissions in the output directory

## 🧭 Using the Wizard
Open Plugin Builder Enterprise from:
Plugins → Plugin Builder Enterprise
Follow the guided steps:
Metadata
Structure selection
Options & licensing
Summary & generation log
Click Generate Plugin to create the full plugin structure.
The wizard remains open after generation, allowing you to review the log or generate another plugin.

## 📄 License
This project is licensed under the GNU General Public License v3.0 (GPL‑3.0).
You may redistribute and/or modify this software under the terms of the GPL v3 as published by the Free Software Foundation.
A copy of the license should be included in the file LICENSE.
If it is missing, you can obtain it at:
https://www.gnu.org/licenses/gpl-3.0.html

## 🤝 Contributing
Contributions, suggestions, and improvements are welcome.
Please open an issue or submit a pull request on the project repository.