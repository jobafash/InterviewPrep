GFS#

GFS is a scalable distributed file system developed by Google for its large data-intensive applications such as BigTable.

    GFS files are broken into fixed-size blocks, called Chunks.
    Chunks are stored on data servers called ChunkServers.
    GFS master manages the metadata.
    SSTables are divided into fixed-size, blocks and these blocks are stored on ChunkServers.
    Each chunk in GFS is replicated across multiple ChunkServers for reliability.
    Clients interact with the GFS master for metadata, but all data transfers happen directly between the client and ChunkServers.

High-level architecture of GFS

For a detailed discussion, please see GFS.
Chubby#

Chubby is a highly available and persistent distributed locking service that allows a multi-thousand node Bigtable cluster to stay coordinated.

    Chubby usually runs with five active replicas, one of which is elected as the master to serve requests. To remain alive, a majority of Chubby replicas must be running.
    BigTable depends on Chubby so much that if Chubby is unavailable for an extended period of time, BigTable will also become unavailable.
    Chubby uses the Paxos algorithm to keep its replicas consistent in the face of failure.
    Chubby provides a namespace consisting of files and directories. Each file or directory can be used as a lock.
    Read and write access to a Chubby file is atomic.
    Each Chubby client maintains a session with a Chubby service. A client’s session expires if it is unable to renew its session lease within the lease expiration time. When a client’s session expires, it loses any locks and open handles. Chubby clients can also register callbacks on Chubby files and directories for notification of changes or session expiration.
    In BigTable, Chubby is used to:
        Ensure there is only one active master. The master maintains a session lease with Chubby and periodically renews it to retain the status of the master.
        Store the bootstrap location of BigTable data (discussed later)
        Discover new Tablet servers as well as the failure of existing ones
        Store BigTable schema information (the column family information for each table)
        Store Access Control Lists (ACLs)

High-level architecture of Chubby
