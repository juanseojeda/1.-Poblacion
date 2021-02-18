import os
class Poblacion:
    def __init__(self):
        'lee el fichero y carga la lista de poblacion'
        self.setPoblacion_v2()
        self.setPaises()


    def setPoblacion_v1(self):
        'Carga la poblacion a partir de una cadena'
        pob= "Spain,ESP,1960,30455000\n"+ \
             "Spain,ESP,1961,30739250\n"+ \
             "Spain,ESP,1962,31023366\n"+ \
             "Spain,ESP,1963,31296651\n"+ \
             "Spain,ESP,1964,31609195\n"+ \
             "Spain,ESP,1965,31954292\n"+ \
             "Spain,ESP,1966,32283194\n"+ \
             "Spain,ESP,1967,32682947\n"+ \
             "Spain,ESP,1968,33113134\n"+ \
             "Spain,ESP,1969,33441054\n"+ \
             "Zimbabwe,ZWE,2016,16150362"
        self.lstPob=pob.split("\n")

    def setPoblacion_v2(self):
        'carga la población a partir de un fichero'
        currentDirectory = os.getcwd()
        print("Directorio actual:"+currentDirectory)
        with open("./data/population.csv") as reader:
            self.lstPob=list(map(str.rstrip, reader))
        


    def setPaises(self):
        self.paises=set() 
        for pob in self.lstPob:
            pais=pob.split(",")[1]
            self.paises.add(pais)


    def getPoblacion(self, cod_pais):
        lstPob=[]
        for pob in self.lstPob:
            pais=pob.split(",")[1]
            if (pais == cod_pais):
                lstPob.append(pob)
        return lstPob

    def getPaises(self):
        return self.paises

    def getNPaises(self):
        return len(self.paises)

    def hayDatos(self, cod_pais):
        print (cod_pais)  
        return (cod_pais in self.paises)
