### What is Histogram Equalization?

Histogram Equalization is a technique which basically takes all the intensity values in an image, and rearranges them so that all bins of the histogram are equally used.

Histogram Equalization with **Nonlinear Transformation** Function (Image courtesy of Prof. Cyrill Stachniss)

<img src="https://github.com/YANG-SOBER/Standard_Histogram_Equalization/blob/main/hist_equal_nonlinear.png" width=50% height=50%>

Histogram Equalization with **Linear Transformation** Function (Image courtesy of Prof. Cyrill Stachniss)

<img src="https://github.com/YANG-SOBER/Standard_Histogram_Equalization/blob/main/hist_equal_linear.png" width=50% height=50%>

Histogram Equalization with **Linear Transformation** Function (Image courtesy of Prof. Cyrill Stachniss)

<img src="https://github.com/YANG-SOBER/Standard_Histogram_Equalization/blob/main/hist_equal_reality.png" width=50% height=50%>

For more detail, readers may refer to [Homography Equalization by Prof. Cyrill Stachniss](https://www.ipb.uni-bonn.de/html/teaching/photo12-2021/2021-pho1-04-img-histo-2-transformations.pptx.pdf)

### Effect of Histogram Equalization
1. Typically increases the contrast
2. Areas of lower local contrast gain higher contrast
3. Distributes the intensities over the histogram

### Variants of Histogram Equalization
1. Adaptive Histogram Equalization (AHE) performs histogram equalization in local patches, not the whole image
2. Adaptive Histogram Equalization (AHE) has issues in low contrast regions as it **overamplifies the corrections**
3. Contrast Limited Adaptive Histogram Equalization (CLAHE) limits this over-amplifications in homogeneous regions

### Result (Histogram Equalization with Linear Transformation Function) (courtesy of Prof. Cyrill Stachniss)

<img src="https://github.com/YANG-SOBER/Standard_Histogram_Equalization/blob/main/result/hist_equal_1st_girl.png" width=50% height=50%>

<img src="https://github.com/YANG-SOBER/Standard_Histogram_Equalization/blob/main/result/hist_equal_2nd_girl.png" width=50% height=50%>

<img src="https://github.com/YANG-SOBER/Standard_Histogram_Equalization/blob/main/result/hist_equal_1st_platform.png" width=50% height=50%>

<img src="https://github.com/YANG-SOBER/Standard_Histogram_Equalization/blob/main/result/hist_equal_2nd_platform.png" width=50% height=50%>
