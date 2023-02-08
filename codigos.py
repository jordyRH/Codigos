from fastapi import FastAPI, HTTPException, status

from pydantic import BaseModel


app= FastAPI()


class User(BaseModel):
    id:int
    Name: str
    LastName:str
    Age:int
 
users_list= [User(id=1,Name="Owens", LastName="Harris", Age="22", Sex="male", Survived="0"),
            User(id=2,Name="Jhon", LastName="Bradley", Age="38", Sex="female" , Survived="1"),
            User(id=3,Name="Laina", LastName="Heikkinen", Age="26", Sex="female" , Survived="1"),
            User(id=4,Name="Henry", LastName="Allen", Age="35", Sex="male" , Survived="0"),
            User(id=5,Name="James", LastName="Mooran", Age="34", Sex="male" , Survived="1"),
            User(id=6,Name="Timothy", LastName="Mcmarthy", Age="54", Sex="male" , Survived="0"),
            User(id=7,Name="Elizabeth", LastName="Bonnell", Age="58", Sex="female" , Survived="1"),
            User(id=8,Name="William", LastName="Henry", Age="20", Sex="male" , Survived="1"),
            User(id=9,Name="Johan", LastName="Andersson", Age="39", Sex="male" , Survived="0"),
            User(id=10,Name="Adolfina", LastName="Vestrom", Age="14", Sex="female" , Survived="0"),
            User(id=11,Name="Mary", LastName="Hewlett", Age="55", Sex="female" , Survived="1"),
            User(id=12,Name="Eugene", LastName="Rice", Age="17", Sex="female" , Survived="0"),
            User(id=13,Name="Fatima", LastName="Masselmani", Age="20", Sex="female" , Survived="0"),
            User(id=14,Name="Joseph", LastName="Fynney", Age="21", Sex="male" , Survived="0"),
            User(id=15,Name="Anna", LastName="Mcgowan", Age="23", Sex="female" , Survived="1"),
            User(id=16,Name="Danira", LastName="Palsson", Age="25", Sex="female" , Survived="1"),
            User(id=17,Name="Alexander", LastName="Fortune", Age="28", Sex="male" , Survived="0"),
            User(id=18,Name="Lalio", LastName="Todoroff", Age="30", Sex="male" , Survived="1"),
            User(id=19,Name="Manuel", LastName="Uruchutu", Age="31", Sex="male" , Survived="1"),
            User(id=20,Name="Agatha", LastName="Glyn", Age="33", Sex="female" , Survived="0"),
            User(id=21,Name="Jamila", LastName="Nicola", Age="40", Sex="female" , Survived="1"),
            User(id=22,Name="Theodor", LastName="Kraeff", Age="43", Sex="male" , Survived="1"),
            User(id=23,Name="Denis", LastName="Lennon", Age="45", Sex="female" , Survived="0"),
            User(id=24,Name="Richard", LastName="Cater", Age="36", Sex="male" , Survived="1"),
            User(id=25,Name="Emily", LastName="Rugg", Age="57", Sex="female" , Survived="1") ]



@app.get("/usersclass/")
async def usersclass():
    return (users_list)


@app.get("/usersclass/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
    



@app.get("/usersclass/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"} 
 

@app.post("/usersclass/", response_model=User, status_code=status.HTTP_201_CREATED)
async def usersclass(user:User):
    
    found=False  
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  
           raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        users_list.append(user)
        raise HTTPException(status_code= status.HTTP_200_OK,detail="Usuario agregado correctamente")
        

@app.put("/usersclass/")
async def usersclass(user:User):
    
    found=False     
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id: 
           users_list[index] = user  
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK,detail="El registro se actualizo correctamente")
    if not found:
        
        raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="No se pudo actualizar el registro")
    else:
        return user
    

@app.delete("/usersclass/{id}")
async def usersclass(id:int):
    
    found=False     
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id ==id:  
           del users_list[index] 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK,detail="El registro se eliminó correctamente")
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Error al eliminar, no se encontro el registro")