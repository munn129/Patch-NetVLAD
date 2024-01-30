python feature_match.py \
  --config_path patchnetvlad/configs/mapi_128.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path pitts30k_imageNames_query.txt \
  --index_file_path pitts30k_imageNames_index.txt \
  --query_input_features_dir patchnetvlad/output_features/storage_pitts30k_query \
  --index_input_features_dir patchnetvlad/output_features/storage_pitts30k_index \
  --ground_truth_path patchnetvlad/dataset_gt_files/pitts30k_test.npz \
  --result_save_folder patchnetvlad/results/mapi_128

python feature_match.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path pitts30k_imageNames_query.txt \
  --index_file_path pitts30k_imageNames_index.txt \
  --query_input_features_dir patchnetvlad/output_features/speed_pitts30k_query \
  --index_input_features_dir patchnetvlad/output_features/speed_pitts30k_index \
  --ground_truth_path patchnetvlad/dataset_gt_files/pitts30k_test.npz \
	--result_save_folder patchnetvlad/results/mapi_512

python feature_match.py \
  --config_path patchnetvlad/configs/pitts_128.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path pitts30k_imageNames_query.txt \
  --index_file_path pitts30k_imageNames_index.txt \
  --query_input_features_dir patchnetvlad/output_features/pitts128_pitts30k_query \
  --index_input_features_dir patchnetvlad/output_features/pitts128_pitts30k_index \
  --ground_truth_path patchnetvlad/dataset_gt_files/pitts30k_test.npz \
	--result_save_folder patchnetvlad/results/pitts_128

python feature_match.py \
  --config_path patchnetvlad/configs/pitts_512.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path pitts30k_imageNames_query.txt \
  --index_file_path pitts30k_imageNames_index.txt \
  --query_input_features_dir patchnetvlad/output_features/pitts512_pitts30k_query \
  --index_input_features_dir patchnetvlad/output_features/pitts512_pitts30k_index \
  --ground_truth_path patchnetvlad/dataset_gt_files/pitts30k_test.npz \
	--result_save_folder patchnetvlad/results/pitts_512
