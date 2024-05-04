"""
Compendium Reader
"""
import os
import sys
import html
import requests
import threading

def init():
    """
    Initialize Global Variables
    """
    global results

    results = {}

def pull_manual_contents(topic, url_base="https://raw.githubusercontent.com/Thanatisia/help-compendium/main/manuals/"):
    """
    Thread Function
    """
    # Initialize Variables

    # Format URL
    url = "{}/{}".format(url_base, topic)

    print("[i] Obtaining manual for [{}]".format(topic))

    # Send a HTTP GET request and store the response
    response = requests.get(url=url)

    # Receive the response text
    rText = response.text

    # Store results in a list
    results[topic] = rText

def design_threads(args):
    threads = []
    number_of_Threads = len(args)

    for i in range(number_of_Threads):
        # Initialize a kew Thread
        thread = threading.Thread(target=pull_manual_contents, args=args)

        # Append the thread into the list of threads
        threads.append(thread)

    return threads

def start_threads(threads):
    # Iterate through the list of threads and start
    for thread in threads:
        # Start thread
        thread.start()

def join_threads(threads):
    # Iterate through the list of threads and wait for the thread to complete before proceeding
    for thread in threads:
        # Wait for thread to complete before proceeding
        thread.join()

def download_manual_multithread(args):
    threads = design_threads(args)
    print("[i] Processing...")
    start_threads(threads)
    join_threads(threads)

    # Complete
    print("")
    print("[+] Process completed")
    print("")

def download_manual_for_loop(args):
    print("[i] Processing...")
    for i in range(len(args)):
        # Get current argument
        curr_arg = args[i]

        # Execute
        pull_manual_contents(curr_arg)

    # Complete
    print("")
    print("[+] Process completed")
    print("")

def main():
    # Initialize global variables
    init()

    # Initialize local variables
    args = [
        "README.md"
        # "software-development/programming-languages/python/libraries/built-in/sqlite3.md"
    ]

    # Download manual contents
    download_manual_multithread(args)

    # Print manual contents
    for k,v in results.items():
        print("{} = {}".format(k,v))

if __name__ == "__main__":
    main()

