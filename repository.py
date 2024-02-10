from domain import Mobila
class MobilaRepo:
    def __init__(self):
        self.__bucati_mobila={}

    def add_mobila(self,bucata_mobila):
        id=bucata_mobila.get_id()
        if id in self.__bucati_mobila.keys():
             raise Exception("id exista deja!")
        else:
            self.__bucati_mobila[id]=bucata_mobila

    def cautare_dupa_id(self,id):
        ok=0
        for cheie in list(self.__bucati_mobila.keys()):
            if self.__bucati_mobila[cheie].get_id()==id:
                return self.__bucati_mobila[cheie]
                ok=1
        if ok==0:
            raise Exception("nu exista id!")
    def get_all(self):
        return  [self.__bucati_mobila[cheie] for cheie in self.__bucati_mobila.keys()]

def test_cdi():
    x=MobilaRepo()
    m=Mobila(1,2,3,4,5)
    x.add_mobila(m)
    assert x.cautare_dupa_id(1)==m

def test_ga():
    x=MobilaRepo()
    m=Mobila(1,2,3,4,5)
    x.add_mobila(m)
    assert x.get_all()==[m]

