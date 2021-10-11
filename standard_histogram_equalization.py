import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Compute img histogram
def compute_hist(img_single):
    h = [0] * 256
    for i in range(img_single.shape[0]):
        for j in range(img_single.shape[1]):
            h[img_single[i, j]] += 1

    return h

# Compute img cumulative histogram
def compute_cumul_hist(h):
    cumul_h = [0] * 256
    for i in range(255):
        cumul_h[i+1] = cumul_h[i] + h[i+1]

    return cumul_h

# Produce x axis
def produce_x_axis():
    x = [0] * 256
    for i in range(256):
        x[i] = i
    return x

# Conduct histogram equalization for single
def hist_equalization(img_in, h, cumul_h):
    height, width = img_in.shape
    num_pixels = height * width
    img_out = np.zeros(img_in.shape, dtype='uint8')

    for i in range(height):
        for j in range(width):
            img_out[i, j] = 255 * (cumul_h[img_in[i, j]] - cumul_h[0]) / (num_pixels - cumul_h[0])
            img_out[i, j] = round(img_out[i, j])

    return img_out

# Plot img histogram and img cumulative histogram for rgb channels
def plot_rgb_hist(img):
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(48, 8))
    x = produce_x_axis()
    color_list = ['red', 'green', 'blue']
    img_equa = []
    axs[0].imshow(img)
    axs[0].set_axis_off()
    axs[0].set_title('Input Image')

    for i in range(img.shape[2]):
        h = compute_hist(img[:, :, i])
        cumul_h = compute_cumul_hist(h)
        img_single_equa = hist_equalization(img[:, :, i], h, cumul_h)
        img_equa.append(img_single_equa)

        axs[1].plot(x, h, color=color_list[i], label=color_list[i].capitalize() + ' Channel')
        axs[1].set_xlabel('Intensity Values')
        axs[1].set_ylabel('Occurrences')
        axs[1].set_title('Image Histogram')
        axs[1].legend()

        axs[2].plot(x, cumul_h, color=color_list[i], label=color_list[i].capitalize() + ' Channel')
        axs[2].set_xlabel('Intensity Values')
        axs[2].set_ylabel('Occurrences')
        axs[2].set_title('Image Histogram')
        axs[2].legend()

    img_out = np.dstack((img_equa[0], img_equa[1], img_equa[2]))
    print(img_out)
    axs[3].imshow(img_out)
    axs[3].set_axis_off()
    axs[3].set_title('Output Image')
    plt.show()
    return img_out

if __name__ == '__main__':
    img_path = 'girl.jpg'
    img = np.array(Image.open(img_path), dtype='uint8')
    img_out = plot_rgb_hist(img)
    plot_rgb_hist(img_out)
