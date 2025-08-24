# Monarchs_PyTorch

# Motivation
-Allow for extremely fast and frequent updates on monarch habitats (and other specie by similar program) to aid conservation and visualize population density

# Initial thoughts
-going to use 'habitat suitability' as opposed to detecing actual indivdual milkweed plants etc. per Wiley Online Library
-Rationale for project is personal passion for protecting and surveying our enviroment through technology, I plant lots of milkweed in my yard and am passionate about monarch conservation as well.

# Display plans
-Graph thats color coded with ranking of most to least suitable

# Struggles
-Handling extremely large image sizes on just my personal machine and particularly vs code
-Finding high res free satellite images that are up to date
-Downloading images using python as opposed to manually (skipped this at this point due to holding up other work)
-Hard to manage HUGE tensors, struggling to handle even one image at a time

# Key Moments
-Used imaging of each band individually to extract the NIR portion of the image. Plants reflect lots of NIR light so they appear distinctly in this band of an image!
-Genereted a NIR image with a key confirming and mapping vegitation density!
-Realized that deep learning is not feasbale and/or not needed, switching to max entropy model

