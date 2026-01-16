from aggiorna_clean import aggiorna_clean
from utils import chiedi_squadra, chiedi_quota
from odds import calcola_quote_pulite
import pandas as pd

def main():
    print("Programma per Analisi Over/Under ⚽\n")
    print("Aggiornamento dati in corso...")
    
    # Aggiornamento dei dati da "grezzi" a puliti
    aggiorna_clean()
    
    print("Dati aggiornati correttamente ✅\n")
    
    df = pd.read_csv("data/matches_clean.csv")
    squadre = sorted(df["Home Team"].unique())
    
    home = chiedi_squadra("Inserisci squadra casa: ", squadre)
    away = chiedi_squadra("Inserisci squadra trasferta: ", list(set(squadre) - {home}))

    quota_over = chiedi_quota("Over ->")
    quota_under = chiedi_quota("Under ->")

    print(f"📊 {home} - {away} | Over: {quota_over:.2f} | Under: {quota_under:.2f}")
    
    quote_pulite = calcola_quote_pulite(quota_over, quota_under)

    # Stampo a schermo
    print("\n--- Quote Pulite ---")
    print(f"Overround bookmaker: {quote_pulite['overround']:.3f}%")
    print(f"P(Over) sporca: {quote_pulite['p_over_raw']:.2%}")
    print(f"P(Under) sporca: {quote_pulite['p_under_raw']:.2%}")
    print(f"P(Over) pulita: {quote_pulite['p_over']:.2%}")
    print(f"P(Under) pulita: {quote_pulite['p_under']:.2%}")
    
if __name__ == "__main__":
    main()