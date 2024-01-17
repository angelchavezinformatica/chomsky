from core import Chomsky, Grammar
from core.types import GrammarType


def print_grammar(grammar: GrammarType):
    for key, value in grammar.items():
        print(f"\t{key} → {' | '.join(value)}")


def chomsky_normal_form(grammar: GrammarType, first_non_terminal: str):
    ch = Chomsky()
    print('GRAMMAR:')
    print_grammar(grammar)
    print("\n1. Limpiar la gramática")
    print("1.1. Eliminar producciones-ε")
    grammar, nullable = ch.remove_epsilon_productions(grammar=Grammar(
        grammar=grammar,
        first_non_terminal=first_non_terminal))
    print("\tAnulable:", nullable, '\n')
    print_grammar(grammar=grammar)

    print("\n1.2. Eliminar producciones unitarias de la forma X → Y")
    grammar, unit_productions = ch.remove_unit_productions(grammar=Grammar(
        grammar=grammar,
        first_non_terminal=first_non_terminal))
    for unit_key, unit_value in unit_productions.items():
        print(f"\tUnitario({unit_key}):", unit_value)
    print()
    print_grammar(grammar=grammar)
    input("continuar...")

    print("\n1.3. Eliminar producciones no útiles")
    print("1.3.1. Quitar variables no generadoras")
    grammar, generators = ch.remove_non_generators(grammar=Grammar(
        grammar=grammar,
        first_non_terminal=first_non_terminal))
    print("\tGeneradores:", generators, '\n')
    print_grammar(grammar=grammar)

    input("continuar...")

    print("\n1.3.2. Quitar variables no alcanzables")
    grammar, reachables = ch.remove_non_reachables(grammar=Grammar(
        grammar=grammar,
        first_non_terminal=first_non_terminal))
    print("\tAlcanzables:", reachables, '\n')
    print_grammar(grammar=grammar)
    input("continuar...")

    print("\n2. Eliminar el lado derecho mixto")
    grammar = ch.remove_mixed_right_hand_side(grammar=Grammar(
        grammar=grammar,
        first_non_terminal=first_non_terminal))
    gr = ch.format_grammar(grammar=Grammar(
        grammar=grammar,
        first_non_terminal=first_non_terminal))
    print_grammar(grammar=gr)
    input("continuar...")

    print("\n3. Factorizar producciones largas")
    grammar = ch.factorize_long_productions(grammar=Grammar(
        grammar=grammar,
        first_non_terminal=first_non_terminal))
    gr = ch.format_grammar(grammar=Grammar(
        grammar=grammar,
        first_non_terminal=first_non_terminal))
    print_grammar(grammar=gr)
