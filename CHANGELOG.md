# Changelog
All notable changes to **Plugin Builder Enterprise** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to **Semantic Versioning**.

---

## [1.0.0] – 2026‑03‑29
### Added
- Initial release of **Plugin Builder Enterprise**.
- Full Qt6‑compatible wizard for generating QGIS 4 plugins.
- Metadata configuration page with validation and syntax rules.
- Plugin structure selector (base plugin, Processing provider, DockWidget, Map Tool).
- Options page with:
  - MIT or GPL v3 license selection  
  - CHANGELOG generation  
  - Experimental flag  
  - Base UI (.ui) generator  
  - Custom icon support  
- Automatic creation of:
  - `metadata.txt`  
  - `README.md`  
  - `LICENSE` and `LICENSE.md`  
  - `CHANGELOG.md`  
  - Translation files (`.ts`) for EN/IT/ES/FR  
- Log viewer in the Summary page.
- Wizard remains open after generation; added **Close** button.

### Fixed
- Correct file naming for `<plugin>_main.py` using slugified plugin name.
- Improved folder creation logic and error handling.

---

## [Unreleased]
### Planned
- Additional plugin templates (Layer Actions, Expression Functions).
- Automatic icon generation presets.
- Multi‑language UI switching at runtime.
- Template preview panel.
