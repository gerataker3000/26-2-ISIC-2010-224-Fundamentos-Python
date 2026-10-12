# Instrucciones

## Comandos enviroment
```
python -m venv .venv
```
```
.\.venv\Scripts\Activate.ps1
```

Si da error de permisos
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
## Dependencias
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

## Correr app
```
streamlit run app.py
```

## comando para desactivar
```
deactivate
```