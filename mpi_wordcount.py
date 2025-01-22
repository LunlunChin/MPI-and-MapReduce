from mpi4py import MPI
import sys
import time

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Rank of the current process
size = comm.Get_size()  # Total number of processes

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

    # Master process (rank 0)
    if rank == 0:
        # Check if the input file is provided
        if len(sys.argv) < 2:
            print("Usage: mpirun -np <num_processes> python3 mpi_wordcount.py <input_file>")
            sys.exit(1)

        input_file = sys.argv[1]

        # Read input data
        with open(input_file, "r") as f:
            lines = f.readlines()

        # Distribute lines to worker processes
        chunk_size = len(lines) // (size - 1)
        for i in range(1, size):
            start = (i - 1) * chunk_size
            end = i * chunk_size if i < size - 1 else len(lines)
            comm.send(lines[start:end], dest=i)

        # Gather results from worker processes
        word_counts_list = []
        for i in range(1, size):
            word_counts = comm.recv(source=i)
            word_counts_list.append(word_counts)

        # Reduce the results
        final_counts = reducer(word_counts_list)

        # Print the final word counts
        for word, count in sorted(final_counts.items()):
            print(f"{word}\t{count}")

        # Print execution time
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")

    # Worker processes (rank > 0)
    else:
        # Receive data from the master process
        lines = comm.recv(source=0)

        # Perform the map operation
        word_counts = {}
        for line in lines:
            words = line.strip().split()
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

        # Send the results back to the master process
        comm.send(word_counts, dest=0)