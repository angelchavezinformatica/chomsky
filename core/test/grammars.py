grammars = [
    {
        'grammar': {
            'S': {'AB', 'bA', 'A'},
            'A': {'aAS', 'a', 'ε'},
            'B': {'SbB', 'AB', 'bB'}
        },
        'first-non-terminal': 'S',
        'steps': {
            1: {
                'nullable': {'A', 'S'},
                'grammar': {
                    'S': {'AB', 'bA', 'A', 'B', 'b'},
                    'A': {'aAS', 'a', 'aS', 'aA'},
                    'B': {'SbB', 'AB', 'bB', 'B'}
                }
            },
            2: {
                'units': {
                    'S': {'S', 'A', 'B'},
                    'A': {'A'},
                    'B': {'B'}
                },
                'grammar': {
                    'S': {'AB', 'bA', 'aAS', 'a', 'aS', 'aA', 'SbB', 'bB', 'b'},
                    'A': {'aAS', 'a', 'aS', 'aA'},
                    'B': {'SbB', 'AB', 'bB'}
                }
            },
            3: {
                'generators': {'S', 'A'},
                'grammar': {
                    'S': {'bA', 'aAS', 'a', 'aS', 'aA', 'b'},
                    'A': {'aAS', 'a', 'aS', 'aA'}
                }
            },
            4: {
                'reachables': {'S', 'A'},
                'grammar': {
                    'S': {'bA', 'aAS', 'a', 'aS', 'aA', 'b'},
                    'A': {'aAS', 'a', 'aS', 'aA'}
                }
            },
            5: {
                'grammar': {
                    'S': {'bA', 'aAS', 'a', 'aS', 'aA', 'b'},
                    'A': {'aAS', 'a', 'aS', 'aA'},
                    'Va': {'a'},
                    'Vb': {'b'}
                }
            },
            6: {
                'grammar': {
                    'S': {'bA', 'aX', 'a', 'aS', 'aA', 'b'},
                    'A': {'aX', 'a', 'aS', 'aA'},
                    'Va': {'a'},
                    'Vb': {'b'},
                    'X': {'AS'}
                }
            }
        }
    },
    {
        'grammar': {
            'S': {'A', 'AA', 'AAA'},
            'A': {'ABa', 'ACa', 'a'},
            'B': {'ABa', 'Ab', 'ε'},
            'C': {'Cab', 'CC'},
            'D': {'CD', 'Cd', 'CEa'},
            'E': {'b'}
        },
        'first-non-terminal': 'S',
        'steps': {
            1: {
                'nullable': {'B'},
                'grammar': {
                    'S': {'A', 'AA', 'AAA'},
                    'A': {'ABa', 'ACa', 'a', 'Aa'},
                    'B': {'ABa', 'Ab', 'Aa'},
                    'C': {'Cab', 'CC'},
                    'D': {'CD', 'Cd', 'CEa'},
                    'E': {'b'}
                }
            },
            2: {
                'units': {
                    'S': {'S', 'A'},
                    'A': {'A'},
                    'B': {'B'},
                    'C': {'C'},
                    'D': {'D'},
                    'E': {'E'}
                },
                'grammar': {
                    'S': {'ABa', 'ACa', 'a', 'Aa', 'AA', 'AAA'},
                    'A': {'ABa', 'ACa', 'a', 'Aa'},
                    'B': {'ABa', 'Ab', 'Aa'},
                    'C': {'Cab', 'CC'},
                    'D': {'CD', 'Cd', 'CEa'},
                    'E': {'b'}
                }
            },
            3: {
                'generators': {'S', 'A', 'E'},
                'grammar': {
                    'S': {'a', 'Aa', 'AA', 'AAA'},
                    'A': {'a', 'Aa'},
                    'E': {'b'}
                }
            },
            4: {
                'reachables': {'S', 'A'},
                'grammar': {
                    'S': {'a', 'Aa', 'AA', 'AAA'},
                    'A': {'a', 'Aa'}
                }
            },
            5: {
                'grammar': {
                    'S': {'a', 'Aa', 'AA', 'AAA'},
                    'A': {'a', 'Aa'},
                    'Va': {'a'}
                }
            },
            6: {
                'grammar': {
                    'S': {'a', 'Aa', 'AA', 'XA'},
                    'A': {'a', 'Aa'},
                    'Va': {'a'},
                    'X': {'AA'}
                }
            }
        }
    },
    {
        'grammar': {
            'R': {'bAA', 'a', 'b', 'bA'},
            'A': {'a', 'Rq', 'q'}
        },
        'first-non-terminal': 'R',
        'steps': {
            1: {
                'nullable': set(),
                'grammar': {
                    'R': {'bAA', 'a', 'b', 'bA'},
                    'A': {'a', 'Rq', 'q'}
                }
            },
            2: {
                'units': {
                    'R': {'R'},
                    'A': {'A'}
                },
                'grammar': {
                    'R': {'bAA', 'a', 'b', 'bA'},
                    'A': {'a', 'Rq', 'q'}
                }
            },
            3: {
                'generators': {'R', 'A'},
                'grammar': {
                    'R': {'bAA', 'a', 'b', 'bA'},
                    'A': {'a', 'Rq', 'q'}
                }
            },
            4: {
                'reachables': {'R', 'A'},
                'grammar': {
                    'R': {'bAA', 'a', 'b', 'bA'},
                    'A': {'a', 'Rq', 'q'}
                }
            },
            5: {
                'grammar': {
                    'R': {'bAA', 'a', 'b', 'bA'},
                    'A': {'a', 'Rq', 'q'},
                    'Vb': {'b'},
                    'Vq': {'q'}
                }
            },
            6: {
                'grammar': {
                    'R': {'bX', 'a', 'b', 'bA'},
                    'A': {'a', 'Rq', 'q'},
                    'Vb': {'b'},
                    'Vq': {'q'},
                    'X': {'AA'}
                }
            }
        }
    },
    {
        'grammar': {
            'S': {'aSA', 'BSB', 'D'},
            'A': {'C'},
            'C': {'a'},
            'B': {'b'},
            'D': {'ε'}
        },
        'first-non-terminal': 'S',
        'steps': {
            1: {
                'nullable': {'D', 'S'},
                'grammar': {
                    'S': {'aSA', 'BSB', 'aA', 'BB'},
                    'A': {'C'},
                    'C': {'a'},
                    'B': {'b'}
                }
            },
            2: {
                'units': {
                    'S': {'S'},
                    'A': {'A', 'C'},
                    'C': {'C'},
                    'B': {'B'}
                },
                'grammar': {
                    'S': {'aSA', 'BSB', 'aA', 'BB'},
                    'A': {'a'},
                    'C': {'a'},
                    'B': {'b'}
                }
            },
            3: {
                'generators': {'S', 'A', 'C', 'B'},
                'grammar': {
                    'S': {'aSA', 'BSB', 'aA', 'BB'},
                    'A': {'a'},
                    'C': {'a'},
                    'B': {'b'}
                }
            },
            4: {
                'reachables': {'S', 'A', 'B'},
                'grammar': {
                    'S': {'aSA', 'BSB', 'aA', 'BB'},
                    'A': {'a'},
                    'B': {'b'}
                }
            },
            5: {
                'grammar': {
                    'S': {'aSA', 'BSB', 'aA', 'BB'},
                    'A': {'a'},
                    'B': {'b'},
                    'Va': {'a'}
                }
            },
            6: {
                'grammar': {
                    'S': {'aX', 'BY', 'aA', 'BB'},
                    'A': {'a'},
                    'B': {'b'},
                    'Va': {'a'},
                    'X': {'SA'},
                    'Y': {'SB'}
                }
            }
        }
    },
    {
        'grammar': {
            'D': {'eEM', 'Mm', 'mD', 'ε'},
            'E': {'ED', 'eM', 'm'},
            'M': {'dD', 'eE', 'e'}
        },
        'first-non-terminal': 'D',
        'steps': {
            1: {
                'nullable': {'D'},
                'grammar': {
                    'D': {'eEM', 'Mm', 'mD', 'm'},
                    'E': {'ED', 'eM', 'm', 'E'},
                    'M': {'dD', 'eE', 'e', 'd'}
                }
            },
            2: {
                'units': {
                    'D': {'D'},
                    'E': {'E'},
                    'M': {'M'}
                },
                'grammar': {
                    'D': {'eEM', 'Mm', 'mD', 'm'},
                    'E': {'ED', 'eM', 'm'},
                    'M': {'dD', 'eE', 'e', 'd'}
                }
            },
            3: {
                'generators': {'D', 'E', 'M'},
                'grammar': {
                    'D': {'eEM', 'Mm', 'mD', 'm'},
                    'E': {'ED', 'eM', 'm'},
                    'M': {'dD', 'eE', 'e', 'd'}
                }
            },
            4: {
                'reachables': {'D', 'E', 'M'},
                'grammar': {
                    'D': {'eEM', 'Mm', 'mD', 'm'},
                    'E': {'ED', 'eM', 'm'},
                    'M': {'dD', 'eE', 'e', 'd'}
                }
            },
            5: {
                'grammar': {
                    'D': {'eEM', 'Mm', 'mD', 'm'},
                    'E': {'ED', 'eM', 'm'},
                    'M': {'dD', 'eE', 'e', 'd'},
                    'Ve': {'e'},
                    'Vd': {'d'},
                    'Vm': {'m'}
                }
            },
            6: {
                'grammar': {
                    'D': {'eX', 'Mm', 'mD', 'm'},
                    'E': {'ED', 'eM', 'm'},
                    'M': {'dD', 'eE', 'e', 'd'},
                    'Ve': {'e'},
                    'Vd': {'d'},
                    'Vm': {'m'},
                    'X': {'EM'}
                }
            }
        }
    }
]
