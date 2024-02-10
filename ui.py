class Consola:
    def __init__(self,service):
        self.__service=service
        self.__comenzi={
            "cautare dupa tip":self.__ui_cauta_tip,
            "cumparare mobila":self.__ui_cumpara,
            "adaugare mobila": self.__ui_adauga_mobila
        }
    def run(self):
        while True:
            input_initial=input(">>>")
            input_initial=input_initial.strip()
            if input_initial=="exit":
                return
            partile_comenzii=input_initial.strip().split(">")
            nume_comanda=partile_comenzii[0]
            if len(partile_comenzii)==1:
                params=[]
            else:
                params=partile_comenzii[1].strip().split(",")
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda](params)
                except Exception as ex:
                    print(ex)
            else:
                print("Nu este posibila efectuarea operatiunii cerute. Va rugam reincercati")

    def __ui_cauta_tip(self,params):
        if len(params)!=1:
            raise Exception("numar parametrii incorect")
        else:
            try:
                ok=0
                tip=params[0].strip()
                lista_ceruta=self.__service.cautare_dupa_tip(tip)
                for mobila in lista_ceruta:
                    print(mobila)
                    ok=1
                if ok==0:
                    print("nu exista")
            except Exception as ex:
                print(ex)

    def __ui_cumpara(self,params):
        if len(params)!=2:
            raise Exception("numar parametrii incorect")
        else:
            try:
                cod=int(params[0])
                nr=int(params[1])
                lista_ceruta=self.__service.cumparare(cod,nr)
                print("nume obiect: "+str(lista_ceruta[0])+" pret total: "+str(lista_ceruta[1])+" stoc ramas: "+str(lista_ceruta[2]))
            except Exception as ex:
                print(ex)

    def __ui_adauga_mobila(self,params):
        if len(params)!=5:
            raise Exception("numar parametrii incorect")
        else:
            try:
                cod = int(params[0].strip())
                tip = params[1].strip()
                nume=params[2].strip()
                stoc=int(params[4].strip())
                pret=int(params[3].strip())
                lista_ceruta=self.__service.adaugare(cod,tip,nume,stoc,pret)
                for x in lista_ceruta:
                    print(x)
            except Exception as ex:
                print(ex)