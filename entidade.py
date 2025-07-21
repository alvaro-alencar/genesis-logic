# entidade.py

class EntidadeLogica:
    """
    Representa uma entidade fundamental na gênese da lógica.
    Sua essência é definida pelo que ela é capaz de perceber.
    """
    _max_recursion_depth = 2 # Um limite para não sobrecarregar o console

    def __init__(self, id, percepcoes):
        self.id = id
        self.percebe = percepcoes

    def __repr__(self, level=0):
        # A nova representação recursiva
        if level > self._max_recursion_depth:
            return f"Entidade {self.id} (...)"
        
        # Constrói a string mostrando as percepções de forma aninhada
        percepcoes_str = ", ".join([e.__repr__(level + 1) for e in self.percebe])
        return f"Entidade {self.id} (Percebe: [{percepcoes_str}])"