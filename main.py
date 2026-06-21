import math
import random
from collections import Counter

def calculate_entropy(data):
    """
    Calculates the Shannon entropy of a given data sequence.
    Entropy quantifies the average amount of information or uncertainty in a random variable.
    Lower entropy suggests more predictability or structure.
    """
    if not data:
        return 0.0

    # Count frequencies of each symbol in the data
    counts = Counter(data)

    # Calculate probabilities of each symbol
    total_symbols = len(data)
    probabilities = [count / total_symbols for count in counts.values()]

    # Calculate Shannon entropy: H = -sum(p * log2(p))
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy

def generate_random_string(length, charset):
    """
    Generates a string of specified length with characters chosen uniformly at random
    from the given charset. This represents truly random data.
    """
    return ''.join(random.choice(charset) for _ in range(length))

def generate_patterned_string_bias(length, charset, pattern_char, bias_factor):
    """
    Generates a string where a specific 'pattern_char' appears with a higher probability
    (bias_factor) than other characters. This simulates a subtle, 'unwritten' bias.
    """
    s = []
    other_chars = [c for c in charset if c != pattern_char]
    for _ in range(length):
        if random.random() < bias_factor: # Higher chance to pick the pattern_char
            s.append(pattern_char)
        else:
            s.append(random.choice(other_chars)) # Pick from other characters
    return ''.join(s)

def generate_patterned_string_repeating(length, charset, base_pattern, noise_level):
    """
    Generates a string with a repeating 'base_pattern' embedded, but with a certain
    'noise_level' where characters are randomly chosen instead of following the pattern.
    This demonstrates a hidden, structured 'message' within randomness.
    """
    s = []
    pattern_len = len(base_pattern)
    for i in range(length):
        if random.random() < noise_level: # Introduce noise
            s.append(random.choice(charset))
        else:
            s.append(base_pattern[i % pattern_len]) # Follow the pattern
    return ''.join(s)

# --- Main execution --- #
if __name__ == "__main__":
    # Define the character set for our 'messages'
    charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " # 27 possible symbols
    data_length = 2000 # Length of the data sequences to analyze

    print("--- Turing's Last Cipher: Detecting Unwritten Messages ---")
    print("\nConcept: This example demonstrates how 'unwritten messages' or hidden patterns within seemingly random data")
    print("can be detected by analyzing their information entropy. Lower entropy often indicates more predictability or structure,")
    print("suggesting the presence of an underlying 'message' not intentionally encoded by a sender.")

    # Calculate the maximum possible entropy for our charset (perfect randomness)
    max_possible_entropy = math.log2(len(charset))
    print(f"\nCharset size: {len(charset)}")
    print(f"Max possible entropy (for this charset): {max_possible_entropy:.4f} bits per symbol")

    # 1. Generate truly random data
    random_data = generate_random_string(data_length, charset)
    random_entropy = calculate_entropy(random_data)
    print(f"\n1. Truly Random Data (High Entropy):")
    print(f"   Sample (first 50 chars): '{random_data[:50]}...'\n")
    print(f"   Entropy: {random_entropy:.4f} bits per symbol")
    # Explanation: Entropy close to the maximum possible indicates high randomness, no discernible 'message'.
    print(f"   (Closer to max possible entropy indicates higher randomness, no hidden 'message' detected.)")

    # 2. Generate data with a subtle character bias
    pattern_char_bias = 'E'
    bias_factor = 0.1 # 'E' appears with 10% probability (vs uniform ~3.7%)
    patterned_data_bias = generate_patterned_string_bias(data_length, charset, pattern_char_bias, bias_factor)
    patterned_entropy_bias = calculate_entropy(patterned_data_bias)
    print(f"\n2. Data with Subtle Character Bias (Lower Entropy):")
    print(f"   Bias towards '{pattern_char_bias}' with a {bias_factor*100:.0f}% chance (vs uniform ~{1/len(charset)*100:.1f}%)")
    print(f"   Sample (first 50 chars): '{patterned_data_bias[:50]}...'\n")
    print(f"   Entropy: {patterned_entropy_bias:.4f} bits per symbol")
    # Explanation: Lower entropy here suggests a hidden bias or 'unwritten message' (e.g., 'E' is more frequent).
    print(f"   (Lower entropy suggests a hidden bias or 'unwritten message' due to the increased frequency of '{pattern_char_bias}'.)")

    # 3. Generate data with an embedded repeating pattern and noise
    base_pattern = "TURING"
    noise_level = 0.7 # 70% noise, 30% pattern
    patterned_data_repeating = generate_patterned_string_repeating(data_length, charset, base_pattern, noise_level)
    patterned_entropy_repeating = calculate_entropy(patterned_data_repeating)
    print(f"\n3. Data with Embedded Repeating Pattern (Lower Entropy):")
    print(f"   Embedded pattern: '{base_pattern}' with {noise_level*100:.0f}% noise")
    print(f"   Sample (first 50 chars): '{patterned_data_repeating[:50]}...'\n")
    print(f"   Entropy: {patterned_entropy_repeating:.4f} bits per symbol")
    # Explanation: Even with significant noise, the embedded pattern reduces overall entropy, hinting at structure or a 'message'.
    print(f"   (Even with significant noise, the embedded pattern reduces overall entropy, hinting at structure or an 'unwritten message'.)")

    print("\nConclusion: By quantifying entropy, we can infer the presence of underlying order or 'unwritten messages' even when data appears random at first glance.")
    print("This aligns with the idea of deciphering patterns not intentionally encoded, as explored in 'Turing's Last Cipher'.")
