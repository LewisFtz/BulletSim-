###Validation for inputted variables.
def validate(initial_velocity, height, mass_of_bullet):
    validate = True

    while validate == True:
        try:
            initial_velocity = (float(initial_velocity))
        except ValueError:
            print("Initial Velocity is not an valid input")
            return validate 
        else:
            print("Initial Velocity is a valid input!")
            validate = False

    validate = True

    while validate == True:
        try:
            height = (float(height))
        except ValueError:
            print("Height is not an valid input")
            return validate 
        else:
            print("Hegiht is a valid input!")
            validate = False
            
            
    validate = True

    while validate == True:
        try:
            mass_of_bullet = (float(mass_of_bullet))
        except ValueError:
            print("Mass Of bullet is not an valid input")
            return validate 
        else:
            print("Mass of bullet is a valid input!")
            validate = False
    return validate
