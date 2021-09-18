As described previously, a BigTable cluster consists of three major components:

    A library component that is linked into every client
    One master server
    Many Tablet servers

BigTable architecture
BigTable master server#

There is only one master server in a BigTable cluster, and it is responsible for:

    Assigning Tablets to Tablet servers and ensuring effective load balancing
    Monitoring the status of Tablet servers and managing the joining or failure of Tablet server
    Garbage collection of the underlying files stored in GFS
    Handling metadata operations such as table and column family creations

Bigtable master is not involved in the core task of mapping tablets onto the underlying files in GFS (Tablet servers handle this). This means that Bigtable clients do not have to communicate with the master at all. This design decision significantly reduces the load on the master and the possibility of the master becoming a bottleneck.
Tablet servers#

    Each Tablet server is assigned ownership of a number of Tablets (typically 10–1,000 Tablets per server) by the master.
    Each Tablet server serves read and write requests of the data of the Tablets it is assigned. The client communicates directly with the Tablet servers for reads/writes.
    Tablet servers can be added or removed dynamically from a cluster to accommodate changes in the workloads.
    Tablet creation, deletion, or merging is initiated by the master server, while Tablet partition is handled by Tablet servers who notify the master.
