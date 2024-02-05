import os
import shutil
import random


def split_images(source_folder, train_folder, validation_folder, test_folder, train_percent=0.7, validation_percent=0.2):
    # the rest 10% are test
    # Create target folders if they don't exist
    for folder in [train_folder, validation_folder, test_folder]:
        os.makedirs(folder, exist_ok=True)

    # List all files in the source folder
    all_images = os.listdir(source_folder)

    # Shuffle the list of images
    random.shuffle(all_images)

    # Calculate the number of images for each category
    total_images = len(all_images)
    train_count = int(total_images * train_percent)
    validation_count = int(total_images * validation_percent)

    # Copy images to the respective folders
    train_images = all_images[:train_count]
    validation_images = all_images[train_count:train_count + validation_count]
    test_images = all_images[train_count + validation_count:]

    for image in train_images:
        shutil.copy(os.path.join(source_folder, image), os.path.join(train_folder, image))

    for image in validation_images:
        shutil.copy(os.path.join(source_folder, image), os.path.join(validation_folder, image))

    for image in test_images:
        shutil.copy(os.path.join(source_folder, image), os.path.join(test_folder, image))


if __name__ == '__main__':
    source_folder = 'data/Dog'

    train_folder = 'data/train/Dog'
    validation_folder = 'data/validation/Dog'
    test_folder = 'data/test/Dog'

    split_images(source_folder, train_folder, validation_folder, test_folder)


# Create 3 directory:
#     1. Train
#     2. Test
#     3. Validation 
# Inside them create folder for each class like: Dog, Cat
# according to this example, this will take the dog images from data/dog and split it into 3 dog folder
