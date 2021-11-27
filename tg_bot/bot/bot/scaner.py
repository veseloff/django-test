"""Чтение qr кода"""
import cv2
from pyzbar import pyzbar


def read_qr(filename):
    """
    Чтение qr кода
    Args:
        filename:

    Returns:

    """
    img = cv2.imread(filename)
    data_encode = pyzbar.decode(img)[0]
    data_decode = data_encode.data.decode('utf-8')
    return data_decode
