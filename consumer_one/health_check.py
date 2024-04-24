from flask import Flask
import time

app = Flask(__name__)

def perform_health_check():
    while True:
        # Add your health check logic here
        print("Performing health check...")
        time.sleep(5)  # Sleep for 5 seconds before the next check

@app.route('/health_check')
def health_check():
    perform_health_check()
    return 'Health check performed.'

if __name__ == '__main__':
    app.run(debug=True)

