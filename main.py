#importar el framework fastapi al entorno de trabajo
from fastapi import FastAPI

#crear el objeto a partir de la clase
app = FastAPI()

Autos=[
        {"marca": "Toyota", "modelo": "Camry", "Año": "2021"},
        {"marca": "Honda", "modelo": "Civic", "Año": "2020"},
        {"marca": "Ford", "modelo": "Mustang", "Año": "2019"},
        {"marca": "Chevrolet", "modelo": "Malibu", "Año": "2018"},
        {"marca": "Volkswagen", "modelo": "Jetta", "Año": "2022"},
        {"marca": "Hyundai", "modelo": "Elantra", "Año": "2017"},
        {"marca": "Nissan", "modelo": "Altima", "Año": "2021"},
        {"marca": "Kia", "modelo": "Optima", "Año": "2020"},
        {"marca": "Subaru", "modelo": "Outback", "Año": "2019"},
        {"marca": "Mazda", "modelo": "CX-5", "Año": "2022"},
        {"marca": "Audi", "modelo": "A4", "Año": "2021"},
        {"marca": "Mercedes-Benz", "modelo": "E-Class", "Año": "2020"},
        {"marca": "Lexus", "modelo": "RX", "Año": "2022"},
        {"marca": "BMW", "modelo": "3 Series", "Año": "2021"},
        {"marca": "Chrysler", "modelo": "300", "Año": "2019"},
        {"marca": "Volvo", "modelo": "XC60", "Año": "2020"},
        {"marca": "Jeep", "modelo": "Grand Cherokee", "Año": "2021"},
        {"marca": "Tesla", "modelo": "Model 3", "Año": "2022"},
        {"marca": "Fiat", "modelo": "500", "Año": "2021"},
        {"marca": "GMC", "modelo": "Sierra", "Año": "2020"},
        {"marca": "Cadillac", "modelo": "Escalade", "Año": "2022"},
        {"marca": "Acura", "modelo": "MDX", "Año": "2021"},
        {"marca": "Buick", "modelo": "Encore", "Año": "2020"},
        {"marca": "Land Rover", "modelo": "Discovery", "Año": "2022"},
        {"marca": "Jaguar", "modelo": "XF", "Año": "2021"},
        {"marca": "Porsche", "modelo": "911", "Año": "2020"},
        {"marca": "Infiniti", "modelo": "QX60", "Año": "2022"},
        {"marca": "Mitsubishi", "modelo": "Outlander", "Año": "2021"},
        {"marca": "Subaru", "modelo": "Forester", "Año": "2020"},
        {"marca": "Nissan", "modelo": "Rogue", "Año": "2022"},
        {"marca": "Kia", "modelo": "Sorento", "Año": "2021"},
        {"marca": "Hyundai", "modelo": "Tucson", "Año": "2020"},
        {"marca": "Ford", "modelo": "Escape", "Año": "2022"},
        {"marca": "Chevrolet", "modelo": "Equinox", "Año": "2021"},
        {"marca": "Toyota", "modelo": "Highlander", "Año": "2020"},
        {"marca": "Honda", "modelo": "CR-V", "Año": "2022"},
        {"marca": "Mazda", "modelo": "Mazda3", "Año": "2021"},
        {"marca": "Audi", "modelo": "Q5", "Año": "2020"},
        {"marca": "Mercedes-Benz", "modelo": "GLC", "Año": "2022"},
        {"marca": "Lexus", "modelo": "NX", "Año": "2021"},
        {"marca": "BMW", "modelo": "X5", "Año": "2020"},
        {"marca": "Chrysler", "modelo": "Pacifica", "Año": "2022"},
        {"marca": "Volvo", "modelo": "S60", "Año": "2021"},
        {"marca": "Jeep", "modelo": "Wrangler", "Año": "2020"},
        {"marca": "Tesla", "modelo": "Model S", "Año": "2021"},
        {"marca": "Fiat", "modelo": "Panda", "Año": "2020"},
        {"marca": "GMC", "modelo": "Terrain", "Año": "2022"},
        {"marca": "Cadillac", "modelo": "XT4", "Año": "2021"},
        {"marca": "Acura", "modelo": "TLX", "Año": "2020"},
        {"marca": "Buick", "modelo": "LaCrosse", "Año": "2022"},
        {"marca": "Land Rover", "modelo": "Range Rover", "Año": "2021"},
        {"marca": "Jaguar", "modelo": "F-PACE", "Año": "2020"},
        {"marca": "Porsche", "modelo": "Cayenne", "Año": "2022"},
        {"marca": "Infiniti", "modelo": "Q50", "Año": "2021"},
        {"marca": "Mitsubishi", "modelo": "Eclipse Cross", "Año": "2020"},
        {"marca": "Subaru", "modelo": "Crosstrek", "Año": "2022"},
        {"marca": "Nissan", "modelo": "Sentra", "Año": "2021"},
        {"marca": "Kia", "modelo": "Forte", "Año": "2020"},
        {"marca": "Hyundai", "modelo": "Sonata", "Año": "2022"},
        {"marca": "Ford", "modelo": "Fusion", "Año": "2021"},
        {"marca": "Chevrolet", "modelo": "Cruze", "Año": "2020"},
        {"marca": "Toyota", "modelo": "Corolla", "Año": "2022"},
        {"marca": "Honda", "modelo": "Accord", "Año": "2021"},
        {"marca": "Mazda", "modelo": "Mazda6", "Año": "2020"},
        {"marca": "Audi", "modelo": "Q7", "Año": "2022"},
        {"marca": "Mercedes-Benz", "modelo": "S-Class", "Año": "2021"},
        {"marca": "Lexus", "modelo": "LS", "Año": "2020"},
        {"marca": "BMW", "modelo": "X3", "Año": "2022"},
        {"marca": "Chrysler", "modelo": "Voyager", "Año": "2021"},
        {"marca": "Volvo", "modelo": "V90", "Año": "2020"},
        {"marca": "Jeep", "modelo": "Compass", "Año": "2022"},
        {"marca": "Tesla", "modelo": "Model X", "Año": "2021"},
        {"marca": "Fiat", "modelo": "500X", "Año": "2020"},
        {"marca": "GMC", "modelo": "Canyon", "Año": "2022"},
        {"marca": "Cadillac", "modelo": "XT5", "Año": "2021"},
        {"marca": "Acura", "modelo": "RDX", "Año": "2020"},
        {"marca": "Buick", "modelo": "Envision", "Año": "2022"},
        {"marca": "Land Rover", "modelo": "Discovery Sport", "Año": "2021"},
        {"marca": "Jaguar", "modelo": "XE", "Año": "2020"},
        {"marca": "Porsche", "modelo": "Macan", "Año": "2022"},
        {"marca": "Infiniti", "modelo": "QX80", "Año": "2021"},
        {"marca": "Mitsubishi", "modelo": "Mirage", "Año": "2020"},
        {"marca": "Subaru", "modelo": "Impreza", "Año": "2022"},
        {"marca": "Nissan", "modelo": "Maxima", "Año": "2021"},
        {"marca": "Kia", "modelo": "Rio", "Año": "2020"},
        {"marca": "Hyundai", "modelo": "Kona", "Año": "2022"},
        {"marca": "Ford", "modelo": "Ranger", "Año": "2021"},
        {"marca": "Chevrolet", "modelo": "Spark", "Año": "2020"},
        {"marca": "Toyota", "modelo": "Sienna", "Año": "2022"},
        {"marca": "Honda", "modelo": "Fit", "Año": "2021"},
        {"marca": "Mazda", "modelo": "CX-9", "Año": "2020"},
        {"marca": "Audi", "modelo": "A3", "Año": "2022"},
        {"marca": "Mercedes-Benz", "modelo": "CLA", "Año": "2021"},
        {"marca": "Lexus", "modelo": "ES", "Año": "2020"},
        {"marca": "BMW", "modelo": "7 Series", "Año": "2022"},
        {"marca": "Chrysler", "modelo": "300C", "Año": "2021"},
        {"marca": "Volvo", "modelo": "XC90", "Año": "2020"},
        {"marca": "Jeep", "modelo": "Renegade", "Año": "2022"},
        {"marca": "Tesla", "modelo": "Model Y", "Año": "2022"},
        {"marca": "Fiat", "modelo": "Tipo", "Año": "2021"},
        {"marca": "GMC", "modelo": "Yukon", "Año": "2020"},
        {"marca": "Cadillac", "modelo": "CT4", "Año": "2022"},
        {"marca": "Acura", "modelo": "ILX", "Año": "2021"},
        {"marca": "Buick", "modelo": "Regal", "Año": "2020"},
        {"marca": "Land Rover", "modelo": "Defender", "Año": "2022"},
        {"marca": "Jaguar", "modelo": "I-PACE", "Año": "2021"},
        {"marca": "Porsche", "modelo": "Panamera", "Año": "2020"},
        {"marca": "Infiniti", "modelo": "Q60", "Año": "2022"},
        {"marca": "Mitsubishi", "modelo": "Lancer", "Año": "2021"},
        {"marca": "Subaru", "modelo": "Legacy", "Año": "2020"},
        {"marca": "Nissan", "modelo": "Titan", "Año": "2022"},
        {"marca": "Kia", "modelo": "Stinger", "Año": "2021"},
        {"marca": "Hyundai", "modelo": "Veloster", "Año": "2020"},
        {"marca": "Ford", "modelo": "Edge", "Año": "2022"},
        {"marca": "Chevrolet", "modelo": "Blazer", "Año": "2021"},
        {"marca": "Toyota", "modelo": "Tundra", "Año": "2020"},
        {"marca": "Honda", "modelo": "Insight", "Año": "2022"},
        {"marca": "Mazda", "modelo": "CX-30", "Año": "2021"},
        {"marca": "Audi", "modelo": "S4", "Año": "2020"},
        {"marca": "Mercedes-Benz", "modelo": "GLA", "Año": "2022"},
        {"marca": "Lexus", "modelo": "GX", "Año": "2021"},
        {"marca": "BMW", "modelo": "X1", "Año": "2020"},
        {"marca": "Chrysler", "modelo": "Aspen", "Año": "2022"},
        {"marca": "Volvo", "modelo": "XC40", "Año": "2021"},
        {"marca": "Jeep", "modelo": "Cherokee", "Año": "2020"},
        {"marca": "Tesla", "modelo": "Roadster", "Año": "2022"},
        {"marca": "Fiat", "modelo": "Ducato", "Año": "2021"},
        {"marca": "GMC", "modelo": "Savana", "Año": "2020"},
        {"marca": "Cadillac", "modelo": "XT6", "Año": "2022"},
        {"marca": "Acura", "modelo": "RLX", "Año": "2021"},
        {"marca": "Buick", "modelo": "Cascada", "Año": "2020"},
        {"marca": "Land Rover", "modelo": "Range Rover Evoque", "Año": "2022"},
        {"marca": "Jaguar", "modelo": "F-TYPE", "Año": "2021"},
        {"marca": "Porsche", "modelo": "718 Boxster", "Año": "2020"},
        {"marca": "Infiniti", "modelo": "QX70", "Año": "2022"},
        {"marca": "Mitsubishi", "modelo": "Montero", "Año": "2021"},
        {"marca": "Subaru", "modelo": "Tribeca", "Año": "2020"},
        {"marca": "Nissan", "modelo": "Cube", "Año": "2022"},
        {"marca": "Kia", "modelo": "K900", "Año": "2021"},
        {"marca": "Hyundai", "modelo": "Entourage", "Año": "2020"},
        {"marca": "Ford", "modelo": "C-MAX", "Año": "2022"},
        {"marca": "Chevrolet", "modelo": "Cobalt", "Año": "2021"},
        {"marca": "Toyota", "modelo": "Land Cruiser", "Año": "2020"},
        {"marca": "Honda", "modelo": "Pilot", "Año": "2022"},
        {"marca": "Mazda", "modelo": "RX-8", "Año": "2021"},
        {"marca": "Audi", "modelo": "TT", "Año": "2020"},
        {"marca": "Mercedes-Benz", "modelo": "GLB", "Año": "2022"},
        {"marca": "Lexus", "modelo": "RC", "Año": "2021"},
        {"marca": "BMW", "modelo": "X6", "Año": "2020"},
        {"marca": "Chrysler", "modelo": "PT Cruiser", "Año": "2022"},
        {"marca": "Volvo", "modelo": "V60", "Año": "2021"},
        {"marca": "Jeep", "modelo": "Liberty", "Año": "2020"},
        {"marca": "Tesla", "modelo": "Model Z", "Año": "2022"},
        {"marca": "Fiat", "modelo": "Bravo", "Año": "2021"},
        {"marca": "GMC", "modelo": "Acadia", "Año": "2020"},
        {"marca": "Cadillac", "modelo": "ATS", "Año": "2022"},
        {"marca": "Acura", "modelo": "NSX", "Año": "2021"},
        {"marca": "Buick", "modelo": "Verano", "Año": "2020"},
        {"marca": "Land Rover", "modelo": "Range Rover Sport", "Año": "2022"},
        {"marca": "Jaguar", "modelo": "XJ", "Año": "2021"},
        {"marca": "Porsche", "modelo": "911 Turbo", "Año": "2020"},
        {"marca": "Infiniti", "modelo": "QX50", "Año": "2022"},
        {"marca": "Mitsubishi", "modelo": "Raider", "Año": "2021"},
        {"marca": "Subaru", "modelo": "Ascent", "Año": "2020"},
        {"marca": "Nissan", "modelo": "Kicks", "Año": "2022"},
        {"marca": "Kia", "modelo": "Soul", "Año": "2021"},
        {"marca": "Hyundai", "modelo": "Accent", "Año": "2020"},
        {"marca": "Ford", "modelo": "EcoSport", "Año": "2022"},
        {"marca": "Chevrolet", "modelo": "Trax", "Año": "2021"},
        {"marca": "Toyota", "modelo": "Rav4", "Año": "2020"},
        {"marca": "Honda", "modelo": "HR-V", "Año": "2022"},
        {"marca": "Mazda", "modelo": "MX-5 Miata", "Año": "2021"},
        {"marca": "Audi", "modelo": "Q8", "Año": "2020"},
        {"marca": "Mercedes-Benz", "modelo": "GLS", "Año": "2022"},
        {"marca": "Lexus", "modelo": "LX", "Año": "2021"},
        {"marca": "BMW", "modelo": "X7", "Año": "2020"},
        {"marca": "Chrysler", "modelo": "Sebring", "Año": "2022"},
        {"marca": "Volvo", "modelo": "V90 Cross Country", "Año": "2021"},
        {"marca": "Jeep", "modelo": "Patriot", "Año": "2020"},
        {"marca": "Tesla", "modelo": "Cybertruck", "Año": "2022"},
        {"marca": "Fiat", "modelo": "Multipla", "Año": "2021"},
        {"marca": "GMC", "modelo": "Envoy", "Año": "2020"},
        {"marca": "Cadillac", "modelo": "XT3", "Año": "2022"},
        {"marca": "Acura", "modelo": "CDX", "Año": "2021"},
        {"marca": "Buick", "modelo": "Encore GX", "Año": "2020"},
        {"marca": "Land Rover", "modelo": "Range Rover Velar", "Año": "2022"},
        {"marca": "Jaguar", "modelo": "XE SV Project 8", "Año": "2021"},
        {"marca": "Porsche", "modelo": "Taycan", "Año": "2020"},
        {"marca": "Infiniti", "modelo": "QX30", "Año": "2022"},
        {"marca": "Mitsubishi", "modelo": "Outlander Sport", "Año": "2021"},
        {"marca": "Subaru", "modelo": "BRZ", "Año": "2020"},
        {"marca": "Nissan", "modelo": "Rogue Sport", "Año": "2022"},
        {"marca": "Kia", "modelo": "Telluride", "Año": "2021"},
        {"marca": "Hyundai", "modelo": "Santa Fe", "Año": "2020"},
        {"marca": "Ford", "modelo": "Explorer", "Año": "2022"},
        {"marca": "Chevrolet", "modelo": "Colorado", "Año": "2021"},
        {"marca": "Toyota", "modelo": "Sequoia", "Año": "2020"},
        {"marca": "Honda", "modelo": "Passport", "Año": "2022"},
        {"marca": "Mazda", "modelo": "CX-3", "Año": "2021"},
        {"marca": "Audi", "modelo": "RS 7", "Año": "2020"}
]

