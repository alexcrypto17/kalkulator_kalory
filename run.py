from app.io import *
from app.formula import *

if __name__ == "__main__":
    
    (ves, vozrast, rost, pol) = input_paramerty()

    kalory = calculate(ves, vozrast, rost, pol)

    output_rezultat(kalory)