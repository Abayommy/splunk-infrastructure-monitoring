import splunklib.client as client
from dotenv import load_dotenv
import os
import json
import time
from datetime import datetime

class SplunkGitInterface:
    def __init__(self):
        load_dotenv()
        self.splunk = client.connect(
            host=os.getenv('SPLUNK_HOST'),
            port=os.getenv('SPLUNK_PORT'),
            username=os.getenv('SPLUNK_USERNAME'),
            password=os.getenv('SPLUNK_PASSWORD')
        )
        
    def collect_metrics(self):
        # Define your Splunk searches
        searches = {
            'system_metrics': '''
                search index=infrastructure sourcetype=system_metrics
                | stats 
                    avg(cpu_usage) as avg_cpu 
                    avg(memory_usage) as avg_mem 
                    avg(disk_usage) as avg_disk
                | eval timestamp=strftime(_time, "%Y-%m-%d %H:%M:%S")
            '''
        }
        
        results = {}
        for name, query in searches.items():
            job = self.splunk.jobs.create(query)
            while not job.is_done():
                time.sleep(2)
            results[name] = list(job.results())
            
        return results
