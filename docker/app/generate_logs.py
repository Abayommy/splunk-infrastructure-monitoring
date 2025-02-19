import time
import random
import logging
from datetime import datetime

logging.basicConfig(
    filename='/app/system.log',
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO
)

def generate_metrics():
    while True:
        # Basic metrics
        cpu_usage = random.uniform(20, 95)
        memory_usage = random.uniform(30, 85)
        disk_usage = random.uniform(40, 90)
        response_time = random.uniform(0.1, 2.0)
        
        # New metrics
        network_latency = random.uniform(1, 100)
        disk_io = random.uniform(0, 200)
        error_rate = random.uniform(0, 5)
        request_count = random.randint(100, 1000)
        
        # Log all metrics
        logging.info(f"CPU_METRIC cpu_usage={cpu_usage:.2f}%")
        logging.info(f"MEMORY_METRIC memory_usage={memory_usage:.2f}%")
        logging.info(f"DISK_METRIC disk_usage={disk_usage:.2f}%")
        logging.info(f"RESPONSE_METRIC response_time={response_time:.2f}s")
        logging.info(f"NETWORK_METRIC latency={network_latency:.2f}ms")
        logging.info(f"DISK_IO_METRIC throughput={disk_io:.2f}MB/s")
        logging.info(f"ERROR_METRIC rate={error_rate:.2f}%")
        logging.info(f"TRAFFIC_METRIC requests={request_count}")
        
        time.sleep(5)

if __name__ == "__main__":
    generate_metrics()
