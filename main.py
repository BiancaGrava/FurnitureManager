from ui import Consola
from business import MobilaService
from repository import MobilaRepo

repo=MobilaRepo()
serv=MobilaService(repo)
cons=Consola(serv)

cons.run()