@app.get("/Autos")

@app.get("/Autos/marca")
async def marcas():
    return [auto["marca"] for auto in Autos]

@app.get("/Autos/marca/ford")
async def ford(): 
    return [auto["modelo"] for auto in Autos if auto["marca"] == "Ford"]

@app.get("/Autos/marca/ford/explorer")
async def mod_explorer():
    return [{"modelo": auto["modelo"], "año":auto["Año"]} 
            for auto in Autos if auto["marca"] == "Ford" and auto["modelo"] == "Explorer"]
    
@app.get("/Autos/marca/mazda")
async def mazda(): 
    return [auto["modelo"] for auto in Autos if auto["marca"] == "Mazda"]

@app.get("/Autos/marca/mazda/cx-3")
async def mod_cx3():
    return [{"modelo": auto["modelo"], "año":auto["Año"]} 
            for auto in Autos if auto["marca"] == "Mazda" and auto["modelo"] == "CX-3"]

@app.get("/Autos/modelo/")
async def modelo(): 
    return [auto["modelo"] for auto in Autos]

@app.get("/Autos/anio/")
async def anio(): 
    return [auto["Año"] for auto in Autos]

@app.get("/Autos/anio/2021")
async def anio_2021(): 
    return [{auto["marca"], auto["modelo"]} for auto in Autos if auto["Año"] == "2021"]

@app.get("/Autos/anio/2020")
async def anio_2020(): 
    return [{auto["marca"], auto["modelo"]} for auto in Autos if auto["Año"] == "2020"]




#Levantamos el server Uvicorn
#-uvicorn main:app --reload-
# En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000