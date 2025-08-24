def calculate_patches(satellite_tensor, patch_size):
    # How many patches fit in each dimension
    patches_h = satellite_tensor.shape[2] // patch_size
    patches_w = satellite_tensor.shape[3] // patch_size
    total_patches = patches_h * patches_w

    # Final tensor patches
    return total_patches