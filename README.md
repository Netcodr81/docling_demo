# docling_demo

## Setup Instructions

Follow these steps to clone and set up the project with a local Python environment:

### 1. Clone the repository
```sh
git clone https://github.com/Netcodr81/docling_demo.git
cd docling_demo
```

### 2. Create a virtual environment
```sh
python -m venv .venv
```

### 3. Activate the virtual environment
- **PowerShell (Windows):**
	```powershell
	.\.venv\Scripts\Activate.ps1
	```
- **Command Prompt (Windows):**
	```cmd
	.\.venv\Scripts\activate.bat
	```
- **Bash (Linux/macOS):**
	```sh
	source .venv/bin/activate
	```

### 4. Install required packages
```sh
pip install -r requirements.txt
```

### 5. Run your project
Refer to project-specific instructions or scripts as needed.

---

# **Note:**
- Do not commit the `.venv` folder. It is excluded via `.gitignore`.
- All required packages are listed in `requirements.txt`.
- If you install new packages, rerun the following command to update `requirements.txt`:
	```sh
	pip freeze > requirements.txt
	```
	This file is not updated automatically.
# docling_demo