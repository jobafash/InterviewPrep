BigTable provides APIs for two types of operations:

    Metadata operations
    Data operations

Metadata operations#

BigTable provides APIs for creating and deleting tables and column families. It also provides functions for changing cluster, table, and column family metadata, such as access control rights.
Data operations#

Clients can insert, modify, or delete values in BigTable. Clients can also lookup values from individual rows or iterate over a subset of the data in a table.

    BigTable supports single-row transactions, which can be used to perform atomic read-modify-write sequences on data stored under a single row key.
    Bigtable does not support transactions across row keys, but provides a client interface for batch writing across row keys.
    BigTable allows cells to be used as integer counters.
    A set of wrappers allow a BigTable to be used both as an input source and as an output target for MapReduce jobs.
    Clients can also write scripts in Sawzall (a language developed at Google) to instruct server-side data processing (transform, filter, aggregate) prior to the network fetch.

Here are APIs for write operations:

    Set(): write cells in a row
    DeleteCells(): delete cells in a row
    DeleteRow(): delete all cells in a row

A read or scan operation can read arbitrary cells in a BigTable:

    Each row read operation is atomic.
    Can ask for data from just one row, all rows, etc.
    Can restrict returned rows to a particular range.
    Can ask for all columns, just certain columns families, or specific columns.
