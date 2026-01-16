Analisi Over/Under – Serie A 2025

Questo progetto è un tool in Python per analizzare le probabilità di scommessa Over/Under su partite di Serie A.
Devo ancora implementare l'algoritmo per il calcolo delle probabilita' dei goal.
Work in Progress.


Il programma permette di:

Aggiornare automaticamente i dati delle partite dal CSV online.

Pulire i dati (split gol casa/trasferta).

Inserire manualmente le quote del bookmaker e calcolare le quote pulite (probabilità corrette rimuovendo il margine del bookmaker).

Calcolare le proprie probabilità basate su gol fatti/subiti (media pesata).

progetto-calcistico/
├─ src/                  # Codice Python
│   ├─ main.py           # File principale
│   ├─ aggiorna_clean.py # Funzione per aggiornamento e pulizia CSV
│   ├─ utils.py          # Funzioni utili: chiedi_squadra, chiedi_quota
│   └─ quote.py          # Funzioni per calcolo quote pulite e overround
├─ data/                 # Cartella con CSV delle partite
│   ├─ matches.csv
│   └─ matches_clean.csv
├─ README.md             # Questo file
├─ requirements.txt      # Librerie Python necessarie
└─ .gitignore            # Per escludere cartelle temporanee o ambiente virtuale
