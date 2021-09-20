import os
from core.api import app


def run_application():
    """
    Runs the flask application with some custom configurations.
    """
    debug = os.environ.get("DEBUG", False)
    host = os.environ.get("APP_HOST", "localhost")
    port = int(os.environ.get('APP_PORT', 5000))

    app.run(debug=debug, host=host, port=port, use_reloader=False)


if __name__ == "__main__":
    run_application()
