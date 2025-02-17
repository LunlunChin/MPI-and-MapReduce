# MPI-and-MapReduce

This repository contains implementations of **MapReduce** and **MPI-based** parallel word count programs. It is designed to demonstrate distributed and parallel computing techniques using Hadoop's MapReduce framework and MPI (Message Passing Interface).

## 📜 Overview

The project includes:
- **Hadoop MapReduce implementation** for word count.
- **MPI-based word count program** to compare performance.
- A test dataset (`war_and_peace.txt`) for running word count.
- Configuration files for setting up Hadoop (`core-site.xml`, `hdfs-site.xml`).
- Scripts to execute the programs.

## 📁 File Structure

- `README.md` - Documentation file  
- `core-site.xml` - Hadoop core configuration  
- `hdfs-site.xml` - Hadoop HDFS configuration  
- `mapper.py` - Mapper script for Hadoop MapReduce  
- `reducer.py` - Reducer script for Hadoop MapReduce  
- `mpi_wordcount.py` - MPI-based word count script  
- `run_wordcount.py` - Script to run the MapReduce job  
- `standalone_wordcount.py` - Standalone Python word count script  
- `war_and_peace.txt` - Sample text file for testing  

## 🚀 Getting Started

### 1️⃣ **Hadoop MapReduce Word Count**
1. Set up Hadoop (single-node or cluster mode).
2. Move the dataset (`war_and_peace.txt`) to HDFS:
   ```sh
   hdfs dfs -put war_and_peace.txt /input/
   ```
3. Run the MapReduce job:
   ```sh
   hadoop jar /path/to/hadoop-streaming.jar \
   -input /input/war_and_peace.txt \
   -output /output/wordcount \
   -mapper "python3 mapper.py" \
   -reducer "python3 reducer.py"
   ```
4. Retrieve results:
   ```sh
   hdfs dfs -cat /output/wordcount/part-*
   ```

### 2️⃣ **MPI Word Count**
1. Install MPI if not already installed:
   ```sh
   sudo apt update && sudo apt install -y mpich
   ```
2. Run MPI-based word count:
   ```sh
   mpirun -np 4 python3 mpi_wordcount.py war_and_peace.txt
   ```

### 3️⃣ **Standalone Word Count**
If you want to run a simple Python script for word count:
```sh
python3 standalone_wordcount.py war_and_peace.txt
```

## 📊 Performance Comparison
You can compare execution times between:
- Hadoop MapReduce (distributed batch processing)
- MPI-based parallel computing
- Standalone single-threaded Python execution

## ⚡ Dependencies
- Python 3.x
- Hadoop (for MapReduce)
- MPICH (for MPI)

## 🎯 Future Work
- Implement additional performance benchmarks.
- Explore different parallel processing strategies.
- Optimize for large-scale datasets.
