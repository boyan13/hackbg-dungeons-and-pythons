def ascii_image_extract(path):
    image = []
    with open(path, 'r') as f:
        image = [line.replace('\n', '') for line in f]

    return image[:len(image) - 1]  # Last member is empty
