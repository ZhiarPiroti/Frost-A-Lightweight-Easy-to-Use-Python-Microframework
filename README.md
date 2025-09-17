# Frost

Frost is a lightweight Python web framework built from scratch.  
It supports routing, templates, static files, forms, and session handling — all without any heavy dependencies.

## Features

- Minimal and fast
- Route handling with dynamic parameters
- Template rendering with variable replacement
- Inline static files (CSS & JS)
- Form handling (POST & GET)
- Simple session management

## Installation

You can install Frost locally via pip:

```bash
pip install pythonfrost
```

## Quick Start
```py
from pythonfrost import Server, route, read_template

@route("/")
def home():
    return read_template("index.html")

Server()
```


## File Structure
```
frost/
├─ pythonfrost/           
│  ├─ __init__.py
│  ├─ server.py
│  ├─ router.py
│  ├─ response.py
│  └─ session.py
├─ setup.py
├─ README.md
└─ LICENSE
```

## Contributing

Frost is open-source! Feel free to fork, submit issues, or contribute improvements.
