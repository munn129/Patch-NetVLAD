python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path d_front_names.txt \
  --dataset_root_dir ~/Documents/hd_db \
  --output_features_dir patchnetvlad/output_features/hd_db/front

  python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path q_front_names.txt \
  --dataset_root_dir ~/Documents/hd_q \
  --output_features_dir patchnetvlad/output_features/hd_q/front

  python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path q_front_names.txt \
  --index_file_path d_front_names.txt \
  --query_input_features_dir patchnetvlad/output_features/hd_q/front \
  --index_input_features_dir patchnetvlad/output_features/hd_db/front \
  --result_save_folder patchnetvlad/results/hd_tmp
