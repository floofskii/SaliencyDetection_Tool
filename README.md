# SaliencyDetection_Tool

Saliency Map Generation and Evaluation
This Python script generates and evaluates saliency maps for three input images using OpenCV and Matplotlib. The script leverages the cv2.saliency.StaticSaliencyFineGrained_create() method to compute saliency maps, which highlight the most visually significant regions of an image. The script also calculates and displays the average saliency of each map, along with visualizations for easy comparison.

Key Features:

Saliency Map Generation: Computes fine-grained saliency maps for each input image.

Image Processing: Resizes and converts images for consistency in analysis.

Average Saliency Evaluation: Calculates the average saliency values of the generated maps.

Visualization: Displays the saliency maps with their respective average values using Matplotlib.
