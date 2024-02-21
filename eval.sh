python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_list.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/1024

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1114_list.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/1114

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path rain_full_list.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/rain_full

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path rain_2nd_lane_list.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/rain_2nd_lane

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path rain_3rd_lane_list.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/rain_3rd_lane

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1024_list.txt \
  --index_file_path 1114_list.txt \
  --query_input_features_dir patchnetvlad/output_features/1024 \
  --index_input_features_dir patchnetvlad/output_features/1114 \
  --result_save_folder patchnetvlad/results/1024_1114

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1024_list.txt \
  --index_file_path rain_full_list.txt \
  --query_input_features_dir patchnetvlad/output_features/1024 \
  --index_input_features_dir patchnetvlad/output_features/rain_full \
  --result_save_folder patchnetvlad/results/1024_rain_full

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1024_list.txt \
  --index_file_path rain_2nd_lane_list.txt \
  --query_input_features_dir patchnetvlad/output_features/1024 \
  --index_input_features_dir patchnetvlad/output_features/rain_2nd_lane \
  --result_save_folder patchnetvlad/results/1024_rain_2nd_lane

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1024_list.txt \
  --index_file_path rain_3rd_lane_list.txt \
  --query_input_features_dir patchnetvlad/output_features/1024 \
  --index_input_features_dir patchnetvlad/output_features/rain_3rd_lane \
  --result_save_folder patchnetvlad/results/1024_rain_3rd_lane