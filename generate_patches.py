import torch

def gen_patches_overlapping(satellite_tensor, patch_size, overlap_percent=20):
    # Calculate stride based on overlap percentage
    stride = patch_size - int(patch_size * overlap_percent / 100)
    
    print(f"Patch size: {patch_size}")
    print(f"Overlap: {overlap_percent}%")
    print(f"Stride: {stride} pixels")
    
    channels, height, width = satellite_tensor.shape
    patches = []
    positions = []
    
    for row in range(0, height - patch_size + 1, stride):
        for col in range(0, width - patch_size + 1, stride):
            patch = satellite_tensor[:, row:row+patch_size, col:col+patch_size]
            patches.append(patch)
            positions.append((row, col))
    
    print(f"Total patches: {len(patches)}")
    return torch.stack(patches), positions

def gen_patches(satellite_tensor, patch_shape):
    # Break the image into smaller patches and create a batch
    patch_batch = torch.empty((1, 4, patch_shape, patch_shape))
    height = 0
    width = 0

    # Generate patches (input is [channels, H, W])
    while height < satellite_tensor.shape[1]:
        while width < satellite_tensor.shape[2]:
            patch = satellite_tensor[:, height:height+128, width:width+128].unsqueeze(0)
            patch_batch = torch.cat((patch_batch, patch), dim=0)
            width += 128
        height += 128
        width = 0

    return patch_batch  # Return a batch