from PIL import Image
import numpy as np

def convert_vid_to_gray_scale(vid):
	'''
	Converts a video to gray scale
	:param vid: The video to convert to gray scale
	:return: The gray scale video
	'''
	pass

def convert_img_to_gray_scale(img):
	'''
	Converts an image to gray scale
	:param img: the image to convert to gray scale
	:return: the grayscale image
	'''
	gray_img = img.convert('L')
	return gray_img

def subtract_gray_scale_images(img1, img2):
	'''
	subtract one gray scale image from the other
	:param img1: We're subtracting img2 from this image
	:param img2: We're subtracting this image from img1
	:return: img2 subtracted from img1
	'''
	
