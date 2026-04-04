# Changelog
All notable changes to **Plugin Builder Enterprise** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to **Semantic Versioning**.

---

## [1.1.0] – 2026‑04‑04
### Added
- Added `plugin_dir_name` to the generator context to ensure correct template rendering.
- Automatic generation of a valid `__init__.py` for each plugin, using the slugified plugin name.
- Improved summary page with clearer reporting of selected options.
- Enhanced internal documentation for generator and wizard components.

### Changed
- Updated `BASE_INIT` template with correct indentation and variable substitution.
- Cleaned and reorganized wizard UI for better clarity and UX.
- Improved metadata validation and consistency across pages.
- Updated internal file structure for better maintainability.

### Removed
- Removed deprecated checkbox **“Create basic (empty) UI in ui/ folder”** from the wizard.
- Eliminated duplicate UI generation logic in `finish_and_generate()`.

### Fixed
- Fixed incorrect import path in generated `__init__.py`.
- Fixed missing variable substitution in templates.
- Fixed plugin generation errors caused by orphaned UI references.
- Fixed inconsistent naming between wizard options and generator logic.

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
- Correct file naming for `<plugin>.py` using slugified plugin name.
- Improved folder creation logic and error handling.

---

## [Unreleased]
### Planned
- Additional plugin templates (Layer Actions, Expression Functions).
- Automatic icon generation presets.
- Multi‑language UI switching at runtime.
- Template preview panel.
