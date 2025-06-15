#!/usr/bin/env python3
"""
Legislative Data Processor

This script reads data about legislators, bills, votes, and vote results, than produces two output files:
- legislators-support-oppose-count: Counts of bills supported and opposed by each legislator
- bills-summary: Summary of each bill including supporter & opposer counts and primary sponsor
"""

import csv
from collections import defaultdict
import os

# using os.path cause im currently in windows
BASE_DIR = "Quorum_Coding_Challenge/Quorum Coding Challenge - Candidate Folder"
LEGISLATORS_INPUT = os.path.join(BASE_DIR, "legislators.csv")
BILLS_INPUT = os.path.join(BASE_DIR, "bills.csv")
VOTES_INPUT = os.path.join(BASE_DIR, "votes.csv")
VOTE_RESULTS_INPUT = os.path.join(BASE_DIR, "vote_results.csv")

# Output files
LEGISLATORS_OUTPUT = "legislators-support-oppose-count.csv"
BILLS_OUTPUT = "bills.csv" #moved the input bills csv to another folder to avoid conflict

def load_legislators():
    legislators = {}
    with open(LEGISLATORS_INPUT, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            legislators[row['id']] = {
                'id': row['id'],
                'name': row['name'],
                'supported_bills': 0,
                'opposed_bills': 0
            }
    print("Legislators: ", legislators)
    return legislators

def load_bills():
    bills = {}
    with open(BILLS_INPUT, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bills[row['id']] = {
                'id': row['id'],
                'title': row['title'],
                'sponsor_id': row['sponsor_id'],
                'supporter_count': 0,
                'opposer_count': 0
            }
    print("Bills: ", bills)
    return bills

def load_votes():
    votes = {}
    with open(VOTES_INPUT, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            votes[row['id']] = row['bill_id']
    print("votes: ", votes)
    return votes

def main():
    """Main function."""
    legislators = load_legislators()
    bills = load_bills()
    votes = load_votes()

if __name__ == "__main__":
    main()