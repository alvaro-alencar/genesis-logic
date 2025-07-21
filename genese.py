# genese.py

from entidade import EntidadeLogica
import time

def run_genese(max_entidades=7):
    """
    Executa a simulação do nascimento da lógica a partir do Vazio.
    """
    
    universo = []
    
    print("--- INÍCIO DA GÊNESE LÓGICA ---")
    print("Universo: []\n")
    time.sleep(2)

    # --- O PRIMEIRO INSTANTE: O VAZIO ---
    # A primeira entidade é o Vazio. Ela não percebe nada, pois nada existe.
    entidade_0 = EntidadeLogica(id=0, percepcoes=[])
    universo.append(entidade_0)
    print(f"PASSO 0: O Vazio (0) emerge. Ele é definido pela ausência de percepção.")
    print(f"Universo: {universo}\n")
    time.sleep(3)

    # --- OS PRÓXIMOS INSTANTES: A CASCATA DA OBSERVAÇÃO ---
    for i in range(1, max_entidades):
        # A nova entidade que nasce é o OBSERVADOR de tudo o que existia antes.
        # Sua percepção é o estado completo do universo no instante anterior.
        percepcoes_da_nova_entidade = list(universo)
        
        nova_entidade = EntidadeLogica(id=i, percepcoes=percepcoes_da_nova_entidade)
        universo.append(nova_entidade)

        print(f"PASSO {i}: A Entidade {i} emerge.")
        if i == 1:
            print("   Ela é a percepção do Vazio. O Vazio, ao ser percebido, torna-se Unidade (1).")
        elif i == 2:
            print("   Ela é a percepção da relação entre o Vazio (0) e a Unidade (1). Ela é a Distinção (2).")
        elif i == 3:
            print("   Ela é a percepção da Tríade (0, 1, 2). O sistema se torna consciente de sua própria estrutura. O 3 eclode.")
        else:
            print(f"   Ela é a percepção do conjunto de todas as entidades anteriores: {i-1}.")
        
        print(f"Universo: {universo}\n")
        time.sleep(3)

if __name__ == "__main__":
    run_genese()