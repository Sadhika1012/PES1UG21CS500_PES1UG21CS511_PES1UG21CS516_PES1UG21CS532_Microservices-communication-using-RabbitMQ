import time

def perform_health_check():
    while True:
        # Add your health check logic here
        print("Performing health check...")
        time.sleep(5)  # Sleep for 5 seconds before the next check

if __name__ == '__main__':
    perform_health_check()
