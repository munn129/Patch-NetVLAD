python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/0519_front_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/0828_front_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0828

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/0828_front_imagenames.txt \
  --index_file_path icrca/0519_front_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519 \
  --result_save_folder patchnetvlad/results/icrca