# PythonFrost

The ultra-fast, zero-dependency Python web microframework.
Built entirely with Python’s standard libraries—no external packages required. From HTTP handling and routing to sessions and template rendering, everything is implemented from scratch. Perfect for blazing-fast web projects.

# Documentation

You can access docs from https://zhiarpiroti.github.io/PythonFrost/

# 🌟 Features

Lightning Fast: 2x faster than FastAPI, 4x faster than Flask (tested on template rendering & JSON responses).

Zero Dependencies: Pure Python, no external packages needed.

Dynamic Routing: Handle routes with parameters effortlessly.

Template Rendering: Replace variables in HTML templates seamlessly.

Inline Static Files: Serve CSS & JS directly.

Form Handling: POST & GET ready.

Simple Session Management: Keep your users’ sessions lightweight and fast.

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

PythonFrost is open-source! Fork, submit issues, or contribute improvements.
Make the web faster, together.
