# ASSIGNMENT
# Show a context manager for file handling that automatically opens and closes a file

import time
import threading
import sqlite3
import multiprocessing
print("number 1")
with open('filename.txt', 'r') as file:
    # some file operations within the context
    # The file is automatically closed when the block exits

    # Read lines from the file
    lines = file.readlines()

    # Print the content of the file
    for line in lines:
        print(line.strip())


print("NUMBER 2")
# show a context manager for managing a database connection


class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


# Example usage
db_file = 'mydatabase.db'

with DatabaseConnection(db_file) as conn:
    # Perform database operations within the context
    cursor = conn.cursor()

    # Execute SQL statements
    cursor.execute("SELECT * FROM my_table")
    rows = cursor.fetchall()

    # Process the results
    for row in rows:
        print(row)

print("NUMBER 3")
# show a multithreading adn a multiprocessing that allows us
# to run the function for different amounts of time

print("Multithreading")


def worker_function(duration):
    print(f"Worker thread started for duration: {duration} seconds")
    time.sleep(duration)
    print(f"Worker thread finished for duration: {duration} seconds")


# List of durations for each worker thread
durations = [3, 5, 2]

# Create and start threads for each duration
threads = []
for duration in durations:
    thread = threading.Thread(target=worker_function, args=(duration,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()


print("Multi processing")


def worker_function(duration):
    print(f"Worker process started for duration: {duration} seconds")
    time.sleep(duration)
    print(f"Worker process finished for duration: {duration} seconds")


# List of durations for each worker process
durations = [5, 10, 15]

# Create and start processes for each duration
processes = []
for duration in durations:
    process = multiprocessing.Process(target=worker_function, args=(duration,))
    process.start()
    processes.append(process)

# Wait for all processes to finish
for process in processes:
    process.join()
