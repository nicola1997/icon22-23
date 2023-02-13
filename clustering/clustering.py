from sys import argv
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

def discretizzazione_voto(dataset):
    votoIntervalli = [
        (dataset['voto_medio'] <= 4),
        (dataset['voto_medio'] <= 7) & (dataset['voto_medio'] > 4),
        (dataset['voto_medio'] <= 9) & (dataset['voto_medio'] > 7),
         (dataset['voto_medio'] > 9)
    ]
    voto_range = ['low_rating','good_rating','nice_rating','top_rating']
    to_insert = np.select(votoIntervalli, voto_range)
    dataset.insert(0, 'class_of_voto', to_insert)
    dataset = dataset.astype({'class_of_voto': 'category'})
    dataset.drop('voto_medio', axis=1, inplace=True)
    return dataset
def discretizzazione_anno(dataset):
    annoIntervalli = [
        (dataset['anno'] <= 1939),
        (dataset['anno'] <= 1967) & (dataset['anno'] > 1939),
        (dataset['anno'] <= 1995) & (dataset['anno'] > 1967),
         (dataset['anno'] > 1995)
    ]
    anno_range = ['piu vecchio', 'vecchio', 'nuovo', 'piu nuovo']
    to_insert = np.select(annoIntervalli, anno_range)
    dataset.insert(0, 'class_of_year', to_insert)
    dataset = dataset.astype({'class_of_year': 'category'})
    dataset.drop('anno', axis=1, inplace=True)
    return dataset

def discretizzazione_durata(dataset):
    durataIntervalli = [
        (dataset['durata'] <= 75),
        (dataset['durata'] <= 120) & (dataset['durata'] > 75),
        (dataset['durata'] <= 230) & (dataset['durata'] > 120),
        (dataset['durata'] > 230)]

    durata_range = ['cortometraggio', 'durataMedia', 'DurataLunga', 'DurataMoltoLunga']
    to_insert = np.select(durataIntervalli, durata_range)
    dataset.insert(0, 'class_of_time', to_insert)
    dataset = dataset.astype({'class_of_time': 'category'})
    dataset.drop('durata', axis=1, inplace=True)
    return dataset
def discretizzazione_hrite(dataset):
    #humor
    humorIntervalli = [
        (dataset['humor'] == 0),
        (dataset['humor'] == 1),
        (dataset['humor'] == 2),
        (dataset['humor'] == 3),
        (dataset['humor'] == 4),
        (dataset['humor'] == 5)]

    humor_range = ['null','low_rating','good_rating','nice_rating','top_rating','super_rating']
    to_insert = np.select(humorIntervalli, humor_range)
    dataset.insert(0, 'class_of_humor', to_insert)
    dataset = dataset.astype({'class_of_humor': 'category'})
    dataset.drop('humor', axis=1, inplace=True)
    ###ritmo
    ritmoIntervalli = [
        (dataset['ritmo'] == 0),
        (dataset['ritmo'] == 1),
        (dataset['ritmo'] == 2),
        (dataset['ritmo'] == 3),
        (dataset['ritmo'] == 4),
        (dataset['ritmo'] == 5)]

    ritmo_range = ['null','low_rating', 'good_rating', 'nice_rating', 'top_rating','super_rating']
    to_insert = np.select(ritmoIntervalli, ritmo_range)
    dataset.insert(0, 'class_of_ritmo', to_insert)
    dataset = dataset.astype({'class_of_ritmo': 'category'})
    dataset.drop('ritmo', axis=1, inplace=True)

    ###impegno
    impegnoIntervalli = [
        (dataset['impegno'] == 0),
        (dataset['impegno'] == 1),
        (dataset['impegno'] == 2),
        (dataset['impegno'] == 3),
        (dataset['impegno'] == 4),
        (dataset['impegno'] == 5)]

    impegno_range = ['null', 'low_rating', 'good_rating', 'nice_rating', 'top_rating','super_rating']
    to_insert = np.select(impegnoIntervalli, impegno_range)
    dataset.insert(0, 'class_of_impegno', to_insert)
    dataset = dataset.astype({'class_of_impegno': 'category'})
    dataset.drop('impegno', axis=1, inplace=True)

    ###tensione
    tensioneIntervalli = [
        (dataset['tensione'] == 0),
        (dataset['tensione'] == 1),
        (dataset['tensione'] == 2),
        (dataset['tensione'] == 3),
        (dataset['tensione'] == 4),
        (dataset['tensione'] == 5)]

    tensione_range = ['null', 'low_rating', 'good_rating', 'nice_rating', 'top_rating','super_rating']
    to_insert = np.select(tensioneIntervalli, tensione_range)
    dataset.insert(0, 'class_of_tensione', to_insert)
    dataset = dataset.astype({'class_of_tensione': 'category'})
    dataset.drop('tensione', axis=1, inplace=True)
    ###erotismo
    erotismoIntervalli = [
        (dataset['erotismo'] == 0),
        (dataset['erotismo'] == 1),
        (dataset['erotismo'] == 2),
        (dataset['erotismo'] == 3),
        (dataset['erotismo'] == 4),
        (dataset['erotismo'] == 5)]

    erotismo_range = ['null', 'low_rating', 'good_rating', 'nice_rating', 'top_rating','super_rating']
    to_insert = np.select(erotismoIntervalli, erotismo_range)
    dataset.insert(0, 'class_of_erotismo', to_insert)
    dataset = dataset.astype({'class_of_erotismo': 'category'})
    dataset.drop('erotismo', axis=1, inplace=True)

    return dataset


