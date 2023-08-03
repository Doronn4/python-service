import subprocess
import time


def main(service):
    while service.is_running:
        # Write your code for the service here

        # ------------------------------------
        # Modify or remove interval
        time.sleep(10)



if __name__ == '__main__':
    # Install the service
    subprocess.run(['python', 'my_service.py', 'install'], check=True)
    # Start the service
    subprocess.run(['python', 'my_service.py', 'start'], check=True)

