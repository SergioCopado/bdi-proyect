# bdi-proyect1
The first proyect of the Big Data Infrastructure subject

# Practice 1: Container-based Infrastructure

1. **Detailed Description** of the infrastructure, justifying its design.

    * Identify and describe the key components of the infrastructure, including the container services to be used.

        - Data Extraction: A Docker container will be used to act as a data extractor. This container will obtain TXT files from the specified source. It will be a script or application that downloads or copies TXT files from the source and stores them locally in the container's file system.

        - Storage System: We can utilize a simple storage system to store the raw files. It can be a local file system within the container or a shared volume mounted in the container.

    * Explain how each component contributes to efficient data management and how they integrate with each other.

2. Brief **guide** to facilitate deployment in any environment.
