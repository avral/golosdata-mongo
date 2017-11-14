import os
import sys

from runner import run_worker
from tasks import override_steemd


def start_worker(worker):
    workers = [
        'scrape_operations',
        'scrape_blockchain',
        'validate_operations',
        'scrape_all_users',
        'scrape_all_users_quick',
        'scrape_prices',
        'refresh_dbstats',
        'override',
    ]

    if worker not in workers:
        print("ERROR: Invalid or no worker specified!")
        quit(1)

    run_worker(worker)


if __name__ == "__main__":
    # For golos.io node
    override_steemd()

    worker = os.getenv('WORKER', 'scrape_operations')
    print("Starting worker: %s" % worker)

    start_worker(worker)
