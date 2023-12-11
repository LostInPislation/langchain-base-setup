## Call all chain files in here to import them"
from app.chains.chain1 import chain1

## List all chains in there to create a library of them to be called all at once by main on run start"
libchains = {
    "chain1":chain1
}