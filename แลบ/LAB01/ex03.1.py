from random import random, uniform, randint, seed, choice
from random import choices, randrange

seed(123)

print("random()=", random())
print("randint()=", randint(1,10))
print("uniform()=", uniform(1,10))
seq = range(1,10)
print("seq=", seq)
print("choice(seq)=", choice(seq))
print("choices(seq,k=5)=", choices(seq, k=5))

print("list(seq)",list(seq))