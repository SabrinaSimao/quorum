# quorum
 Working with Legislative Data

1. Discuss your solution’s time complexity. What tradeoffs did you make?
O(n), where n is the total number of records in each file.
We read each file once linearly, process each vote once, and then use a lookup dictionary for the legislators/bills/votes (which is O(1))
This solution is fairly simple and straightforward, its a working solution for a dataset this small.
It trades off some more complex libraries for a very easy to read and to understand code.
It doesnt require any external libs like pandas, we simply use csv.
I didn't test it in linux but it should work with the use of os.path
Technically this solution uses dictionaries for all of its data processing, so its keeping the data in memory.
Its good for a faster approach but for a large/huge dataset, we should go with something else (like actually using queries in a database p.e)

2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
Since were using dicts, its fairly simple to add new fields.
I would add them to the functions that capture this data, like load_votes(), after having added date information to the vote schema of course.
For the co-sponsors, it would have to be either a new input file or this information would be on the bills.csv as a "secondary_sponsor" field.
Tehn I simply add the secondary sponsor to the bills dictionary and update the output generation.

3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
simply replace the file reading functions to accept lists instead of csv, the rest should work the same.
If it was a requirement, I could make a function that accepted both formats.

4. How long did you spend working on the assignment?
So, i started looking into this friday,but i got really sick and started taking antibiotics. Only today (sunday) i felt a little better to finish it and commit all on git.
Actually looking at it and coding must have been about 1h, maybe 1h30 counting the time to type and answer the questions.