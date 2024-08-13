python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path debug_data.txt \
  --dataset_root_dir ~/Documents/Patch-NetVLAD/patchnetvlad  \
  --output_features_dir patchnetvlad/output_features/debug

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir ~/Documents/Patch-NetVLAD/patchnetvlad \
  --query_file_path debug_data.txt \
  --index_file_path debug_data.txt \
  --query_input_features_dir patchnetvlad/output_features/debug \
  --index_input_features_dir patchnetvlad/output_features/debug \
  --result_save_folder patchnetvlad/results/debug