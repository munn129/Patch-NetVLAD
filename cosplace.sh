python feature_extract.py \
  --config_path patchnetvlad/configs/cosplace.ini \
  --dataset_file_path cosplace_test.txt \
  --dataset_root_dir /home/moon/Documents/Patch-NetVLAD/patchnetvlad \
  --output_features_dir patchnetvlad/output_features/cosplace/test \
  --cosplace True

python feature_match.py \
  --config_path patchnetvlad/configs/cosplace.ini \
  --dataset_root_dir /home/moon/Documents/Patch-NetVLAD/patchnetvlad \
  --query_file_path cosplace_test.txt \
  --index_file_path cosplace_test.txt \
  --query_input_features_dir patchnetvlad/output_features/cosplace/test \
  --index_input_features_dir patchnetvlad/output_features/cosplace/test \
  --result_save_folder patchnetvlad/results/cosplace/test