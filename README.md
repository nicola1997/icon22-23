# Progetto Ingegneria della conoscenza A.A. 2022-2023 

**Gruppo di lavoro**

-	Nicola Dipinto, 729920, n.dipinto8@studenti.uniba.it 
- Andrea Biasco, 744605, a.biasco3@studenti.uniba.it 

# FASE INIZIALE

**Installare SWIProlog** (installare la versione a 64 bit) 

https://www.swi-prolog.org/download/stable/bin/swipl-8.2.4-1.x64.exe.envelope 

**Clonare il repository dal prompt dei comandi:**

 git clone https://github.com/nicola1997/progetto-icon22-23.git 

**Creare l'ambiente virtuale:** 

 cd progetto-icon22-23 

 python -m venv progetto-icon22-23 

**Installare le dipendenze:** 

 pip install -r requirements.txt 

# Esecuzione del codice 
**Preprocessing:** 

 python preprocessing\cleaning_datasets.py datasets\filmtv.csv 

**Creazione dei cluster:**

 python clustering\clustering.py datasets\dataset_clustering.csv [n_cluster] [n_iter]

**Creazione Knowledge Base:**

 python kb\kb.py datasets\dataset_prolog.csv
 **Creazione Belief Network:**

 python bn/ui.py 

 