def k_cluster(dataframe,k,max):
    """
    :param dataframe: dataframe con le features da utilizzare per il clustering
    :param k: numero di cluster
    :param max_it: numero massimo di iterate
    :return: i cluster crati
    """
    print("Creating clusters...")
    km = KMeans(n_clusters=k,max_iter=max)
    clusters = km.fit_predict(dataframe)
    return clusters
def elbow_plot(dataframe, it):
    distortions = []
    for i in range(1, it):
        km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300, random_state=0)
        km.fit(dataframe)
        distortions.append(km.inertia_)

    plt.plot(range(1,it), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.show()
def plot_durata_voto(df):
  # Carica il dataset di film
 film_dataset = df

 # Seleziona le colonne "durata" e "voto_medio" per la visualizzazione
 x = film_dataset["durata"]
 y = film_dataset["voto_medio"]

 # Crea il plot scatter
 plt.scatter(x, y)

 # Aggiungi un titolo e le etichette degli assi
 plt.title("Relazione tra durata e voto medio dei film")
 plt.xlabel("Durata (minuti)")
 plt.ylabel("Voto medio")

 # Mostra il plot
 plt.show()
def plot_genere_voto(df):
    # Carica il dataset di film
    film_dataset = df

    # Seleziona le colonne "genere" e "voto_medio" per la visualizzazione
    x = film_dataset["genere"]
    y = film_dataset["voto_medio"]

    # Crea il plot scatter
    plt.scatter(x, y)

    # Aggiungi un titolo e le etichette degli assi
    plt.title("Relazione tra genere e voto medio dei film")
    plt.xlabel("genere")
    plt.ylabel("Voto medio")

    # Mostra il plot
    plt.show()
def plot_paese_voto(df):
    # Carica il dataset di film
    film_dataset = df

    # Seleziona le colonne "paese" e "voto_medio" per la visualizzazione
    x = film_dataset["paese"]
    y = film_dataset["voto_medio"]

    # Crea il plot scatter
    plt.scatter(x, y)

    # Aggiungi un titolo e le etichette degli assi
    plt.title("Relazione tra paese e voto medio dei film")
    plt.xlabel("paese")
    plt.ylabel("Voto medio")

    # Mostra il plot
    plt.show()
def plot_anno_voto(df):
    # Carica il dataset di film
    film_dataset = df

    # Seleziona le colonne "anno" e "voto_medio" per la visualizzazione
    x = film_dataset["anno"]
    y = film_dataset["voto_medio"]

    # Crea il plot scatter
    plt.scatter(x, y)

    # Aggiungi un titolo e le etichette degli assi
    plt.title("Relazione tra anno e voto medio dei film")
    plt.xlabel("anno")
    plt.ylabel("Voto medio")

    # Mostra il plot
    plt.show()
def main():
    try:
        dataframe = pd.read_csv(argv[1])
        k = int(argv[2])  # number of cluster
        it = int(argv[3]) # number of iterations
        clusters = k_cluster(dataframe, k, it)
        df_prolog = pd.read_csv('./datasets/dataset_prolog.csv')
        df_prolog['cluster'] = clusters
        df_prolog.to_csv('./datasets/dataset_prolog.csv',index = False)

        #creazione bn dataset dicretizzato
        bn_dataset=pd.read_csv('./datasets/dataset_prolog.csv')
        bn_dataset=discretizzazione_voto(bn_dataset)
        bn_dataset=discretizzazione_anno(bn_dataset)
        bn_dataset=discretizzazione_durata(bn_dataset)
        bn_dataset=discretizzazione_hrite(bn_dataset)
        bn_dataset=bn_dataset.drop(['registi','attori','filmtv_id','titolo_originale'],axis=1)
        bn_dataset.to_csv('./datasets/bn_dataset.csv',index=False)

        #df = pd.read_csv(r"C:\Users\ndipi\Desktop\progetto-icon22-23\datasets\dataset_clustering.csv")
        #elbow_plot(df, 100) #10 min
        print("Clustering Done.")
        #df=pd.read_csv('./datasets/dataset_prolog.csv')
        #plot_durata_voto(df_prolog)
        #plot_genere_voto(df_prolog)
        #plot_paese_voto(df_prolog)
        #plot_anno_voto(df_prolog)

    except FileNotFoundError as e:
        print("File not found",e)
    except Exception as e:
        print(e)

main()