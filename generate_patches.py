import torch

def gen_patches_overlapping(satellite_tensor, patch_size, overlap_percent=20):
    # Calculate stride based on overlap percentage
    stride = patch_size - int(patch_size * overlap_percent / 100)
    
    print(f"Patch size: {patch_size}")
    print(f"Overlap: {overlap_percent}%")
    print(f"Stride: {stride} pixels")
    
    channels, height, width = satellite_tensor.shape
    patches = torch.empty((0, channels, patch_size, patch_size))  # To store patches
    positions = torch.empty((0, 2), dtype=torch.int)  # To store (row, col) positions of patches
    
    for row in range(0, height - patch_size + 1, stride):
        for col in range(0, width - patch_size + 1, stride):
            patch = satellite_tensor[:, row:row+patch_size, col:col+patch_size]
            patches = torch.cat((patches, patch.unsqueeze(0)), dim=0)
            positions = torch.cat((positions, torch.tensor([[row, col]])), dim=0)

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