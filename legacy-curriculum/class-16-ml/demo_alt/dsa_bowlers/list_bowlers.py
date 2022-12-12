def find_worst_average_bowler(bowlers):
    worst_so_far = None
    for current_bowler in bowlers:
        worst_so_far = worst_so_far or current_bowler
        if current_bowler.average < worst_so_far.average:
            worst_so_far = current_bowler

    return worst_so_far
