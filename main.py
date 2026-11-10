from pyscript import document, display
#NO AI WAS USED FOR GENERATING CODE
listed_elements = {
        "H":("Hydrogen", 1, 1.008),
        "C":("Carbon", 6, 12.011),
        "N":("Nitrogen", 7, 14.007),
        "O":("Oxygen", 8, 15.999),
        "P":("Phosphorus", 15, 30.974),
        "S":("Sulfur", 16, 32.065),
        "Se":("Selenium", 34, 78.960),
        "Cl":("Chlorine", 17, 35.453),
        "F":("Flourine", 9, 18.998),
        "Br":("Bromine", 35, 79.904),
        "I":("Iodine", 1, 1.008),
        "Rn":("Radon", 86, 222),
        "He":("Helium", 2, 4.0026),
        "Ne":("Neon", 10, 20.180),
        "Ar":("Argon", 18, 39.948),
        "Kr":("Krypton", 36, 83.798),
        "Xe":("Xenon", 54, 131.29)
    }

def check_element (e):
    document.getElementById("output1").innerHTML = ""
    element = document.getElementById("atom").value
    element = element.title()
    
    #var2 = dict.get(element,("Element not found","-","-"))
    #document.getElementById("").innerHTML = f""" """"

    verify = listed_elements.get(element, ("-ELEMENT NOT FOUND-","-","-"))
    document.getElementById("output1").innerHTML = f"""
     Symbol: {element} <br>
     Element: {verify[0]} <br>
     Atomic Number: {verify[1]} <br>
     Atomic Mass: {verify[2]} 
    """

