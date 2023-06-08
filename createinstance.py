from google.cloud import bigtable
import os
from var import *

from google.cloud.bigtable import Client
from google.cloud.bigtable import enums

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../key.json"

my_instance_id = myfirstinstance
my_cluster_id = "myfirstcluster"
location_id = "us-central1-a"
storage_type = enums.StorageType.SSD
dev = enums.Instance.Type.DEVELOPMENT

client = Client(admin=True)
instance = client.instance(my_instance_id, instance_type=dev)
cluster = instance.cluster(
    my_cluster_id,
    location_id=location_id,
    default_storage_type=storage_type,
)
operation = instance.create(clusters=[cluster])
print("my first bigtable instance")
operation.result(timeout=100)
