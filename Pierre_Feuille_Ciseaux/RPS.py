import random

def player(prev_play, opponent_history=[]):
    # Append the previous play of the opponent to the history
    if prev_play:
        opponent_history.append(prev_play)

    # Use an adaptive strategy based on opponent's history
    guess = adaptive_strategy(opponent_history)
    return guess

# Strategy to count frequencies of opponent's moves
def frequency_strategy(opponent_history):
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    
    count_R = opponent_history.count("R")
    count_P = opponent_history.count("P")
    count_S = opponent_history.count("S")

    if count_R > count_P and count_R > count_S:
        return "P"  # Play Paper to beat Rock
    elif count_P > count_R and count_P > count_S:
        return "S"  # Play Scissors to beat Paper
    else:
        return "R"  # Play Rock to beat Scissors

# Strategy to find patterns in the opponent's history
def pattern_strategy(opponent_history):
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    last_three = "".join(opponent_history[-3:])
    patterns = {
        "RRR": "P", "RRP": "P", "RRS": "R",
        "RPR": "S", "RPP": "S", "RPS": "R",
        "RSR": "P", "RSP": "R", "RSS": "R",
        "PRR": "S", "PRP": "S", "PRS": "P",
        "PPR": "R", "PPP": "R", "PPS": "P",
        "PSR": "S", "PSP": "P", "PSS": "P",
        "SRR": "R", "SRP": "R", "SRS": "S",
        "SPR": "P", "SPP": "P", "SPS": "S",
        "SSR": "R", "SSP": "S", "SSS": "S",
    }
    return patterns.get(last_three, random.choice(["R", "P", "S"]))

# Adaptive strategy that switches between different strategies
def adaptive_strategy(opponent_history):
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])
    
    freq_guess = frequency_strategy(opponent_history)
    pattern_guess = pattern_strategy(opponent_history)

    # Simple decision to switch strategies
    if random.random() > 0.5:
        return freq_guess
    else:
        return pattern_guess
