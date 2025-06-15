#!/usr/bin/env python3
"""
Legislative Data Processor

This script reads data about legislators, bills, votes, and vote results, than produces two output files:
- legislators-support-oppose-count: Counts of bills supported and opposed by each legislator
- bills-summary: Summary of each bill including supporter & opposer counts and primary sponsor
"""

import csv
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
    #print("Legislators: ", legislators)
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
    #print("Bills: ", bills)
    return bills

def load_votes():
    #this is a basic junction table
    votes = {}
    with open(VOTES_INPUT, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            votes[row['id']] = row['bill_id']
    #print("votes: ", votes)
    return votes

def process_vote_results(legislators, bills, votes):
    """Process vote results and update legislator and bill counts"""
    with open(VOTE_RESULTS_INPUT, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            legislator_id = row['legislator_id']
            vote_id = row['vote_id']
            vote_type = int(row['vote_type'])
            
            # if legislator or vote not found
            if legislator_id not in legislators or vote_id not in votes:
                continue

            bill_id = votes[vote_id] #retrieves the id of a bill associated with a vote on the junction table
            
            # just an edge case if the bill didnt exist
            if bill_id not in bills:
                continue
                
            # update legislator and bill counts
            # 1 == yea, 2 == nay
            if vote_type == 1:
                legislators[legislator_id]['supported_bills'] += 1
            elif vote_type == 2:
                legislators[legislator_id]['opposed_bills'] += 1

            if vote_type == 1:
                bills[bill_id]['supporter_count'] += 1
            elif vote_type == 2:
                bills[bill_id]['opposer_count'] += 1

def write_legislators_output(legislators):
    """Write legislator support & oppose counts"""
    with open(LEGISLATORS_OUTPUT, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'num_supported_bills', 'num_opposed_bills']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for legislator in legislators.values():
            writer.writerow({
                'id': legislator['id'],
                'name': legislator['name'],
                'num_supported_bills': legislator['supported_bills'],
                'num_opposed_bills': legislator['opposed_bills']
            })

def write_bills_output(bills, legislators):
    """Write bill summary data"""
    # dict lookup for sponsor names
    sponsor_names = {legislator['id']: legislator['name'] for legislator in legislators.values()}
    #print("sponsors: ",sponsor_names) # reminder: currently we only have one known sponsor and one unknown

    with open(BILLS_OUTPUT, 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for bill in bills.values():
            # get sponsor name or "Unknown" if not found
            sponsor_id = bill['sponsor_id']
            sponsor_name = sponsor_names.get(sponsor_id, "Unknown")
            
            writer.writerow({
                'id': bill['id'],
                'title': bill['title'],
                'supporter_count': bill['supporter_count'],
                'opposer_count': bill['opposer_count'],
                'primary_sponsor': sponsor_name
            })

def main():
    """Main function to process data and generate output files in csv format"""
    legislators = load_legislators()
    bills = load_bills()
    votes = load_votes()

    process_vote_results(legislators, bills, votes)
    
    print("Writing output: ")
    write_legislators_output(legislators)
    write_bills_output(bills, legislators)
    
    print(f"Output files created successfully!")

if __name__ == "__main__":
    main()