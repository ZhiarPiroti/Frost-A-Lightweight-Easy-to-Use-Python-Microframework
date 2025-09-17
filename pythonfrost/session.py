from response import *

sessions = {}

def set_cookie_header(session_name, path="/", conn_type="HttpOnly"):
    headers = {
        "Set-Cookie": f"session_id={session_name}; Path={path}; {conn_type}"
    }
    return http_response("<></>", extra_headers=headers)


def create_session(name, data, path="/", conn_type="HttpOnly"):

    sessions[name] = {"data": data, "path": path, "conn_type": conn_type}
    return name

def session(name, data, path="/", conn_type="HttpOnly"):
    s = create_session(name, data, path=path, conn_type=conn_type)
    return set_cookie_header(s, path=path, conn_type=conn_type)

def get_session(session_name):
    if session_name in sessions:
        return sessions.get(session_name)["data"]
    else:
        return ""
    


def destroy_session(session_name):
    if session_name in sessions:
        path = sessions[session_name]["path"]
        del sessions[session_name]
        headers = {
            "Set-Cookie": f"session_id={session_name}; Path={path}; Expires=Thu, 01 Jan 1970 00:00:00 GMT"
        }

        return http_response("<></>", extra_headers=headers)
