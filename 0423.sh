python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 0404_full.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/0404_full

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_1m.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/1024_1m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_5m.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/1024_5m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_10m.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/1024_10m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_15m.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/1024_15m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1024_20m.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/1024_20m

python feature_extract.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path 1114_1m.txt \
  --dataset_root_dir /patchnetvlad_workspace/data  \
  --output_features_dir patchnetvlad/output_features/1114_1m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace/data \
  --query_file_path 0404_full.txt \
  --index_file_path 1024_1m.txt \
  --query_input_features_dir patchnetvlad/output_features/0404_full \
  --index_input_features_dir patchnetvlad/output_features/1024_1m \
  --result_save_folder patchnetvlad/results/1024_1m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 0404_full.txt \
  --index_file_path 1024_5m.txt \
  --query_input_features_dir patchnetvlad/output_features/0404_full \
  --index_input_features_dir patchnetvlad/output_features/1024_5m \
  --result_save_folder patchnetvlad/results/1024_5m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 0404_full.txt \
  --index_file_path 1024_10m.txt \
  --query_input_features_dir patchnetvlad/output_features/0404_full \
  --index_input_features_dir patchnetvlad/output_features/1024_10m \
  --result_save_folder patchnetvlad/results/1024_10m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 0404_full.txt \
  --index_file_path 1024_15m.txt \
  --query_input_features_dir patchnetvlad/output_features/0404_full \
  --index_input_features_dir patchnetvlad/output_features/1024_15m \
  --result_save_folder patchnetvlad/results/1024_15m

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path 0404_full.txt \
  --index_file_path 1024_20m.txt \
  --query_input_features_dir patchnetvlad/output_features/0404_full \
  --index_input_features_dir patchnetvlad/output_features/1024_20m \
  --result_save_folder patchnetvlad/results/1024_20m