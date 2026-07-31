# Virtual Environment

## Introduction

A virtual environment is an isolated Python environment created for a specific project.

Each virtual environment has its own:

- Installed packages
- Package versions
- Python executables

This prevents dependency conflicts between projects.

---

# Why Use a Virtual Environment?

Without a virtual environment:

- All projects share the same global packages.
- Installing a new package version may break another project.
- Dependency management becomes difficult.

With a virtual environment:

- Each project is isolated.
- Different projects can use different package versions.
- Projects become easier to share and reproduce.

---

# Creating a Virtual Environment

Windows:

```bash
python -m venv venv
```

macOS / Linux:

```bash
python3 -m venv venv
```

---

# Activating a Virtual Environment

### Windows (Command Prompt)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, your terminal usually displays the environment name:

```text
(venv)
```

---

# Deactivating

```bash
deactivate
```

---

# Installing Packages

Install:

```bash
pip install requests
```

Upgrade:

```bash
pip install --upgrade requests
```

Remove:

```bash
pip uninstall requests
```

List installed packages:

```bash
pip list
```

Show package information:

```bash
pip show requests
```

---

# requirements.txt

Save installed packages:

```bash
pip freeze > requirements.txt
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Example:

```text
requests==2.32.0
numpy==2.3.1
pandas==2.3.0
```

---

# Common Commands

| Command | Purpose |
|---------|---------|
|`python -m venv venv`|Create environment|
|`activate`|Activate environment|
|`deactivate`|Deactivate environment|
|`pip install`|Install package|
|`pip uninstall`|Remove package|
|`pip list`|List packages|
|`pip freeze`|Generate requirements file|

---

# Best Practices

- Create one virtual environment per project.
- Do not commit the `venv/` folder to Git.
- Commit `requirements.txt`.
- Keep dependencies updated when appropriate.
- Activate the environment before installing packages.

---

# Summary

- Virtual environments isolate project dependencies.
- `venv` is the standard library tool for creating them.
- `pip` installs and manages packages.
- `requirements.txt` makes projects reproducible.
