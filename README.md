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

# Benchmark Test

Tested with 100 sequential requests on localhost (127.0.0.1) using a standard machine (CPU: i5, RAM: 8GB).

Test code:
```py
import requests
import time

def test_request(url, n=100):
    times = []
    for i in range(n):
        start = time.time()
        r = requests.get(url)
        elapsed = time.time() - start
        times.append(elapsed)
    avg_time = sum(times) / n
    print(f"{url} - Average response time for {n} requests: {avg_time:.4f}s")

# PythonFrost
test_request("http://127.0.0.1:5000/", 100)

# FastAPI
test_request("http://127.0.0.1:8000/", 100)

# Flask
test_request("http://127.0.0.1:7000/", 100)
```


| Framework       | Avg Response Time (per request) |
| --------------- | ------------------------------- |
| **PythonFrost** | **0.0011s (1.1 ms)** ⚡         |
| FastAPI         | 0.0019s (1.9 ms)                |
| Flask           | \~0.0060s (6 ms)                |


✅ PythonFrost is the simplest and fastest Python web framework.

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
