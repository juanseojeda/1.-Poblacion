import unittest
from Poblacion import Poblacion
class Testsbasicos(unittest.TestCase):
    def setUp(self):
        self.pob= Poblacion()
 
    def test_poblacion_Zimbawe(self):
        pob_test= "Zimbabwe,ZWE,1960,3747369\n" + \
                "Zimbabwe,ZWE,1961,3870756\n" + \
                "Zimbabwe,ZWE,1962,3999419\n" + \
                "Zimbabwe,ZWE,1963,4132756\n" + \
                "Zimbabwe,ZWEls,1964,4269863\n" + \
                "Zimbabwe,ZWE,1965,4410212\n" + \
                "Zimbabwe,ZWE,1966,4553433\n" + \
                "Zimbabwe,ZWE,1967,4700041\n" + \
                "Zimbabwe,ZWE,1968,4851431\n" + \
                "Zimbabwe,ZWE,1969,5009514\n" + \
                "Zimbabwe,ZWE,1970,5175618\n" + \
                "Zimbabwe,ZWE,1971,5351195\n" + \
                "Zimbabwe,ZWE,1972,5535874\n" + \
                "Zimbabwe,ZWE,1973,5727044\n" + \
                "Zimbabwe,ZWE,1974,5920943\n" + \
                "Zimbabwe,ZWE,1975,6115370\n" + \
                "Zimbabwe,ZWE,1976,6308300\n" + \
                "Zimbabwe,ZWE,1977,6501893\n" + \
                "Zimbabwe,ZWE,1978,6703182\n" + \
                "Zimbabwe,ZWE,1979,6921790\n" + \
                "Zimbabwe,ZWE,1980,7164172\n" + \
                "Zimbabwe,ZWE,1981,7431940\n" + \
                "Zimbabwe,ZWE,1982,7721536\n" + \
                "Zimbabwe,ZWE,1983,8027565\n" + \
                "Zimbabwe,ZWE,1984,8342195\n" + \
                "Zimbabwe,ZWE,1985,8658857\n" + \
                "Zimbabwe,ZWE,1986,8976205\n" + \
                "Zimbabwe,ZWE,1987,9293283\n" + \
                "Zimbabwe,ZWE,1988,9604302\n" + \
                "Zimbabwe,ZWE,1989,9902540\n" + \
                "Zimbabwe,ZWE,1990,10183113\n" + \
                "Zimbabwe,ZWE,1991,10443043\n" + \
                "Zimbabwe,ZWE,1992,10682868\n" + \
                "Zimbabwe,ZWE,1993,10905756\n" + \
                "Zimbabwe,ZWE,1994,11116948\n" + \
                "Zimbabwe,ZWE,1995,11320346\n" + \
                "Zimbabwe,ZWE,1996,11518262\n" + \
                "Zimbabwe,ZWE,1997,11709997\n" + \
                "Zimbabwe,ZWE,1998,11893272\n" + \
                "Zimbabwe,ZWE,1999,12064537\n" + \
                "Zimbabwe,ZWE,2000,12222251\n" + \
                "Zimbabwe,ZWE,2001,12366165\n" + \
                "Zimbabwe,ZWE,2002,12500525\n" + \
                "Zimbabwe,ZWE,2003,12633897\n" + \
                "Zimbabwe,ZWE,2004,12777511\n" + \
                "Zimbabwe,ZWE,2005,12940032\n" + \
                "Zimbabwe,ZWE,2006,13124267\n" + \
                "Zimbabwe,ZWE,2007,13329909\n" + \
                "Zimbabwe,ZWE,2008,13558469\n" + \
                "Zimbabwe,ZWE,2009,13810599\n" + \
                "Zimbabwe,ZWE,2010,14086317\n" + \
                "Zimbabwe,ZWE,2011,14386649\n" + \
                "Zimbabwe,ZWE,2012,14710826\n" + \
                "Zimbabwe,ZWE,2013,15054506\n" + \
                "Zimbabwe,ZWE,2014,15411675\n" + \
                "Zimbabwe,ZWE,2015,15777451\n" + \
                "Zimbabwe,ZWE,2016,16150362\n" 
        pobTest=pob_test.splitlines()
        pobZimbawe=self.pob.getPoblacion("ZWE")   
        self.assertEqual(pobTest,pobZimbawe)
        
    def test_paises_distintos(self):
        paises={'YEM', 'AND', 'UMC', 'ECA', 'MAR', 'COD', 'GRD', 'MUS', 'NRU', 'NOR', 'PRY', 'LCA', 'GBR', 'MNP', 'EMU', 'LUX', 'AGO', 'JAM', 'VIR', 'IDN', 'GNB', 'JOR', 'SAU', 'IBT', 'GRC', 'GTM', 'BMU', 'EAP', 'KHM', 'BDI', 'GEO', 'CHN', 'PHL', 'BRB', 'PAK', 'VUT', 'KEN', 'TMN', 'GIN', 'EAR', 'CHE', 'STP', 'SSD', 'BRA', 'NAM', 'TTO', 'PSE', 'OED', 'HND', 'IRQ', 'GIB', 'NGA', 'FRA', 'BOL', 'URY', 'LTE', 'CRI', 'XKX', 'PER', 'PLW', 'MLT', 'BLZ', 'PAN', 'CYP', 'WSM', 'IND', 'PRK', 'MNE', 'MMR', 'CYM', 'PST', 'USA', 'IDB', 'OMN', 'DMA', 'PRE', 'KNA', 'ARM', 'BTN', 'HRV', 'LBR', 'LAO', 'MRT', 'HPC', 'CUW', 'RUS', 'MNA', 'LAC', 'HIC', 'KAZ', 'OSS', 'BHS', 'ESP', 'TUN', 'LMY', 'IRN', 'AZE', 'ERI', 'BEL', 'MAF', 'SLV', 'NLD', 'SSA', 'DNK', 'NPL', 'LIC', 'VNM', 'VEN', 'BGR', 'NAC', 'SLB', 'SAS', 'SXM', 'SUR', 'MDG', 'QAT', 'WLD', 'BEN', 'EUU', 'THA', 'BHR', 'COM', 'HUN', 'EAS', 'UKR', 'LBY', 'RWA', 'CAN', 'CHL', 'CSS', 'SOM', 'TUR', 'CIV', 'TEA', 'ABW', 'FCS', 'BGD', 'EST', 'TLA', 'DZA', 'LCN', 'MOZ', 'COL', 'VCT', 'ZMB', 'MYS', 'PSS', 'SRB', 'CEB', 'IBD', 'ARB', 'KGZ', 'MLI', 'SVK', 'GUY', 'DJI', 'FIN', 'KIR', 'VGB', 'IDX', 'FJI', 'POL', 'IDA', 'ITA', 'AFG', 'KWT', 'NZL', 'PNG', 'ATG', 'LBN', 'GHA', 'CAF', 'ARE', 'TLS', 'SWZ', 'ZAF', 'CUB', 'BIH', 'MEX', 'TGO', 'TEC', 'TON', 'ETH', 'SST', 'EGY', 'SYC', 'SMR', 'AUS', 'BRN', 'IRL', 'GUM', 'KOR', 'BFA', 'SSF', 'BWA', 'HKG', 'LTU', 'MNG', 'CPV', 'MHL', 'IMN', 'TCA', 'TCD', 'ALB', 'ISL', 'LMC', 'GNQ', 'ECS', 'MWI', 'SYR', 'TZA', 'TUV', 'LVA', 'MIC', 'TKM', 'SEN', 'AUT', 'GAB', 'SVN', 'SWE', 'GMB', 'CZE', 'SLE', 'ARG', 'MKD', 'ECU', 'MCO', 'ASM', 'HTI', 'CMR', 'TSA', 'DEU', 'BLR', 'FRO', 'LSO', 'LKA', 'PRT', 'UZB', 'NER', 'MAC', 'DOM', 'SGP', 'TSS', 'FSM', 'NCL', 'ROU', 'MEA', 'UGA', 'PRI', 'CHI', 'MDV', 'GRL', 'SDN', 'LDC', 'PYF', 'TJK', 'JPN', 'MDA', 'ISR', 'LIE', 'NIC', 'ZWE'}
        print ("Paises"+str(self.pob.getPaises()))
        self.assertEqual(paises,self.pob.getPaises())

    def test_hay_datos_Spain(self):
        hayDatos=self.pob.hayDatos('ESP')
        self.assertEqual(True,hayDatos)
     
    
    def test_no_hay_datos_BLX(self):
        hayDatos=self.pob.hayDatos('BLX')
        self.assertEqual(False,hayDatos)
     
    def test_n_paises(self):
        self.assertEqual(262,self.pob.getNPaises())