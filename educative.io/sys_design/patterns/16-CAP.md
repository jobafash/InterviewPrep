Background#

In distributed systems, different types of failures can occur, e.g., servers can crash or fail permanently, disks can go bad resulting in data losses, or network connection can be lost, making a part of the system inaccessible. How can a distributed system model itself to get the maximum benefits out of different resources available?
Definition#

CAP theorem states that it is impossible for a distributed system to simultaneously provide all three of the following desirable properties:

Consistency ( C ): All nodes see the same data at the same time. It is equivalent to having a single up-to-date copy of the data.

Availability ( A ): Every request received by a non-failing node in the system must result in a response. Even when severe network failures occur, every request must terminate.

Partition tolerance ( P ): A partition-tolerant system continues to operate despite partial system failure or arbitrary message loss. Such a system can sustain any network failure that does not result in a failure of the entire network. Data is sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages.
Solution#

According to the CAP theorem, any distributed system needs to pick two out of the three properties. The three options are CA, CP, and AP. However, CA is not really a coherent option, as a system that is not partition-tolerant will be forced to give up either Consistency or Availability in the case of a network partition. Therefore, the theorem can really be stated as: In the presence of a network partition, a distributed system must choose either Consistency or Availability.
CAP theorem
Examples#

Dynamo: In CAP theorem terms, Dynamo falls within the category of AP systems and is designed for high availability at the expense of strong consistency. The primary motivation for designing Dynamo as a highly available system was the observation that the availability of a system directly correlates to the number of customers served.

BigTable: In terms of the CAP theorem, BigTable is a CP system, i.e., it has strictly consistent reads and writes.
