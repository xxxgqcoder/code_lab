spark_conf = {
    "spark.executor.cores": "4",
    "spark.driver.memory": "16g",
    "spark.executor.instances": "16",
    "spark.dynamicAllocation.minExecutors": "16",
    "spark.shuffle.file.buffer": "64k",
    "spark.reducer.maxSizeInFlight": "96m",
    "spark.driver.maxResultSize": "8g",
    "spark.driver.memoryOverhead": "4096",
    "spark.executor.memoryOverhead": "4096",
    "spark.shuffle.service.enabled": "true",
    "spark.sql.shuffle.partitions": "1000",
    "spark.default.parallelism": "4000",
    "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
    "spark.kryoserializer.buffer.max": "1024m",
    "spark.kryo.registrationRequired": "false",
    "spark.sql.files.ignoreCorruptFiles": "true",
    "spark.hadoop.avro.mapred.ignore.inputs.without.extension": "false",
    "spark.files": "gs://pypl-bkt-rsh-row-std-gds-madmen/madmen/apps/dpu/conf/log4j.properties",
    "spark.driver.extraClassPath": "dpu-latest.jar:spark-bigquery-with-dependencies_2.11-0.23.1.jar",
    "spark.executor.extraClassPath": "dpu-latest.jar:spark-bigquery-with-dependencies_2.11-0.23.1.jar",
}

gcp_jars = [
    "gs://pypl-bkt-rsh-row-std-gds-madmen/madmen/apps/dpu/libs/dpu-latest.jar",
    "gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.11-0.23.1.jar",
    "gs://pypl-bkt-rsh-row-std-gds-art/automation_utils/jars/automation-utils-0.0.1.jar",
]

cluster_pkgs = [
    "onnx==1.8.1",
    "onnxmltools==1.9.1",
    "onnxruntime==1.7.0",
    "tf2onnx==1.9.2",
    "pandas==1.1.5",
    "automation_utils==0.2.0",
    "pyScoring>=0.6.7.3",
    "automation_utils==0.2.0",
    "google-cloud-storage>=1.37.0",
]

cluster_conf = {
    "work_num": "4",
    "cpus_per_worker": "4",
    "mem_per_worker": "16G",
}

dataproc_conf = {
    "spark:spark.driver.memory": "32G",
    "dataproc:dataproc.conscrypt.provider.enable": "false",
}


def get_lib_info(module_list):
    import os

    lib_info = os.popen("pip freeze").read().strip().split("\n")
    lib_dict = {lib.split("==")[0]: lib.split("==")[1] for lib in lib_info if "==" in lib}

    lib_list = []

    for lib_name in module_list:
        if lib_name not in lib_dict:
            print(f"{lib_name} not installed in local environment!")
            continue
        lib_version = lib_dict[lib_name]
        lib_list.append(f"{lib_name}=={lib_version}")

    return lib_list
