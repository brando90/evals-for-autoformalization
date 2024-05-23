def print_hello_snap():
    print("Hello, World from the Snap Cluster Setup src!")

def print_by_editing_me():
    print("Elyas Obbad")

def print_from_another():
    from another_hello import print_another
    print_another()

if __name__ == "__main__":
    import time
    start_time = time.time()
    print_hello_snap()
    print_by_editing_me()
    print_from_another()
    print(f"Time taken: {time.time() - start_time:.2f} seconds, or {(time.time() - start_time) / 60:.2f} minutes, or {(time.time() - start_time) / 3600:.2f} hours.\a")
