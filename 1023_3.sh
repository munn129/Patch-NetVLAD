python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_075.txt \
  --index_file_path icrca/imagenames_0519_050.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_075 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_050 \
  --result_save_folder patchnetvlad/results/icrca/075_3

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_100.txt \
  --index_file_path icrca/imagenames_0519_050.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_100 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_050 \
  --result_save_folder patchnetvlad/results/icrca/100_3

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_125.txt \
  --index_file_path icrca/imagenames_0519_050.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_125 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_050 \
  --result_save_folder patchnetvlad/results/icrca/125_3

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_150.txt \
  --index_file_path icrca/imagenames_0519_050.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_150 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_050 \
  --result_save_folder patchnetvlad/results/icrca/150_3