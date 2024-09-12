python feature_extract.py \
  --config_path patchnetvlad/configs/concat.ini \
  --dataset_file_path oxford/0514_concat_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0514_concat

python feature_extract.py \
  --config_path patchnetvlad/configs/front.ini \
  --dataset_file_path oxford/0514_front_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0514_front

python feature_extract.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_file_path oxford/0514_left_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0514_left

python feature_extract.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_file_path oxford/0514_rear_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0514_rear

  python feature_extract.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_file_path oxford/0514_right_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0514_right

python feature_extract.py \
  --config_path patchnetvlad/configs/concat.ini \
  --dataset_file_path oxford/0626_concat_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0626_concat

python feature_extract.py \
  --config_path patchnetvlad/configs/front.ini \
  --dataset_file_path oxford/0626_front_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0626_front

python feature_extract.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_file_path oxford/0626_left_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0626_left

python feature_extract.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_file_path oxford/0626_rear_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0626_rear

  python feature_extract.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_file_path oxford/0626_right_imagenames.txt \
  --dataset_root_dir /media/moon/moon_ssd/moon\ ubuntu/post_oxford \
  --output_features_dir patchnetvlad/output_features/oxford_multiview/0626_right

  python feature_match.py \
  --config_path patchnetvlad/configs/concat.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path oxford/0514_concat_imagenames.txt \
  --index_file_path oxford/0626_concat_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/oxford_multiview/0514_concat \
  --index_input_features_dir patchnetvlad/output_features/oxford_multiview/0626_concat \
  --result_save_folder patchnetvlad/results/oxford/concat

  python feature_match.py \
  --config_path patchnetvlad/configs/front.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path oxford/0514_front_imagenames.txt \
  --index_file_path oxford/0626_front_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/oxford_multiview/0514_front \
  --index_input_features_dir patchnetvlad/output_features/oxford_multiview/0626_front \
  --result_save_folder patchnetvlad/results/oxford/front

  python feature_match.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path oxford/0514_right_imagenames.txt \
  --index_file_path oxford/0626_right_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/oxford_multiview/0514_right \
  --index_input_features_dir patchnetvlad/output_features/oxford_multiview/0626_right \
  --result_save_folder patchnetvlad/results/oxford/right

  python feature_match.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path oxford/0514_left_imagenames.txt \
  --index_file_path oxford/0626_left_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/oxford_multiview/0514_left \
  --index_input_features_dir patchnetvlad/output_features/oxford_multiview/0626_left \
  --result_save_folder patchnetvlad/results/oxford/left

  python feature_match.py \
  --config_path patchnetvlad/configs/mono.ini \
  --dataset_root_dir /patchnetvlad_workspace \
  --query_file_path oxford/0514_rear_imagenames.txt \
  --index_file_path oxford/0626_rear_imagenames.txt \
  --query_input_features_dir patchnetvlad/output_features/oxford_multiview/0514_rear \
  --index_input_features_dir patchnetvlad/output_features/oxford_multiview/0626_rear \
  --result_save_folder patchnetvlad/results/oxford/rear
