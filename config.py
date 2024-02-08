config = {
    'global_params' : {
        'pooling' : 'patchnetvlad',
        'num_pcs' : '512',
        'patch_sizes' : '5',
        'strides' : '1',
        'weight_file' : './patchnetvlad/pretrained_models/mapillary_WPCA512.pth.tar'
    },
    'feature_extract' : {
        'batchsize' : '5',
        'cachebatchsize' : '5',
        'imageresizew' : '640',
        'imageresizeh' : '480'
    },
    'feature_match' : {
        'patchWeights2Use' : '1',
        'imageresizeW' : '640',
        'imageresizeH' : '480'
    }
}