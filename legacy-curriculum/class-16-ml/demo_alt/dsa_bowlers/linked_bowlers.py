def find_worst_average_bowler(bowlers):
    if not bowlers.head:
        return None  # or raise en Exception

    current = bowlers.head
    worst_so_far = current.value
    current = current.next

    while current:
        current_bowler = current.value
        if current_bowler.average < worst_so_far.average:
            worst_so_far = current_bowler
        current = current.next

    return worst_so_far
