def find_worst_average_bowler(root, worst_so_far=None):
    if not root:
        return worst_so_far

    current_bowler = root.value

    worst_so_far = worst_so_far or current_bowler

    if current_bowler.average < worst_so_far.average:
        worst_so_far = current_bowler

    worst_so_far = find_worst_average_bowler(root.left, worst_so_far)
    worst_so_far = find_worst_average_bowler(root.right, worst_so_far)

    return worst_so_far
