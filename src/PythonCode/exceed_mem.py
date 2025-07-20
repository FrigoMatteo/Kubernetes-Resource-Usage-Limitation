import time

def allocate_memory(mb):
    size = mb*1024*1024
    return bytearray(size)


time.sleep(5)
print("We start by allocating 10 MB of memory")
mem_chunks = [allocate_memory(10)]  # 10 MB

time.sleep(30)
print("After ten seconds we will try allocating 50MB")

try:
    mem_chunks.append(allocate_memory(50))  # Supera i 50 MB totali
    print("Process still alive")
except MemoryError:
    print(" MemoryError: we overflow the limit")

# Wait to observe the pod behaviour
time.sleep(60)
print("Finished")
