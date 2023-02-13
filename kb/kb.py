import traceback
import pandas as pd
from os import path, remove
from sys import argv

#filmtv_id,titolo_originale,anno,genere,durata,paese,registi,attori,voto_medio,humor,ritmo,impegno,tensione,erotismo,cluster

class KnowledgeBase:
    s=["anno","genere","durata","paese","registi","attori","voto_medio","humor","ritmo","impegno","tensione","erotismo","cluster"]

    def __init__(self,dataframe):
        self.dataframe = dataframe
        if path.exists('.\datasets\kb.pl'):
            remove('.\datasets\kb.pl')
        self.kbPath = '.\datasets\kb.pl'

    def KbCreation(self,max=-1):

        #definizione degli assiomi della kb

        file = open(self.kbPath, "a")
        pd.set_option('display.max_rows', 1000)

        print("Creating Knowledge Base...")
        features = self.dataframe.columns
        for i in range(0, len(features)):
            try:
                for row in self.dataframe.iterrows():
                    value = row[1]
                    if features[i] == 'filmtv_id':
                        file.write('filmtv_id(' + str(value["filmtv_id"]) + ').\n')
                    elif features[i] == "titolo_originale":
                        file.write('titolo(' + str(value["titolo_originale"]) + ').\n')
                    elif features[i] == "anno":
                        file.write('anno(' + str(value["anno"]) + ').\n')
                    elif features[i] == "genere":
                        file.write('genere(' + str(value["genere"]) + ').\n')
                    elif features[i] == "durata":
                        file.write('durata(' + str(value["durata"]) + ').\n')
                    elif features[i] == "paese":
                        file.write('paese(' + str(value["paese"]) + ').\n')
                    elif features[i] == "registi":
                        file.write('registi(' + str(value["registi"]) + ').\n')
                    elif features[i] == "attori":
                        file.write('attori(' + str(value["attori"]) + ').\n')
                    elif features[i] == "voto_medio":
                        file.write('voto_medio(' + str(value["voto_medio"]) + ').\n')
                    elif features[i] == "humor":
                        file.write('humor(' + str(value["humor"]) + ').\n')
                    elif features[i] == "ritmo":
                        file.write('ritmo(' + str(value["ritmo"]) + ').\n')
                    elif features[i] == "impegno":
                        file.write('impegno(' + str(value["impegno"]) + ').\n')
                    elif features[i] == "tensione":
                        file.write('tensione(' + str(value["tensione"]) + ').\n')
                    elif features[i] == "erotismo":
                        file.write('erotismo(' + str(value["erotismo"]) + ').\n')
                    elif features[i] == "cluster":
                        file.write('cluster(' + str(value["cluster"]) + ').\n')

            except Exception as e:
             print("Exception " +  str(e))

        try:
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('id_titolo(' + str(value["titolo_originale"]) + ',' + str(value["filmtv_id"])+ ').\n')
            for p in self.dataframe.iterrows():
                 value = p[1]
                 file.write('anno_titolo(' + str(value["titolo_originale"]) + ',' + str(value["anno"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('genere_titolo(' + str(value["titolo_originale"]) + ',' + str(value["genere"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('durata_titolo(' + str(value["titolo_originale"]) + ',' + str(value["durata"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('registi_titolo(' + str(value["titolo_originale"]) + ',' + str(value["registi"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('attori_titolo(' + str(value["titolo_originale"]) + ',' + str(value["attori"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('humor_titolo(' + str(value["titolo_originale"]) + ',' + str(value["humor"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('ritmo_titolo(' + str(value["titolo_originale"]) + ',' + str(value["ritmo"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('impegno_titolo(' + str(value["titolo_originale"]) + ',' + str(value["impegno"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('tensione_titolo(' + str(value["titolo_originale"]) + ',' + str(value["tensione"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('erotismo_titolo(' + str(value["titolo_originale"]) + ',' + str(value["erotismo"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('cluster_titolo(' + str(value["titolo_originale"]) + ',' + str(value["cluster"]) + ').\n')
            for p in self.dataframe.iterrows():
                value = p[1]
                file.write('voto_titolo(' + str(value["titolo_originale"]) + ',' + str(value["voto_medio"]) + ').\n')

        except Exception as e:
              print("Exception " + str(e))
              file.close()

    def RulesCreation(self):
        # creazione delle regole all'interno della base di conoscenza

        file = open(self.kbPath, "a")
        print('Creating Rules...')
        #regole basate su cluster
        file.write('film_simili(X,Y) :- cluster_titolo(X,C), cluster_titolo(Y,D), C = D.\n')

        file.write('attori_registi_work(X,Y) :- attori_titolo(Z,X) ,registi_titolo(Z,Y) .\n')
        file.write('registi_attori_work(X,Y) :- registi_titolo(Z,X) ,attori_titolo(Z,Y) .\n')

        file.write('film_stesso_anno(X,Y) :- durata_titolo(Z,X) ,durata_titolo(Z,Y) .\n')

        file.write('film_stesso_genere(X,Y) :- genere_titolo(Z,X) ,genere_titolo(Z,Y) .\n')

        file.write('film_stesso_paese(X,Y) :- paese_titolo(Z,X) ,paese_titolo(Z,Y) .\n')










        file.close()
def main():
    try:
        dataframe = pd.read_csv(argv[1])
        kb = KnowledgeBase(dataframe)
        kb.KbCreation()
        kb.RulesCreation()
        print("Knowledge Base done.")
    except FileNotFoundError as e:
        print("Error file" + e)
main()