def calcola_overround(quota_over, quota_under):
    return (1 / quota_over) + (1 / quota_under) 


def calcola_quote_pulite(quota_over, quota_under):
    """
    Calcola le probabilità pulite Over/Under partendo dalle quote.

    Args:
        quota_over (float): quota Over
        quota_under (float): quota Under

    Returns:
        dict: {'overround': float, 'p_over': float, 'p_under': float}
    """
    # 1️⃣ calcolo overround totale
    overround = calcola_overround(quota_over, quota_under)

    # 2️⃣ probabilità implicite “sporche” ovvero secondo il bookmaker
    p_over_raw = 1 / quota_over
    p_under_raw = 1 / quota_under

    # 3️⃣ normalizzazione per ottenere probabilità pulite ovvero quelle reali senza i margini del book
    p_over = p_over_raw / overround
    p_under = p_under_raw / overround

    return {
        "overround": (overround - 1)* 100,
        "p_over_raw": p_over_raw,
        "p_under_raw": p_under_raw,
        "p_over": p_over,
        "p_under": p_under
    }
