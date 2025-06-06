# lazy-durable-function

The goal here is to create an Azure Durable Function that implementes the [Async HTTP Pattern](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=in-process%2Cnodejs-v3%2Cv2-model&pivots=python#async-http).

The long running process will be a call to Lazy GraphRAG to perform an index of files in blob storage.

