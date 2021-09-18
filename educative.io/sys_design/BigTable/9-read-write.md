Write request#

Upon receiving a write request, a Tablet server performs the following set of steps:

    Checks that the request is well-formed.
    Checks that the sender is authorized to perform the mutation. This authorization is performed based on the Access Control Lists (ACLs) that are stored in a chubby file.
    If the above two conditions are met, the mutation is written to the commit-log in GFS that stores redo records.
    Once the mutation is committed to the commit-log, its contents are stored in memory in a sorted buffer called MemTable.
    After inserting the data into the MemTable, acknowledgment is sent to the client that the data has been successfully written.
    Periodically, MemTables are flushed to SSTables, and SSTables are merged during compaction (discussed later).

The anatomy of a write request
Read request#

Upon receiving a read request, a Tablet server performs the following set of steps:

    Checks that the request is well-formed and the sender is authorized
    Returns the rows if they are available in the Cache (discussed later)
    Reads MemTable first to find the required rows
    Reads SSTable indexes that are loaded in memory to find SSTables that will have the required data, then reads the rows from those SSTables
    Merge rows read from MemTable and SSTables to find the required version of the data. Since the SSTables and the MemTable are sorted, the merged view can be formed efficiently.

The anatomy of a read request
