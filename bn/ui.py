import pyswip as psw
import pandas as pd
from pgmpy.models import  BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

prg = psw.Prolog()

def correct_input(a):
    command = input().lower().strip()
    while(command != a[0] and command != a[1]):
        print("Wrong command,you can insert ",a)
        command = input().lower().strip()
    return command
def dropping(answer):
    """
    :param answer:indica una query da eseguire sulla KB, sotto forma di lista
    :return: dataframe con le risposte esatte per quella query
    """
    dataframe = pd.DataFrame(answer)
    canc = set()
    for index, row in dataframe.iterrows():
        for col in dataframe.columns:
            if isinstance(row[col], psw.Variable):
                canc.add(index)
                break
    dataframe.drop(index=canc, inplace=True)
    return dataframe
def kbquery():
    """
    Funzione per la gestione e la stampa delle query della kb
    """
    try:
        # vera [{}], false[],  risposte [{X:...}]
        print("Insert a query for KnowledgeBase:")
        query = input()
        answer = prg.query(query)
        answer_list = list(answer)
        if len(answer_list) == 0:
            print("false")
        elif len(answer_list) == 1 and len(answer_list[0]) == 0:
            print("true")
        else:
            dataframe = dropping(answer_list)
            print("Answer:\n")
            print(dataframe)

    except Exception as e:
        print("Error" + str(e))
def help():
    #help generale per l'utente
    print("This is a list of command:")
    print("'help' to print the list of commands")
    print("'query' to insert a query in KB")
    print("'inference' to do inference with Belief Network")
    print("'quit' to exit\n")
def bn():

    #P(voto|genere)
    #P(voto|paese)
    #P(voto|anno)
    #P(voto|durata)
    #P(genere|erotismo)
    #P(genere|tensione)
    #P(genere|impegno)
    #P(genere|ritmo)
    #P(genere|humor)
    df = pd.read_csv(r'datasets\bn_dataset.csv')

    # crea la struttura della rete bayesiana
    model = BayesianNetwork([('genere', 'class_of_erotismo'),('genere', 'class_of_tensione'),
                             ('genere', 'class_of_impegno'),('genere', 'class_of_ritmo'),('genere', 'class_of_humor'),
                             ])
    # addestra la rete bayesiana
    model.fit(df, estimator=MaximumLikelihoodEstimator)

    inference = VariableElimination(model)
    prob = inference.query(variables=['genere'], evidence={'class_of_humor': "good_rating" })
    print(prob)


def BNetwork_query():
    bn()

def main():
    print("Loading knowledge base...")
    prg.consult("./datasets/kb.pl")
    pd.set_option('display.max_rows', 3000, 'display.max_columns', 10)
    help()
    while (True):
        print("Insert command:")
        command = input()
        command = command.strip().lower()
        if command == 'quit':
            break
        elif command == 'help':
            help()
        elif command == 'query':
            while(True):
                kbquery()
                print("Do you want to insert another query? [yes,no]")
                cont = correct_input(['yes', 'no'])
                if cont == 'no':
                    break
        elif command == 'inference':
            BNetwork_query()
        else:
            print("Wrong command")
            help()

main()
