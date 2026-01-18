import os
import pandas as pd

def aggiorna_clean():
    
    # Creiamo la cartella data nel caso non esista
    os.makedirs("data", exist_ok=True)
    
    # URL del CSV online
    url = "https://fixturedownload.com/download/serie-a-2025-UTC.csv"
    
    # scarica il CSV e salva localmente
    try:
        df = pd.read_csv(url)
        df.to_csv("data/matches.csv", index=False)
        print("matches.csv scaricato e salvato ✅")
    except Exception as e:
        print("Errore nel download del CSV:", e)
        return
    
    if "Result" not in df.columns:
        print("Errore: colonna 'Result' non trovata nel CSV")
        return
    
    # split della colonna Result in Home Goals / Away Goals
    df[["Home Goals", "Away Goals"]] = df["Result"].str.split(" - ", expand=True)
    
    # converti in numeri, valori vuoti diventano NaN
    df["Home Goals"] = pd.to_numeric(df["Home Goals"], errors='coerce')
    df["Away Goals"] = pd.to_numeric(df["Away Goals"], errors='coerce')
    
    # salva CSV pulito
    df.to_csv("data/matches_clean.csv", index=False)
    print("matches_clean.csv aggiornato correttamente ✅")

# permette di eseguire la funzione direttamente da terminale
if __name__ == "__main__":
    aggiorna_clean()