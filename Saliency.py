import cv2
import matplotlib.pyplot as plt
import numpy as np

plt.rc('axes', labelsize=20)
fig = plt.figure(figsize=(40, 40))


def generate_Heat_map(image):    
    saliency_method = cv2.saliency.StaticSaliencyFineGrained_create()
    success, saliency_map = saliency_method.computeSaliency(image)
    return (saliency_map * 255).astype("uint8")

def Load_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (550, 820))
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def evaluate_Saliency(ip1, ip2, ip3):
    images = [Load_image(ip) for ip in [ip1, ip2, ip3]]
    saliency_maps = [generate_Heat_map(image) for image in images]
    means = evaluate_Average(*saliency_maps)
    Generate_Saliency_Maps(saliency_maps, means)

def Generate_Saliency_Maps(saliency_maps, means):
    titles = ['Saliency Map 1', 'Saliency Map 2', 'Saliency Map 3']
    for i, (map, mean) in enumerate(zip(saliency_maps, means), start=1):
        ax = fig.add_subplot(1, 3, i)
        ax.set_title(titles[i-1])
        ax.set_xlabel(f'average is {mean:.2f}', labelpad=20, fontsize=12)
        plt.imshow(np.asarray(cv2.resize(map, (200, 300))))

    plt.subplots_adjust(wspace=0.5)
    plt.show()

def evaluate_Average(one, two, three):
    return np.mean(one), np.mean(two), np.mean(three)

image_path1 = input('Please enter the path to the first image file: ')
image_path2 = input('Please enter the path to the second image file: ')
image_path3 = input('Please enter the path to the third image file: ')

print(image_path1, image_path2, image_path3)
evaluate_Saliency(image_path1, image_path2, image_path3)
