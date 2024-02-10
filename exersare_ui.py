class Consola:
    def __init__(self,service):
        self.__service=service
        self.__comenzi={
            "cumparare": self.__ui_cumparare,
            "returnare": self.__ui_returnare
        }
    def __ui_cumparare(self,params):
        if len(params)!=2:
            raise Exception("nr p incorect")
        else:
            pass

    def __ui_returnare(self,params):
        if len(params)!=3:
            raise Exception("nr p incorect")
        else:
            pass

    def run(self):
        while True:
            input_initial=input("introduceti o comada: ")
            input_initial=input_initial.strip()
            if input_initial=="exit":
                return
            else:
                partile_comenzii=input_initial.split(">")
                numele_comenzii=partile_comenzii[0].strip()
                if len(input_initial)==1:#mai degraba de partile_comenzii ca inputul initial poate avea mai multe cuvine=te, dar niciun '>'
                    params=[]
                else:
                    params=partile_comenzii[1].strip().split(",")
                if numele_comenzii in self.__comenzi:
                    try:
                        self.__comenzi[numele_comenzii](params)
                    except Exception as ex:
                        print(ex)
                else:
                    print("comanda nu este cunoscuta. Va rugam sa mai incercati")


