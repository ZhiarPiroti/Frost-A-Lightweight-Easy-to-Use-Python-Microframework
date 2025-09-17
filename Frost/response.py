import json
import os
import re

def http_response(body, status_code=200, extra_headers=None):
    status_text = {200: "OK", 404: "Not Found", 302: "Found"}
    if body is None:
        body_bytes = b""
    elif isinstance(body, bytes):
        body_bytes = body
    else:
        body_bytes = body.encode("utf-8")

    headers = ""
    if extra_headers:
        for k, v in extra_headers.items():
            headers += f"{k}: {v}\r\n"

    response = (
        f"HTTP/1.1 {status_code} {status_text.get(status_code, '')}\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        + headers +
        "Connection: close\r\n"
        "\r\n"
    ).encode("utf-8") + body_bytes

    return response



def make_response(result):
    if isinstance(result, bytes):
        return result
    elif isinstance(result, str) and result.startswith("HTTP/1.1"):
        return result.encode()
    else:
        return http_response(result)

def read_template(filename, context=None):
    """
    Read an HTML template from 'templates/', render variables, 
    and inline any static files (CSS, JS) found in <link> or <script> tags.
    """
    path = os.path.join("templates", filename)
    if not os.path.exists(path):
        return "<h1>Template not found!</h1>"

    with open(path, "r", encoding="utf-8") as f:
        template_str = f.read()

    if context:
        def replace_var(match):
            var_name = match.group(1).strip()
            value = context.get(var_name, "")
            if isinstance(value, list):
                return "".join(str(v) for v in value)
            return str(value)
        template_str = re.sub(r"{{\s*(.*?)\s*}}", replace_var, template_str)

    def inline_css(match):
        href = match.group(1)
        css_path = os.path.join("static", href)
        if os.path.exists(css_path):
            with open(css_path, "r", encoding="utf-8") as f:
                css_content = f.read()
            return f"<style>\n{css_content}\n</style>"
        return match.group(0)  

    template_str = re.sub(r'<link\s+rel=["\']stylesheet["\']\s+href=["\'](.*?)["\']\s*/?>', inline_css, template_str)

    def inline_js(match):
        src = match.group(1)
        js_path = os.path.join("static", src)
        if os.path.exists(js_path):
            with open(js_path, "r", encoding="utf-8") as f:
                js_content = f.read()
            return f"<script>\n{js_content}\n</script>"
        return match.group(0)

    template_str = re.sub(r'<script\s+src=["\'](.*?)["\']\s*>\s*</script>', inline_js, template_str)

    return template_str

def redirect(to_path):
    return http_response("", status_code=302, extra_headers={"Location": to_path})


def send_json(data, status=200):
    body = json.dumps(data)
    return http_response(body, status_code=status)
