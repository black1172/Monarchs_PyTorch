import torch

def gen_patches_overlapping(satellite_tensor, patch_size, overlap_percent=20):
    
    # Calculate stride
    stride = patch_size - int(patch_size * overlap_percent / 100)
    
    print(f"Patch size: {patch_size}")
    print(f"Overlap: {overlap_percent}%") 
    print(f"Stride: {stride} pixels")
    
    channels, height, width = satellite_tensor.shape
    
    # Pre-calculate number of patches
    rows = list(range(0, height - patch_size + 1, stride))
    cols = list(range(0, width - patch_size + 1, stride))
    total_patches = len(rows) * len(cols)
    
    print(f"Total patches: {total_patches}")
    
    # Pre-allocate tensors (MUCH faster than concatenation)
    patches = torch.empty((total_patches, channels, patch_size, patch_size))
    positions = torch.empty((total_patches, 2), dtype=torch.int)
    
    # Fill pre-allocated tensors
    idx = 0
    for row in rows:
        for col in cols:
            patches[idx] = satellite_tensor[:, row:row+patch_size, col:col+patch_size]
            positions[idx] = torch.tensor([row, col])
            idx += 1

    return patches.clone()

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