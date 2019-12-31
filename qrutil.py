import json
import os
import qrcode



# Encode data into an array of QR codes
def encodeFile(fpath='', chunk_len=4096):
    images = []
    idx = 0

    with open(fpath, 'r') as f:
        data = f.read()

    header = {
        'index': idx,
        'name': os.path.basename(fpath),
        'length': len(data),
        'chunk_len': chunk_len }
    images.append(encodeDict(header))
    idx += 1

    for i in range(0, len(data), chunk_len):
        j = min(i + chunk_len, len(data))
        chunk = { 'index': idx, 'data': data[i:j] }
        images.append(encodeDict(chunk))
        idx += 1

    return images


# Encode a dictionary into QR code (as a JSON string)
def encodeDict(d):
    image = qrcode.make( json.dumps(d) )
    return image


# Export list of QR code images to path (numbered)
def export(images, outdir):
    fmtstr = outdir + '\\' + 'img_{0}.bmp'

    for idx in range(len(images)):
        img = images[idx]
        img.save(fmtstr.format(idx))
