import os
import qrcode
import qrtools



# Encode data into an array of QR codes
def encode(path='', chunk_len=4096):
    images = []
    data = loadData(path)
    filename = os.path.basename(path)
    header_data = 'index=0\nname={0}\nlength={1}\nchunk_length={2}'.format(
            filename, len(data), chunk_len )
    header_code = qrcode.make(header_data)
    images.append(header_code)

    index = 1
    for idxA in range(0, len(data), chunk_len):
        idxB = min(data_idx + chunk_len, len(data))
        chunk = data[idxA, idxB]
        img_data = 'index={0}\n{1}'.format(index, chunk)
        img = qrcode.make(img_data)
        images.append(img)
        index += 1

    return images


# Export list of QR code images to path (numbered)
def export(images, path):
    out = path + '\\' + 'img_{0}.bmp'

    for idx in range(len(images)):
        img = images[idx]
        outfile = out.format(idx)
        img.save(outfile)


# Decode a collection of QR code images into raw data
def decode(path):
    data = ''

    for img in os.listdir(path):
        qr = qrtools.QR()
        qr.decode(img)
        data += qr.data

    return data


# Load raw data (no QR encoded yet -- text file etc.)
def loadData(path):
    with open(path, 'r') as data_file:
        return data_file.read()


# Preview an array of QR codes (as a GIF)
def previewQRStream(qr_codes):
    pass
