from app import app
import sys
from app.models import db, loaddb, __init_app__
import socket


if __name__ == "__main__":
    #loaddb()
    __init_app__()
    app.run()
    #goles_list = ["run", "create", "start", "go", "drop", "init", "start"]
    #server = "127.0.0.1"
    #gole = goles_list[0]
    #if sys.argv[1:]:
    #    for arg in sys.argv[1:]:
    #        if arg.startswith("--g="):
    #            if arg[4:] not in goles_list:
    #                pass
    #            else:
    #                gole = arg[4:]
    #        if arg.startswith("--s="):
    #            if arg[4:] == "local":
    #                server = "127.0.0.1"
    #            elif arg[4:] == "global":
    #                server = socket.gethostbyname(socket.gethostname())
    #            else:
    #                pass
    #    
    #    
    #if gole == "run" or gole == "start" or gole == "go":
    #    #__run_db__()
    #    print("\n"*5 + "application started " + "\n"*5)
    #    loaddb()
    #    app.run(debug=True, host = server)
    #elif gole == "drop":
    #    #__drop_db__()
    #    pass
    #elif gole == "create":
    #    #__create_db__()
    #    pass
    #elif gole == "init":
    #    #__drop_db__()
    #    #__create_db__()
    #    #__init_db__()
    #    pass
    #else:
    #    app.run(debug=True, host = server, port = 5000)