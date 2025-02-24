import splunklib.client as client
from dotenv import load_dotenv
import os

def test_connection():
    try:
        # Load environment variables
        load_dotenv()
        
        # Connect to Splunk
        service = client.connect(
            host=os.getenv('SPLUNK_HOST'),
            port=os.getenv('SPLUNK_PORT'),
            username=os.getenv('SPLUNK_USERNAME'),
            password=os.getenv('SPLUNK_PASSWORD')
        )
        
        # Test the connection
        if service.apps:
            print("✅ Successfully connected to Splunk!")
            print(f"Connected to: {service.host}:{service.port}")
        
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")

if __name__ == "__main__":
    test_connection()
