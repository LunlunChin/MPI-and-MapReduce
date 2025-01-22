import time

def mapper(text):
    """Mapper function: splits text into words and emits (word, 1) pairs."""
    words = text.strip().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def reducer(word_counts_list):
    """Reducer function: aggregates word counts from all mappers."""
    final_counts = {}
    for word_counts in word_counts_list:
        for word, count in word_counts.items():
            final_counts[word] = final_counts.get(word, 0) + count
    return final_counts

if __name__ == "__main__":
    # Start timing
    start_time = time.time()

    # Read input data
    input_file = "war_and_peace.txt"
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Perform the map operation
    word_counts_list = []
    for line in lines:
        word_counts = mapper(line)
        word_counts_list.append(word_counts)

    # Perform the reduce operation
    final_counts = reducer(word_counts_list)

    # Print the final word counts
    for word, count in sorted(final_counts.items()):
        print(f"{word}\t{count}")

    # Print execution time
    end_time = time.time()
    print(f"Execution time (standalone): {end_time - start_time:.4f} seconds")