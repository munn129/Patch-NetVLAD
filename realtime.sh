python realtime.py \
  --config_path patchnetvlad/configs/mapi_512.ini \
  --dataset_file_path webcam.txt \
  --dataset_root_dir ~/Documents/Patch-NetVLAD/patchnetvlad  \
  --output_features_dir patchnetvlad/output_features/webcam  \
  --query_file_path webcam.txt \
  --index_file_path webcam.txt \
  --query_input_features_dir patchnetvlad/output_features/webcam \
  --index_input_features_dir patchnetvlad/output_features/webcam \
  --result_save_folder patchnetvlad/results/webcam