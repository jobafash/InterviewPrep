HDFS write process#

HDFS write process can be outlined as follows:

    HDFS client initiates a write request by calling the create() method of the Distributed FileSystem object.
    The Distributed FileSystem object sends a file creation request to the NameNode.
    The NameNode verifies that the file does not already exist and that the client has permission to create the file. If both these conditions are verified, the NameNode creates a new file record and sends an acknowledgment.
    The client then proceeds to write the file using FSData OutputStream
    The FSData OutputStream writes data to a local queue called ‘Data Queue.’ The data is kept in the queue until a complete block of data is accumulated.
    Once the queue has a complete block, another component called DataStreamer is notified to manage data transfer to the DataNode.
    DataStreamer first asks the NameNode to allocate a new block on DataNodes, thereby picking desirable DataNodes to be used for replication.
    The NameNode provides a list of blocks and the locations of each block replica.
    Upon receiving the block locations from the NameNode, the DataStreamer starts transferring the blocks from the internal queue to the nearest DataNode.
    Each block is written to the first DataNode, which then pipelines the block to other DataNodes in order to write replicas of the block. This way, the blocks are replicated during the file write itself. It is important to note that HDFS does not acknowledge a write to the client until all the replicas for that block have been written by the DataNodes.
    Once the DataStreamer finishes writing all blocks, it waits for acknowledgments from all the DataNodes.
    Once all acknowledgments are received, the client calls the close() method of the OutputStream.
    Finally, the Distributed FileSystem contacts the NameNode to notify that the file write operation is complete. At this point, the NameNode commits the file creation operation, which makes the file available to be read. If the NameNode dies before this step, the file is lost.
