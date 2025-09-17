routes = {}


def route(path, methods=["GET"]):
    def wrapper(func):
        for method in methods:
            routes[(method.upper(), path)] = func
        return func
    return wrapper


def handle_request(method, request_path, body_bytes=None):
    for (route_method, route_path), handler in routes.items():
        if route_method != method:
            continue

        route_parts = route_path.strip("/").split("/")
        request_parts = request_path.strip("/").split("/")

        if len(route_parts) != len(request_parts):
            continue

        params = {}
        matched = True
        for r_part, req_part in zip(route_parts, request_parts):
            if r_part.startswith("<") and r_part.endswith(">"):
                param_name = r_part[1:-1]
                params[param_name] = req_part
            elif r_part != req_part:
                matched = False
                break

        if matched:
            if method.upper() == "POST":
                form_data = {}
                if body_bytes:
                    from urllib.parse import parse_qs
                    form_data = parse_qs(body_bytes.decode("utf-8"))
                    form_data = {k: v[0] if len(v)==1 else v for k,v in form_data.items()}
                return handler(**params, form_data=form_data)
            else:
                return handler(**params)

    return "404 Not Found"

