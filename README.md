# EFit
[![Python 3.6](https://img.shields.io/badge/python-3.9-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Windows-orange.svg)]()

EFit is a sport management software in spanish for a school project.

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/EFit/main/images/logo_efit.png" alt="drawing" width="400"/>
  <img src="https://raw.githubusercontent.com/ErtonDev/EFit/main/images/logo_efit_NEW.png" alt="drawing" width="400"/>
</p>

> EFit logo and logo for new training windows

## Resources
EFit uses the following modules:
 - PyQt5 https://pypi.org/project/PyQt5/
 - PySide2 https://pypi.org/project/PySide2/
 - pathlib https://pypi.org/project/pathlib/
 - random *(Installed by default)*
 - io *(Installed by default)*
 - subprocess *(Installed by default)*

Make sure to have them installed on your computer.

## Execution
`login.py` is supposed to be executed first. Then it calls a subprocess for `main.py` once you have logged in or registered.

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/EFit/main/images/EFit Login_005.png" alt="drawing" width=290/>
  <img src="https://raw.githubusercontent.com/ErtonDev/EFit/main/images/EFit_006.png" alt="drawing" width=600/>
</p>

> EFit's "Login" and "Main" windows being executed on Linux OS in spanish

```python
## OPENS MAIN WINDOW
############################################################
# subprocess module allows secondary tasks
subprocess.Popen(['python', (client_path / '../main.py').resolve()]) # Opens main window
sys.exit('login.py') # Closes
```

Once executing `main.py`, you can call a subprocess for `train.py` which will allow you to display a new window while `main.py` stays active.

<p align="center">
  <img src="https://raw.githubusercontent.com/ErtonDev/EFit/main/images/Nuevo Entrenamiento_007.png" alt="drawing" width=600/>
</p>

> EFit's "New Training" window being executed on Linux OS in spanish

```python
subprocess.Popen(['python', (client_path / '../train.py').resolve()])  # Opens train window
```

To execute the script type the following command in your terminal:
```
login.py
```
or
```
python login.py
```
In case you have an especific version of python, type:
```
python3 login.py         or         python2 login.py         --- (Depending on your version)
```

---

**REMINDER: EFit isn't under development and won't be finished.**
