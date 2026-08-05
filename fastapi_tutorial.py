from fastapi import FastAPI

main = FastAPI()

items = []
@main.get("/")
def read_root():
    return {"message" : "Hello I am Anmol Varshney, Welcome to my FastAPI tutorial!"}

@main.post("/items")
def create_item(item: str):
    items.append(item)
    return {"message": f"Item '{item}' created successfully."}

@main.get("/items/{item}")
def read_items(item: int) -> str:
    Spec_item = items[item]
    return Spec_item