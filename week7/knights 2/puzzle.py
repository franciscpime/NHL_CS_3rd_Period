from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

base_rules = And(
    # A is a Knight or a Knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is a knight or a Knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # C is a knight or a Knave, but not both
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    base_rules,
    # A is a knight implies A is both a knight and a knave
    Implication(AKnight, And(AKnight, AKnave)),
    # A is a knave implies A is not both a knight and a knave
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    base_rules,
    # A is a knight implies A is both a knight and a knave
    Implication(AKnight, And(AKnave, BKnave)),
    # A is a knave implies A is not both a knight and a knave
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    base_rules,
    # Declaration A
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # Declaration B
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    base_rules,

    # B says that A said "I am a knave"
    # If B is Knight (tells the truth), then A really said "I am a knave"
    #   >> If A is Knight, A only tells the truth, then AKnave would be true >> contradiction
    #   >> If A is Knave, A lies, then "I am a knave" would be false >> contradiction
    # So B can only be Knave
    Implication(BKnight, And(
        Implication(AKnight, AKnave),   # A said "I am a knave" and is knight >> contradiction
        Implication(AKnave, Not(AKnave)) # A said "I am a knave" and is knave >> lies >> contradiction
    )),
    Implication(BKnave, Not(And(
        Implication(AKnight, AKnave),
        Implication(AKnave, Not(AKnave))
    ))),

    # B says "C is a knave"
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight)),
)


def main() -> None:
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
