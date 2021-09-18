Service initialization#

Upon initialization, Chubby performs the following steps:

    A master is chosen among Chubby replicas using Paxos.
    Current master information is persisted in storage, and all replicas become aware of the master.

Client initialization#

Upon initialization, a Chubby client performs the following steps:

    Client contacts the DNS to know the listed Chubby replicas.
    Client calls any Chubby server directly via Remote Procedure Call (RPC).
    If that replica is not the master, it will return the address of the current master.
    Once the master is located, the client maintains a session with it and sends all requests to it until it indicates that it is not the master anymore or stops responding.

Chubby high-level architecture
Leader election example using Chubby#

Let’s take an example of an application that uses Chubby to elect a single master from a bunch of instances of the same application.

Once the master election starts, all candidates attempt to acquire a Chubby lock on a file associated with the election. Whoever acquires the lock first becomes the master. The master writes its identity on the file, so that other processes know who the is current master.
Sample pseudocode for leader election#

The pseudocode below shows how easy it is to add leader election logic to existing applications with just a few additional code lines.

/_ Create these files in Chubby manually once.
Usually there are at least 3-5 required for minimum quorum requirement. _/
lock_file_paths = {
"ls/cell1/foo",
"ls/cell2/foo",
"ls/cell3/foo",
}

Main() {
// Initialize Chubby client library.
chubbyLeader = newChubbyLeader(lock_file_paths)

    // Establish client's connection with Chubby service.
    chubbyLeader.Start()

    // Waiting to become the leader.
    chubbyLeader.Wait()

    // Becomes Leader
    Log("Is Leader: " + chubbyLeader.isLeader ())

    While(chubbyLeader.renewLeader ()) {
        // Do work
    }
    // Not leader anymore.

}
