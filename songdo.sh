python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path songdo1024.txt \
  --dataset_root_dir /patchnetvlad_workspace/songdo1024 \
  --output_features_dir patchnetvlad/output_features/songdo1024_m512

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path songdo1114.txt \
  --dataset_root_dir /patchnetvlad_workspace/songdo1114 \
  --output_features_dir patchnetvlad/output_features/songdo1114_m512

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path songdo1114.txt \
  --index_file_path songdo1024.txt \
  --query_input_features_dir patchnetvlad/output_features/songdo1114_p512 \
  --index_input_features_dir patchnetvlad/output_features/songdo1024_p512 \
  --result_save_folder patchnetvlad/results/songdo_mapi512
