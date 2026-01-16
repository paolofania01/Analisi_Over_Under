def media_gol_squadra(df, squadra, casa=True):
    if casa:
        partite = df[df["Home Team"] == squadra]
        gf = partite["Home Goals"]
        gs = partite["Away Goals"]
    else:
        partite = df[df["Away Team"] == squadra]
        gf = partite["Away Goals"]
        gs = partite["Home Goals"]

    return gf.mean(), gs.mean()
