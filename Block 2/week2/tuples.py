
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_activity1():
    print(f"Minimum likelihood of falling: {likelihood()}%")

# Activity 1 finished --------------------------------------


def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)

    return min(likelihoods), max(likelihoods)


def run_activity2():
    min_likelihood, max_likelihood = likelihood_min_max()
    print(f"Minimum likelihood of falling: {min_likelihood}%")
    print(f"Maximum likelihood of falling: {max_likelihood}%")

# Activity 2 finished --------------------------------------


def steps():
    return [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]


def run_activity3():
    steps_probs = steps()

    good_steps = []
    bad_steps = []

    for index in range(len(steps_probs)):
        current_tuple = steps_probs[index]
        if current_tuple[1] >= 50:
            bad_steps.append(current_tuple)
            continue

        good_steps.append(current_tuple)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")


run_activity3()

# Activity 3 finished --------------------------------------