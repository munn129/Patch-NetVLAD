python feature_extract.py \
  --config_path patchnetvlad/configs/cosplace.ini \
  --dataset_file_path oxford/0519_front_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/cosplace/0519 \
  --cosplace True

python feature_extract.py \
  --config_path patchnetvlad/configs/cosplace.ini \
  --dataset_file_path oxford/0828_front_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/cosplace/0828 \
  --cosplace True

python feature_match.py \
  --config_path patchnetvlad/configs/cosplace.ini \
  --dataset_root_dir /home/moon/Documents/Patch-NetVLAD/patchnetvlad \
  --query_file_path oxford/0828_front_imagenames.txt \
  --index_file_path oxford/0519_front_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/cosplace/0828 \
  --index_input_features_dir patchnetvlad/output_features/cosplace/0519 \
  --result_save_folder patchnetvlad/results/cosplace/ox_front \
  --cosplace True