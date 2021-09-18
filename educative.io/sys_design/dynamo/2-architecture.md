High-level Architecture

This lesson gives a brief overview of Dynamo’s architecture.

At a high level, Dynamo is a Distributed Hash Table (DHT) that is replicated across the cluster for high availability and fault tolerance.
Introduction: Dynamo’s architecture#

Dynamo’s architecture can be summarized as follows (we will discuss all of these concepts in detail in the following lessons):
Data distribution#

Dynamo uses Consistent Hashing to distribute its data among nodes. Consistent hashing also makes it easy to add or remove nodes from a Dynamo cluster.
Data replication and consistency#

Data is replicated optimistically, i.e., Dynamo provides eventual consistency.
Handling temporary failures#

To handle temporary failures, Dynamo replicates data to a sloppy quorum of other nodes in the system instead of a strict majority quorum.
Inter-node communication and failure detection#

Dynamo’s nodes use gossip protocol to keep track of the cluster state.
High availability#

Dynamo makes the system “always writeable” (or highly available) by using hinted handoff.
Conflict resolution and handling permanent failures#

Since there are no write-time guarantees that nodes agree on values, Dynamo resolves potential conflicts using other mechanisms:

    Use vector clocks to keep track of value history and reconcile divergent histories at read time.
    In the background, dynamo uses an anti-entropy mechanism like Merkle trees to handle permanent failures.

Let’s discuss each of these concepts one by one.
