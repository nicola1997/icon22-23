import re
from sys import argv
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from unidecode import unidecode

#filmtv_id,titolo_originale,anno,genere,durata,paese,registi,attori,voto_medio,+5
def cleaning_dataset(dataframe):
    print("Pulizia generale dataframe...") #humor,ritmo,impegno,tensione,erotismo
    try:
     dataframe=dataframe.drop(["titolo_italiano",'voto_critica','voto_pubblico','voti_totali','descrizione','note'],axis=1)
     dataframe = dataframe.drop_duplicates(subset=['filmtv_id'])
     dataframe = dataframe.drop_duplicates(subset=['titolo_originale'])
     dataframe = dataframe[~((dataframe['humor'].astype(str).str.contains("0")) & (dataframe['ritmo'].astype(str).str.contains("0"))
                      & (dataframe['impegno'].astype(str).str.contains("0"))& (dataframe['tensione'].astype(str).str.contains("0"))
                      & (dataframe['erotismo'].astype(str).str.contains("0")))]

     dataframe = dataframe.dropna()
     #titolo_originale
     dataframe["paese"]=dataframe["paese"].apply(lambda x: re.sub("[','][\s+\S]+",'',x))
     dataframe["registi"]=dataframe["registi"].apply(lambda x: re.sub("[','][\s+\S]+",'',x))
     dataframe["attori"]=dataframe["attori"].apply(lambda x: re.sub("[','][\s+\S]+",'',x))

     dataframe["titolo_originale"] = dataframe["titolo_originale"].apply(lambda x: unidecode(x))
     dataframe["paese"] = dataframe["paese"].apply(lambda x: unidecode(x))
     dataframe["registi"] = dataframe["registi"].apply(lambda x: unidecode(x))
     dataframe["attori"] = dataframe["attori"].apply(lambda x: unidecode(x))
     dataframe["genere"] = dataframe["genere"].apply(lambda x: unidecode(x))

     dataframe["titolo_originale"] = dataframe["titolo_originale"].str.lower()
     dataframe["attori"] = dataframe["attori"].str.lower()
     dataframe["genere"] = dataframe["genere"].str.lower()
     dataframe["paese"] = dataframe["paese"].str.lower()
     dataframe["registi"] = dataframe["registi"].str.lower()


     dataframe["titolo_originale"]=dataframe["titolo_originale"].apply(lambda x: re.sub(" ", "_", x)) #sostituisce gli spazi con _
     dataframe["paese"]=dataframe["paese"].apply(lambda x: re.sub(" ", "_", x)) #sostituisce gli spazi con _
     dataframe["registi"]=dataframe["registi"].apply(lambda x: re.sub(" ", "_", x)) #sostituisce gli spazi con _
     dataframe["attori"]=dataframe["attori"].apply(lambda x: re.sub(" ", "_", x)) #sostituisce gli spazi con _




     #cancello caratteri speciali
     dataframe["titolo_originale"] = dataframe["titolo_originale"].apply(lambda x: re.sub("\W", "", x))
     dataframe["paese"] = dataframe["paese"].apply(lambda x: re.sub("\W", "", x))
     dataframe["registi"] = dataframe["registi"].apply(lambda x: re.sub("\W", "", x))
     dataframe["attori"] = dataframe["attori"].apply(lambda x: re.sub("\W", "", x))

     #sostituisco numeri
     dataframe["titolo_originale"] = dataframe["titolo_originale"].apply(lambda x: re.sub("\d", "", x))
     dataframe["paese"] = dataframe["paese"].apply(lambda x: re.sub("\d", "", x))
     dataframe["registi"] = dataframe["registi"].apply(lambda x: re.sub("\d", "", x))
     dataframe["attori"] = dataframe["attori"].apply(lambda x: re.sub("\d", "", x))

     dataframe["titolo_originale"] = dataframe["titolo_originale"].apply(
         lambda x: re.sub("\A_*", "", x))  # cancella solo i primi _
     dataframe["paese"] = dataframe["paese"].apply(lambda x: re.sub("\A_*", "", x))
     dataframe["registi"] = dataframe["registi"].apply(lambda x: re.sub("\A_*", "", x))
     dataframe["attori"] = dataframe["attori"].apply(lambda x: re.sub("\A_*", "", x))

     dataframe = dataframe.dropna()
     dataframe = dataframe.drop_duplicates(subset=['titolo_originale'])

    except:
     print("Errore,file aperto oppure file.csv o colonna non trovata.")

    return dataframe

def clustering_preprocessing(dataframe):
    dataframe['0'] = dataframe['genere'].astype('category').cat.codes
    dataframe['1'] = dataframe['durata'].astype('category').cat.codes
    dataframe['2'] = dataframe['paese'].astype('category').cat.codes
    dataframe['3'] = dataframe['anno'].astype('category').cat.codes
    dataframe['4'] = dataframe['humor'].astype('category').cat.codes
    dataframe['5'] = dataframe['ritmo'].astype('category').cat.codes
    dataframe['6'] = dataframe['impegno'].astype('category').cat.codes ######################à
    dataframe['7'] = dataframe['tensione'].astype('category').cat.codes
    dataframe['8'] = dataframe['erotismo'].astype('category').cat.codes


    dataframe = dataframe.drop(['titolo_originale','genere','paese','registi','attori'
    ,'filmtv_id',"voto_medio"], axis=1)

    pca = PCA(n_components=9)
    pca.fit(dataframe)
    features = pca.transform(dataframe)
    dataframe = pd.DataFrame(features)
    scaler = MinMaxScaler()
    dataframe = pd.DataFrame(scaler.fit_transform(dataframe), columns=dataframe.columns)
    #dataframe[0].round(10)


    return dataframe
def main():
    data=pd.read_csv(argv[1])
    #creazione cleaned_dataset e dataset_prolog
    print("Iniziando pre processing...")
    dataset_cleaned=cleaning_dataset(data)
    dataset_cleaned.to_csv(".\datasets\cleaned_dataset.csv",index = False)
    dataset_cleaned.to_csv(".\datasets\dataset_prolog.csv",index = False)



    dataframe_clustering=clustering_preprocessing(dataset_cleaned)
    dataframe_clustering.to_csv(".\datasets\dataset_clustering.csv", index=False)

main()