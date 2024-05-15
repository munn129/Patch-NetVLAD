python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path oxford_151113_filename_list.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/oxford_151113

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path oxford_151110_filename_list.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/oxford_151110

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path oxford_151110_filename_list.txt \
  --index_file_path oxford_151113_filename_list.txt \
  --query_input_features_dir patchnetvlad/output_features/oxford_151110 \
  --index_input_features_dir patchnetvlad/output_features/oxford_151113 \
  --result_save_folder patchnetvlad/results/oxford