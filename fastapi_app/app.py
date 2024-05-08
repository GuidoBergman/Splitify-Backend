from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import schemas
from sqlalchemy.orm import Session
from typing import List, Optional


import crud, models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # URL del frontend
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)



@app.post("/expenditures")
def create_expenditure(expenditure: schemas.ExpenditureBase, db: Session = Depends(get_db)):
    return crud.create_expenditure(db=db, expenditure=expenditure)


@app.get("/expenditures/{id_group}", response_model=List[schemas.ExpenditureBase])
def read_expenditures(
    id_group: int, id_user: Optional[int] = None,
    skip: int = 0, limit: int = 100, 
    db: Session = Depends(get_db)
):
    expenditures = crud.get_expenditures(
        db, id_group, id_user, skip=skip, limit=limit
    )

    print(expenditures)

    return expenditures



@app.post("/users")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/users", response_model=List[schemas.User])
def read_users(
    id_user: Optional[int] = None,
    username: Optional[str] = None,
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    users = crud.get_users(
        db, skip, limit, id_user, username
    )

    print(users)

    return users


@app.get("/user/{username}", response_model=schemas.User)
def read_users(
    username: str,
    db: Session = Depends(get_db)
):
    user = crud.get_user(
        db, username
    )

    print(user)

    return user

@app.get("/hello")
async def read_root():
    return {"message": "Estos son los datos desde el backend"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)