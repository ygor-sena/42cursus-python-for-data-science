from S1E9 import Character, Stark
from textwrap import dedent

# hodor = Character("hodor")

Ned = Stark("Ned")

print(Ned.__dict__)

print(Ned.is_alive)

Ned.die()
print(Ned.is_alive)

print(dedent(Ned.__doc__))
print(dedent(Ned.__init__.__doc__))
print(dedent(Ned.die.__doc__))

print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
