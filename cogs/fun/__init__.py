from .bunger import Bunger
from .eightball import EightBall
from .load import Load
from .loaf import Loaf
from .owo import Owo
from .petthebot import PetTheBot
from .petthebunger import PetTheBunger
from .rate import Rate
from .uwu import Uwu


def init_fun(client):
    client.add_cog(Bunger(client))
    client.add_cog(EightBall(client))
    client.add_cog(Load(client))
    client.add_cog(Loaf(client))
    client.add_cog(Owo(client))
    client.add_cog(PetTheBot(client))
    client.add_cog(PetTheBunger(client))
    client.add_cog(Rate(client))
    client.add_cog(Uwu(client))