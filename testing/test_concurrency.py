import subprocess
import time
import os
import concurrent.futures
import json
import sys

LINK = "https://autograder-service-ece440spring2024.apps.shift.nerc.mghpcc.org"
UNAME_PWD = "istaplet:123"

# request with correct solution
def make_request1():
    for http_retries in range(1):
        try:
            response = subprocess.run(["curl", "-m", "120", "--user", UNAME_PWD, "-X", "POST", "-F", "submission.zip=@./correct_solution/submission.zip", LINK], capture_output=True, text=True)

            response_json = json.loads(response.stdout)
            score = response_json.get('score')
            print(score)
        except:
            print('fail')

# bogus request
def make_request2():

    for http_retries in range(1):
        try:
            response = subprocess.run(["curl","-m", "120", "--user", UNAME_PWD, "-X", "POST", "-F", "submission.zip=@./bogus_solution/submission.zip", LINK], capture_output=True, text=True)

            response_json = json.loads(response.stdout)
            score = response_json.get('score')
            print(score)
        except:
            print('fail')

def main():
    number_of_requests = 100

    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_requests) as executor:
        # Create a list of futures
        futures = []
        for i in range(number_of_requests):
            if i % 10 == 0:
                time.sleep(2)
            if i % 2 == 0:  # Even step
                futures.append(executor.submit(make_request2))
            else:  # Odd step
                futures.append(executor.submit(make_request1))        
        # Wait for the futures to complete and get the results
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
if __name__ == "__main__":
    main()
