python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path d.txt \
  --dataset_root_dir ~/Documents/Patch-NetVLAD/patchnetvlad/kiapi \
  --output_features_dir patchnetvlad/output_features/d

  python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path q.txt \
  --dataset_root_dir ~/Documents/Patch-NetVLAD/patchnetvlad/kiapi \
  --output_features_dir patchnetvlad/output_features/q

  python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path q.txt \
  --index_file_path d.txt \
  --query_input_features_dir patchnetvlad/output_features/q \
  --index_input_features_dir patchnetvlad/output_features/d \
  --result_save_folder patchnetvlad/results/kiapi
