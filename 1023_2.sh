python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_050.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_050

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_075.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_075

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_100.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_100

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_125.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_125

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0519_150.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0519_150

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0828_050.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0828_050

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0828_075.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0828_075

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0828_100.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0828_100

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0828_125.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0828_125

python feature_extract.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_file_path icrca/imagenames_0828_150.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/icrca \
  --output_features_dir patchnetvlad/output_features/icrca/0828_150

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_050.txt \
  --index_file_path icrca/imagenames_0519_050.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_050 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_050 \
  --result_save_folder patchnetvlad/results/icrca/050

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_075.txt \
  --index_file_path icrca/imagenames_0519_075.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_075 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_075 \
  --result_save_folder patchnetvlad/results/icrca/075

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_100.txt \
  --index_file_path icrca/imagenames_0519_100.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_100 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_100 \
  --result_save_folder patchnetvlad/results/icrca/100

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_125.txt \
  --index_file_path icrca/imagenames_0519_125.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_125 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_125 \
  --result_save_folder patchnetvlad/results/icrca/125

python feature_match.py \
  --config_path patchnetvlad/configs/speed.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path icrca/imagenames_0828_150.txt \
  --index_file_path icrca/imagenames_0519_150.txt \
  --query_input_features_dir patchnetvlad/output_features/icrca/0828_150 \
  --index_input_features_dir patchnetvlad/output_features/icrca/0519_150 \
  --result_save_folder patchnetvlad/results/icrca/150