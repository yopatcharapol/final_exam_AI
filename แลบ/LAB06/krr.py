def load_knowledge(filename="knowledge.txt"):
    knowledge = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue

            if "=>" not in line:
                continue

            keys_part, value = line.split("=>", 1)
            value = value.strip()

            keys = frozenset([k.strip() for k in keys_part.split(",") if k.strip()])
            knowledge[keys] = value

    return knowledge

def krr(questions):

    rules = load_knowledge()

    for rules,fact in rules.items():
        if all(question in rules for question in questions ):
            return fact

    return 'ไม่สามารถวินิจฉัยได้'

if __name__ == '__main__':
    n = int(input("Enter number of your cases:"))

    rule = []
    for i in range(n):
        rule.append(input())

    fact = krr(rule)
    print('-----------------------------------')
    print(fact)