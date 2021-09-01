def input_paramerty():
    print("vvedyte ves (v kg):")
    ves = input()
    print("ves: ", ves, "\na teper rost (v cm):")
    rost = input()
    print("rost: ", rost, "\na teper vozrast:")
    vozrast = input()
    print("vozrast: ", vozrast, "\na teper pol (0 = muzjina, 1 = jenshina):")
    # 0 это мужчина а 1 это женщина
    pol = input()
    print("pol: ", pol)
    return(int(ves), int(vozrast), int(rost), int(pol))

def output_rezultat(kalory):
    print("vam nado zgugat stolko kalory: ", kalory)