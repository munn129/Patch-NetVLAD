python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_200.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_200

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_300.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_300

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_400.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_400

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_500.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_500

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_050.txt \
  --index_file_path icrca/imagenames_0519_200.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_050 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_200 \
  --result_save_folder patchnetvlad/results/icrca/200

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_050.txt \
  --index_file_path icrca/imagenames_0519_300.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_050 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_300 \
  --result_save_folder patchnetvlad/results/icrca/300

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_050.txt \
  --index_file_path icrca/imagenames_0519_400.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_050 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_400 \
  --result_save_folder patchnetvlad/results/icrca/400

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_050.txt \
  --index_file_path icrca/imagenames_0519_500.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_050 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_500 \
  --result_save_folder patchnetvlad/results/icrca/500