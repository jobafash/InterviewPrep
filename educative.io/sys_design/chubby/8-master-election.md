Initializing a newly elected master#

A newly elected master proceeds as follows:

    Picks epoch number: It first picks up a new client epoch number to differentiate itself from the previous master. Clients are required to present the epoch number on every call. The master rejects calls from clients using older epoch numbers. This ensures that the new master will not respond to a very old packet that was sent to the previous master.
    Responds to master-location requests but does not respond to session-related operations yet.
    Build in-memory data structures:
        It builds in-memory data structures for sessions and locks that are recorded in the database.
        Session leases are extended to the maximum that the previous master may have been using.
    Let clients perform KeepAlives but no other session-related operations at this point.
    Emits a failover event to each session: This causes clients to flush their caches (because they may have missed invalidations) and warn applications that other events may have been lost.
    Wait: The master waits until each session acknowledges the failover event or lets its session expire.
    Allow all operations to proceed.
    Honor older handles by clients: If a client uses a handle created prior to the failover, the master recreates the in-memory representation of the handle and honors the call.
    Deletes ephemeral files: After some interval (a minute), the master deletes ephemeral files that have no open file handles. Clients should refresh handles on ephemeral files during this interval after a failover.

Chubby events#

Chubby supports a simple event mechanism to let its clients subscribe to a variety of events. Events are delivered to the client asynchronously via callbacks from the Chubby library. Clients subscribe to a range of events while creating a handle. Here are examples of such events:

    File contents modified
    Child node added, removed, or modified
    Chubby master failed over
    A handle (and its lock) has become invalid.
    Lock acquired
    Conflicting lock request from another client

Additionally, the client sends the following session events to the application:

    Jeopardy: When session lease timeout and grace period begins.
    Safe: When a session is known to have survived a communication problem
    Expired: If the session times out
