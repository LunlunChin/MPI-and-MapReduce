import subprocess
import time

# Start timing
start_time = time.time()

# Run the Hadoop Streaming job
command = [
    "hadoop", "jar", "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar",
    "-files", "mapper.py,reducer.py",
    "-mapper", "mapper.py",
    "-reducer", "reducer.py",
    "-input", "/input/war_and_peace.txt",
    "-output", "/output-war-and-peace"
]

# Execute the command
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print the output and errors
print("STDOUT:", process.stdout.decode())
print("STDERR:", process.stderr.decode())

# Print execution time
end_time = time.time()
print(f"Total execution time: {end_time - start_time:.4f} seconds")