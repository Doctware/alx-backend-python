#!/usr/bin/env python3
""" This module measures the execution time of wait_n """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken for wait_n to
    execute n coroutines with max_delay.
    """
    start_time = time.time()  # Start the timer
    
    # Run the asynchronous wait_n function and wait for its result
    asyncio.run(wait_n(n, max_delay))
    
    end_time = time.time()  # End the timer
    
    # Calculate total time and average time per coroutine
    total_time = end_time - start_time
    return total_time / n  # Return average time
