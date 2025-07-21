import time
import os

class EntidadeMetafisica:
    """Uma entidade definida por seu estado e sua relação com outras."""
    def __init__(self, nome, estado_inicial, imovel=False):
        self.nome = nome
        self.estado = estado_inicial # O 'estado' aqui é a sua posição em uma linha vertical.
        self.imovel = imovel

    def __repr__(self):
        return f"{self.nome}({self.estado})"

def avaliar_dissonancia(universo):
    """
    A Função de Coerência Universal.
    Calcula a "tensão" total do universo. Neste modelo, a tensão é a
    distância total entre todas as entidades. Um universo mais compacto
    é mais coerente (menos dissonante).
    """
    dissonancia_total = 0
    # Calcula a distância entre cada par de entidades
    for i in range(len(universo)):
        for j in range(i + 1, len(universo)):
            distancia = abs(universo[i].estado - universo[j].estado)
            dissonancia_total += distancia
    return dissonancia_total

def run_metafisica(passos=15):
    """
    Simula a emergência de uma lei física a partir da busca pela coerência.
    """
    # Gênese: O universo nasce com duas entidades. O Chão é a nossa âncora.
    chao = EntidadeMetafisica(nome="Chão", estado_inicial=0, imovel=True)
    copo = EntidadeMetafisica(nome="Copo", estado_inicial=10)
    
    universo = [chao, copo]
    
    print("--- UNIVERSO INICIAL ---")
    print(f"Estado: {universo}")
    print(f"Dissonância Inicial: {avaliar_dissonancia(universo)}\n")
    print("--------------------------\n")
    time.sleep(3)

    for i in range(passos):
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
        print(f"--- AVALIANDO INSTANTE {i+1} ---")
        
        # Encontra o copo (a entidade que pode se mover)
        entidade_movel = next(e for e in universo if not e.imovel)
        estado_atual = entidade_movel.estado
        
        # Gera todos os futuros possíveis para este instante
        futuros_possiveis = {
            "subir": estado_atual + 1,
            "ficar parado": estado_atual,
            "descer": estado_atual - 1,
        }
        
        resultados = {}

        print(f"Estado Atual: {universo}")
        print("Analisando futuros possíveis...")

        # Avalia a coerência de cada futuro hipotético
        for nome_futuro, estado_futuro in futuros_possiveis.items():
            # Cria um universo hipotético para avaliação
            universo_hipotetico = [chao, EntidadeMetafisica(nome="Copo", estado_inicial=estado_futuro)]
            dissonancia = avaliar_dissonancia(universo_hipotetico)
            resultados[nome_futuro] = dissonancia
            print(f"  - Se o copo '{nome_futuro}', a dissonância do universo seria: {dissonancia}")

        # A Decisão do Universo: Escolher o futuro com a menor dissonância
        melhor_futuro = min(resultados, key=resultados.get)
        
        print(f"\nDECISÃO DO UNIVERSO: O estado de menor dissonância é '{melhor_futuro}'.")

        # Colapso da Função de Onda: O futuro escolhido se torna a nova realidade
        entidade_movel.estado = futuros_possiveis[melhor_futuro]
        
        print(f"\n--- NOVO ESTADO DO UNIVERSO ---")
        print(f"Estado: {universo}")
        print(f"Dissonância Atual: {avaliar_dissonancia(universo)}\n")
        print("--------------------------\n")

        # Se o copo chegou ao chão, a história termina.
        if entidade_movel.estado <= chao.estado + 1:
            print("EQUILÍBRIO ATINGIDO. O copo não pode se aproximar mais do chão sem violar sua existência.")
            break
            
        time.sleep(2)

if __name__ == "__main__":
    run_metafisica()