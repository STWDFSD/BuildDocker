import sys


def application(env, start_response):
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    start_response("200 OK", [("Content-Type", "text/plain")])
    message = "Hello World from a default Nginx uWSGI Python {} app in a Docker container (default)".format(
        version
    )
    return [message.encode("utf-8")]
