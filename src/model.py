def stima_over(gf_home, gs_home, gf_away, gs_away):
    gol_attesi = gf_home + gf_away
    prob_over = min(gol_attesi / 3, 1)  # normalizzazione semplice
    return prob_over
