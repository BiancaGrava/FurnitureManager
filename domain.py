class Mobila:
    def __init__(self,cod,tip,nume,pret,stoc):
        self.__id=cod
        self.__tip=tip
        self.__nume=nume
        self.__pret=pret
        self.__stoc=stoc

    def get_id(self):
        return self.__id
    def get_tip(self):
        return self.__tip
    def get_nume(self):
        return self.__nume
    def get_pret(self):
        return self.__pret
    def get_stoc(self):
        return self.__stoc

    def set_id(self,id):
        self.__id=id
    def set_tip(self,tip):
        self.__tip=tip
    def set_pret(self,pret):
        self.__pret=pret
    def set_stoc(self,stoc):
        self.__stoc=stoc

    def __eq__(self,mobila):
        return self.__id==mobila.__id
    def __str__(self):
        return f"{self.__id}, {self.__tip}, {self.__nume}, {self.__stoc}, {self.__pret}"

def test_creare_mobila():
    id=12
    nume="lampa"
    tip="corp iluminat"
    pret=300
    stoc=2
    mobila=Mobila(id,tip,nume,pret,stoc)
    assert mobila.get_id()==12
    assert mobila.get_nume()=="lampa"
    assert mobila.get_tip()=="corp iluminat"
    assert mobila.get_pret()==300
    assert mobila.get_stoc()==2
    
test_creare_mobila()
