System design patterns#

Here is a summary of system design patterns used in Dynamo:

    Consistent Hashing: Dynamo uses Consistent Hashing to distribute its data across nodes.

    Quorum: To ensure data consistency, each Dynamo write operation can be configured to be successful only if the data has been written to at least a quorum of replica nodes.

    Gossip protocol: Dynamo uses gossip protocol that allows each node to keep track of state information about the other nodes in the cluster.

    Hinted Handoff: Dynamo nodes use Hinted Handoff to remember the write operation for failing nodes.

    Read Repair: Dynamo uses ‘Read Repair’ to push the latest version of the data to nodes with the older versions.

    Vector clocks: To reconcile concurrent updates on an object Dynamo uses Vector clocks.

    Merkle trees: For anti-entropy and to resolve conflicts in the background, Dynamo uses Merkle trees.
