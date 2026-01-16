def chiedi_squadra(messaggio, squadre):
    while True:
        squadra = input(messaggio).strip().title()

        if squadra in squadre:
            return squadra
        else:
            print("❌ Squadra non valida. Riprova.")

def chiedi_quota(messaggio):
    while True:
        try:
            quota = float(input(messaggio))
            if quota > 1:
                return quota
            else:
                print("❌ La quota deve essere > 1")
        except ValueError:
            print("❌ Inserisci un numero valido")
