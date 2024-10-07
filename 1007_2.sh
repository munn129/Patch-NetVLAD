python feature_extract.py \
  --config_path patchnetvlad/configs/concat.ini \
  --dataset_file_path oxford/0519_concat_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0519_concat

python feature_extract.py \
  --config_path patchnetvlad/configs/front.ini \
  --dataset_file_path oxford/0519_front_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0519_front

python feature_extract.py \
  --config_path patchnetvlad/configs/concat.ini \
  --dataset_file_path oxford/0828_concat_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0828_concat

python feature_extract.py \
  --config_path patchnetvlad/configs/front.ini \
  --dataset_file_path oxford/0828_front_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon_ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0828_front

python feature_match.py \
  --config_path patchnetvlad/configs/concat.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path oxford/0828_concat_imagenames.txt \
  --index_file_path oxford/0519_concat_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/oxford_multiview/0828_concat \
  --index_input_features_dir patchnetvlad/output_features/oxford_multiview/0519_concat \
  --result_save_folder patchnetvlad/results/oxford/concat_q_0828

python feature_match.py \
  --config_path patchnetvlad/configs/front.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path oxford/0828_front_imagenames.txt \
  --index_file_path oxford/0519_front_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/oxford_multiview/0828_front \
  --index_input_features_dir patchnetvlad/output_features/oxford_multiview/0519_front \
  --result_save_folder patchnetvlad/results/oxford/front_q_0828
