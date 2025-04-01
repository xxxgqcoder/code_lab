def data_func(params):
    """test func"""
    gcs_data_dir = params.get('gcs_data_dir', None)
    bq_project = params.get('bq_project', None)
    bq_dataset = params.get('bq_dataset', None)
    
    # write your job code here
    import sys
    sys.path.append("dpu-latest.jar")
    from py_dpu import BigqueryManager


    query = """
        select driver_TRANS_ID
        from pypl-edw.pp_scratch.cc_trust_simulation_csv_all_0108_train_oot_result
        limit 1000
    """
    bq_mgr = BigqueryManager(spark)
    bq_mgr.store_query_to_hdfs(query, project=bq_project, dataset=bq_dataset, output_path=gcs_data_dir)

    print(f'successfully saving data to {gcs_data_dir}')
