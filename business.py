from domain import Mobila
from repository import MobilaRepo
class MobilaService:
    def __init__(self,repo):
        self.__repo=repo

    def adaugare(self,a,b,c,d,e):
        elem=Mobila(a,b,c,d,e)
        self.__repo.add_mobila(elem)
        return self.__repo.get_all()
    def cumparare(self,cod,nr):
        try:
            bucata_mobila=self.__repo.cautare_dupa_id(cod)
            pret=bucata_mobila.get_pret()
            pret=pret*nr
            stoc=bucata_mobila.get_stoc()
            stoc=stoc-nr
            nume=bucata_mobila.get_nume()
            return [nume,pret,stoc]
        except Exception as ex:
            raise Exception(ex)
    def cautare_dupa_tip(self,tip):
        lista=self.__repo.get_all()
        lista_ceruta=[]
        for mobila in lista:
            if mobila.get_tip()==tip:
                lista_ceruta.append(mobila)

        return lista_ceruta

def test_cdt():
    '''
    returneaza o lisat cu obiecte cu tipul dat
    :return:
    '''
    r=MobilaRepo()
    m=MobilaService(r)
    a=Mobila(1,"corp iluminat",3,4,5)
    b = Mobila(2, "corp iluminat", 3, 4, 5)
    assert m.cautare_dupa_tip("corp iluminat") == []
    r.add_mobila(a)
    r.add_mobila(b)
    assert m.cautare_dupa_tip("corp iluminat")==[a,b]

def test_cumparare():
    r = MobilaRepo()
    m = MobilaService(r)
    a = Mobila(1, "corp iluminat", 3, 4, 5)
    b = Mobila(2, "corp iluminat", 3, 4, 5)
    r.add_mobila(a)
    assert m.cumparare(1,1) == [3,4,4]
    r.add_mobila(b)
    assert m.cautare_dupa_tip("corp iluminat") == [a, b]
test_cumparare()
test_cdt()
