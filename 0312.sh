python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_1m.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/1024_1m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_3m.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/1024_3m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_5m.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/1024_5m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_7m.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/1024_7m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_10m.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/1024_10m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1114.txt \
  --dataset_root_dir /patchnetvlad_workspace \
  --output_features_dir patchnetvlad/output_features/1114

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1114.txt \
  --index_file_path 1024_1m.txt \
  --query_input_features_dir patchnetvlad/output_features/1114 \
  --index_input_features_dir patchnetvlad/output_features/1024_1m \
  --result_save_folder patchnetvlad/results/1024_1m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1114.txt \
  --index_file_path 1024_3m.txt \
  --query_input_features_dir patchnetvlad/output_features/1114 \
  --index_input_features_dir patchnetvlad/output_features/1024_3m \
  --result_save_folder patchnetvlad/results/1024_3m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1114.txt \
  --index_file_path 1024_5m.txt \
  --query_input_features_dir patchnetvlad/output_features/1114 \
  --index_input_features_dir patchnetvlad/output_features/1024_5m \
  --result_save_folder patchnetvlad/results/1024_5m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1114.txt \
  --index_file_path 1024_7m.txt \
  --query_input_features_dir patchnetvlad/output_features/1114 \
  --index_input_features_dir patchnetvlad/output_features/1024_7m \
  --result_save_folder patchnetvlad/results/1024_7m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 1114.txt \
  --index_file_path 1024_10m.txt \
  --query_input_features_dir patchnetvlad/output_features/1114 \
  --index_input_features_dir patchnetvlad/output_features/1024_10m \
  --result_save_folder patchnetvlad/results/1024_10m