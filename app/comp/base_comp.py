## Call all chain files in here to import them"
from app.comp.llms import llm

## List all components (incl. templates) in there to create a library of them to be called all at once by main on run start"
libcomps = {
    "llm-orca":llm-orca,
    "llm-mistral":llm-mistral,
}