# from tkinter import *
# from tkinter import filedialog
# from tkinter import messagebox
# import cv2
# import numpy as np
# import PIL.Image
# import PIL.ImageTk
#
# class Editor(Tk):
#
# 	def __init__(self):
# 		Tk.__init__(self)
# 		self.title('Image Editor')
# 		self.resizable(900, 700)
#
# 		self.imageLabel = Label(self)
# 		self.imageLabel.grid(row=0,column=0)
#
# 		# self.openImage('dav.jpg')
#
# 		self.butFrame = Frame(self)
# 		self.butFrame.grid(row=0,column=1)
#
# 		self.buttonQuit			= Button(self.butFrame, 	text='Quit',		 	command=self.quit						).pack(fill=BOTH)
# 		self.buttonOpen			= Button(self.butFrame, 	text='Open image', 		command=self.openImage					).pack(fill=BOTH)
# 		self.buttonRevert		= Button(self.butFrame, 	text='Revert to original',command=self.revertImage				).pack(fill=BOTH)
# 		self.buttonSave			= Button(self.butFrame, 	text='Save image', 		command=self.saveImage					).pack(fill=BOTH)
# 		self.flipLabel 			= Label(self.butFrame)
# 		self.flipLabel.pack()
# 		self.flipText			= Label(self.flipLabel, 	text='Flip:'													).pack(fill=BOTH, side='left')
# 		self.buttonFlipHor 		= Button(self.flipLabel,	text='Horiz',			command=lambda: self.flip('HORIZONTAL')	).pack(fill=BOTH, side='left')
# 		self.buttonFlipVer 		= Button(self.flipLabel,	text='Vert',			command=lambda: self.flip('VERTICAL')	).pack(fill=BOTH, side='right')
# 		self.brightLabel		= Label(self.butFrame)
# 		self.brightLabel.pack()
# 		self.brightText			= Label(self.brightLabel,	text='Brightness:'												).pack(fill=BOTH, side='left')
# 		self.buttonBrightUp		= Button(self.brightLabel,	text='Up',				command=lambda: self.brightness('UP')	).pack(fill=BOTH, side='left')
# 		self.buttonBrightDown	= Button(self.brightLabel,	text='Down',			command=lambda: self.brightness('DOWN')	).pack(fill=BOTH, side='right')
# 		self.contrastLabel		= Label(self.butFrame)
# 		self.contrastLabel.pack()
# 		self.contrastText		= Label(self.contrastLabel, text='Contrast:'												).pack(fill=BOTH, side='left')
# 		self.buttonContrastUp	= Button(self.contrastLabel,text='Up',				command=lambda: self.contrast('UP')		).pack(fill=BOTH, side='left')
# 		self.buttonContrastDown	= Button(self.contrastLabel,text='Down',			command=lambda: self.contrast('DOWN')	).pack(fill=BOTH, side='right')
# 		self.buttonGray 		= Button(self.butFrame, 	text='Grayscale', 		command=self.grayscale 					).pack(fill=BOTH)
# 		self.buttonQuant 		= Button(self.butFrame, 	text='Quantization', 	command=self.quantization 				).pack(fill=BOTH)
# 		self.buttonNeg			= Button(self.butFrame, 	text='Negative',		command=self.negative 					).pack(fill=BOTH)
# 		self.buttonHist			= Button(self.butFrame, 	text='Histogram',		command=self.histogram 					).pack(fill=BOTH)
# 		self.buttonEqualize		= Button(self.butFrame, 	text='Equalize Histo',	command=self.equalizeHistograms			).pack(fill=BOTH)
# 		self.buttonMatch		= Button(self.butFrame, 	text='Match Histos',	command=self.matchHistograms			).pack(fill=BOTH)
# 		self.zoomLabel 			= Label(self.butFrame)
# 		self.zoomLabel.pack()
# 		self.zoomText			= Label(self.zoomLabel, 	text='Zoom:'													).pack(fill=BOTH, side='left')
# 		self.buttonZoomIn		= Button(self.zoomLabel,	text='In ',				command=lambda: self.zoom('IN')			).pack(fill=BOTH, side='left')
# 		self.buttonZoomOut		= Button(self.zoomLabel,	text='Out',				command=lambda: self.zoom('OUT')		).pack(fill=BOTH, side='right')
# 		self.rotateLabel		= Label(self.butFrame)
# 		self.rotateLabel.pack()
# 		self.rotateText			= Label(self.rotateLabel, 	text='Rotate:'													).pack(fill=BOTH, side='left')
# 		self.buttonRotLeft		= Button(self.rotateLabel,	text='Left',			command=lambda: self.rotate('LEFT')		).pack(fill=BOTH, side='left')
# 		self.buttonRotRight		= Button(self.rotateLabel, 	text='Right',			command=lambda: self.rotate('RIGHT')	).pack(fill=BOTH, side='right')
#
# 	def updateLabel(self, img):
# 		tempImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
# 		tempImg = PIL.Image.fromarray(tempImg)
# 		tempImg = PIL.ImageTk.PhotoImage(image=tempImg)
# 		self.imageLabel.configure(image=tempImg)
# 		self.imageLabel.image = tempImg
#
# 	def openImage(self, filename=None):
# 		if filename is None:	# if the filename was not passed as a parameter
# 			try:
# 				filename = filedialog.askopenfilename(initialdir='~/Pictures',title='Open image') #, filetypes=(("image files", "*.jpg"),("all files", "*.*")))
# 			except(OSError, FileNotFoundError):
# 				messagebox.showerror('Error','Unable to find or open file <filename>')
# 			except Exception as error:
# 				messagebox.showerror('Error','An error occurred: <error>')
#
# 		if filename:	# if filename is not an empty string
# 			self.image = cv2.imread(filename)
# 			self.origImage = self.image.copy()
# 			self.updateLabel(self.image)
#
# 	def revertImage(self):
# 		self.image = self.origImage.copy()
# 		self.updateLabel(self.image)
#
# 	def saveImage(self):
# 		try:
# 			filename = filedialog.asksaveasfilename(initialdir='~/Pictures',title='Save image')
# 		except Exception as error:
# 			messagebox.showerror('Error','An error occurred: <error>')
#
# 		if filename:
# 			cv2.imwrite(filename, self.image)
#
# 	def flip(self, option):
# 		h, w, _ = self.image.shape
# 		temp = np.zeros((h,w,3), np.uint8)
# 		if option == 'HORIZONTAL':
# 			for i in range(0,w):
# 				temp[:,i,:] = self.image[:,w-i-1,:]
# 		elif option == 'VERTICAL':
# 			for j in range(0,h):
# 				temp[j,:,:] = self.image[h-j-1,:,:]
# 		self.image = temp
# 		self.updateLabel(self.image)
#
# 	def grayscale(self):
# 		b = self.image[:,:,0]
# 		g = self.image[:,:,1]
# 		r = self.image[:,:,2]
# 		gray = 0.114*b + 0.587*g + 0.299*r
# 		self.image[:,:,0] = self.image[:,:,1] = self.image[:,:,2] = gray
# 		self.updateLabel(self.image)
#
# 	def quantization(self):
# 		pass
#
# 	def brightness(self, option):
# 		if option == 'UP':
# 			bias = 20
# 		elif option == 'DOWN':
# 			bias = -20
# 		self.image = cv2.addWeighted(self.image, 1, np.zeros(self.image.shape, self.image.dtype), 0, bias)
# 		self.updateLabel(self.image)
#
# 	def contrast(self, option):
# 		if option == 'UP':
# 			gain = 1.25
# 		elif option == 'DOWN':
# 			gain = 0.8
# 		self.image = cv2.addWeighted(self.image, gain, np.zeros(self.image.shape, self.image.dtype), 0, 0)
# 		self.updateLabel(self.image)
#
# 	def negative(self):
# 		self.image[:,:,:] = 255 - self.image[:,:,:]
# 		self.updateLabel(self.image)
#
# 	def histogram(self):
# 		pass
#
# 	def equalizeHistograms(self):
# 		pass
#
# 	def matchHistograms(self):
# 		pass
#
# 	def zoom(self, option):
# 		h, w, _ = self.image.shape
# 		if option == 'IN':# and h < 2000 and w < 2000:
# 			temp1 = np.zeros((h,2*w,3), np.uint8)
# 			for i in range(0,w):
# 				temp1[:,2*i,:] = self.image[:,i,:]
# 				temp1[:,2*i+1,:] = self.image[:,i,:]
# 			temp = np.zeros((2*h,2*w,3), np.uint8)
# 			for j in range(0,h):
# 				temp[2*j,:,:] = temp1[j,:,:]
# 				temp[2*j+1,:,:] = temp1[j,:,:]
# 		elif option == 'OUT' and h > 10 and w > 10:
# 			temp1 = np.zeros((h,int(w/2),3), np.uint8)
# 			for i in range(0,int(w/2)):
# 				temp1[:,i,:] = (self.image[:,2*i,:] + self.image[:,2*i+1,:])/2
# 			temp = np.zeros((int(h/2),int(w/2),3), np.uint8)
# 			for j in range(0,int(h/2)):
# 				temp[j,:,:] = (temp1[2*j,:,:] + temp1[2*j+1,:,:])/2
#
# 		self.image = temp
# 		self.updateLabel(self.image)
#
# 	def rotate(self, option):
# 		h, w, _ = self.image.shape
# 		temp = np.zeros((w,h,3), np.uint8) # null image with inverted dimensions
# 		if option == 'LEFT':
# 			for i in range(0,w):
# 				temp[w-i-1,:,:] = self.image[:,i,:]
# 		elif option == 'RIGHT':
# 			for j in range(0,h):
# 				temp[:,h-j-1,:] = self.image[j,:,:]
# 		self.image = temp
# 		self.updateLabel(self.image)
#
# 	def convolutiom(self, kernel):
# 		pass
#
# if __name__ == '__main__':
# 	app = Editor()
# 	app.mainloop()
import os
import tkinter as tk
from tkinter import (ttk, Tk, PhotoImage, Canvas, filedialog, colorchooser, RIDGE,
                     GROOVE, ROUND, Scale, HORIZONTAL)
import cv2
from PIL import ImageTk, Image
import numpy as np


class FrontEnd:
    def __init__(self, master):
        self.master = master
        master.config(bg="#055c57")
        self.menu_initialisation()

    def menu_initialisation(self):
        self.master.geometry('750x630+250+10')
        self.master.title('Photo Editing App with Python (Tkinter and OpenCV)')

        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background='#0a1c2f', foreground='#aaaaaa', width=20, borderwidth=1, focusthickness=3,
                        focuscolor='none', font=('Helvetica', 10))
        style.map('TButton', background=[('active', 'black')])
        style.configure('TFrame', background='#042e3f')

        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        # self.logo = PhotoImage(file='logo1.png').subsample(2, 2)
        # print(self.logo)
        # ttk.Label(self.frame_header, image=self.logo).grid(
        #     row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text='Select and enhance image').grid(
            row=0, column=2, columnspan=1)
        ttk.Label(self.frame_header, text='Teeth Alignment').grid(
            row=1, column=1, columnspan=3)

        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))

        ttk.Button(
            self.frame_menu, text="Upload An Image", command=self.upload_action).grid(
            row=0, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Crop Image", command=self.crop_action).grid(
            row=1, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Adjust Levels", command=self.adjust_action).grid(
            row=6, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Rotate", command=self.rotate_action).grid(
            row=7, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Flip", command=self.flip_action).grid(
            row=8, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Next", command=self.save_action).grid(
            row=9, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        self.canvas = Canvas(self.frame_menu, bg="#054057", width=300, height=400)
        self.canvas.grid(row=0, column=3, rowspan=10)

        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=4, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))

        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()
        self.apply = ttk.Button(self.apply_and_cancel, text="Apply", command=self.apply_action).grid(
            row=0, column=0, columnspan=1, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.apply_and_cancel, text="Cancel", command=self.cancel_action).grid(
            row=0, column=1, columnspan=1, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.apply_and_cancel, text="Revert All Changes", command=self.revert_action).grid(
            row=0, column=2, columnspan=1, padx=5, pady=5, sticky='sw')

    def upload_action(self):
        self.canvas.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)

        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        self.display_image(self.edited_image)

    def text_action_1(self):
        self.text_extracted = "hello"
        self.refresh_side_frame()
        ttk.Label(
            self.side_frame, text="Enter the text").grid(row=0, column=2, padx=5, pady=5, sticky='se')
        self.text_on_image = ttk.Entry(self.side_frame)
        self.text_on_image.grid(row=1, column=2, padx=5, sticky='se')
        ttk.Button(
            self.side_frame, text="Pick A Font Color", command=self.choose_color).grid(
            row=2, column=2, padx=5, pady=5, sticky='se')
        self.text_action()

    def crop_action(self):
        self.rectangle_id = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.canvas.bind("<ButtonPress>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)
        self.canvas.bind("<ButtonRelease>", self.end_crop)

    def start_crop(self, event):
        self.crop_start_x = event.x
        self.crop_start_y = event.y

    def crop(self, event):
        if self.rectangle_id:
            self.canvas.delete(self.rectangle_id)

        self.crop_end_x = event.x
        self.crop_end_y = event.y

        self.rectangle_id = self.canvas.create_rectangle(self.crop_start_x, self.crop_start_y,
                                                         self.crop_end_x, self.crop_end_y, width=1)

    def end_crop(self, event):
        if self.crop_start_x <= self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x <= self.crop_end_x and self.crop_start_y > self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)

        x = slice(start_x, end_x, 1)
        y = slice(start_y, end_y, 1)

        self.filtered_image = self.edited_image[y, x]
        self.display_image(self.filtered_image)

    def text_action(self):
        self.rectangle_id = 0
        # self.ratio = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.canvas.bind("<ButtonPress>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)
        self.canvas.bind("<ButtonRelease>", self.end_text_crop)

    def end_text_crop(self, event):
        if self.crop_start_x <= self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x <= self.crop_end_x and self.crop_start_y > self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)

        if self.text_on_image.get():
            self.text_extracted = self.text_on_image.get()
        start_font = start_x, start_y
        print(self.color_code)  # ((r,g,b),'#ff00000')
        r, g, b = tuple(map(int, self.color_code[0]))

        self.filtered_image = cv2.putText(
            self.edited_image, self.text_extracted, start_font, cv2.FONT_HERSHEY_SIMPLEX, 2, (b, g, r), 5)
        self.display_image(self.filtered_image)

    def draw_action(self):
        self.color_code = ((255, 0, 0), '#ff0000')
        self.refresh_side_frame()
        self.canvas.bind("<ButtonPress>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.draw_color_button = ttk.Button(
            self.side_frame, text="Pick A Color", command=self.choose_color)
        self.draw_color_button.grid(
            row=0, column=2, padx=5, pady=5, sticky='sw')

    def choose_color(self):
        self.color_code = colorchooser.askcolor(title="Choose color")

    def start_draw(self, event):
        self.x = event.x
        self.y = event.y
        self.draw_ids = []

    def draw(self, event):
        print(self.draw_ids)
        self.draw_ids.append(self.canvas.create_line(self.x, self.y, event.x, event.y, width=2,
                                                     fill=self.color_code[-1], capstyle=ROUND, smooth=True))

        cv2.line(self.filtered_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
                 (int(event.x * self.ratio), int(event.y * self.ratio)),
                 (0, 0, 255), thickness=int(self.ratio * 2),
                 lineType=8)

        self.x = event.x
        self.y = event.y

    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass

        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        self.display_image(self.edited_image)
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=4, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))

    def filter_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Negative", command=self.negative_action).grid(
            row=0, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Black And white", command=self.bw_action).grid(
            row=1, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Stylisation", command=self.stylisation_action).grid(
            row=2, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Sketch Effect", command=self.sketch_action).grid(
            row=3, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Emboss", command=self.emb_action).grid(
            row=4, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Sepia", command=self.sepia_action).grid(
            row=5, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Binary Thresholding", command=self.binary_threshold_action).grid(
            row=6, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Erosion", command=self.erosion_action).grid(
            row=7, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Dilation", command=self.dilation_action).grid(
            row=8, column=2, padx=5, pady=5, sticky='se')

    def blur_action(self):
        self.refresh_side_frame()

        ttk.Label(
            self.side_frame, text="Averaging Blur").grid(
            row=0, column=2, padx=5, sticky='sw')

        self.average_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.averaging_action)
        self.average_slider.grid(row=1, column=2, padx=5, sticky='sw')

        ttk.Label(
            self.side_frame, text="Gaussian Blur").grid(row=2, column=2, padx=5, sticky='sw')

        self.gaussian_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.gaussian_action)
        self.gaussian_slider.grid(row=3, column=2, padx=5, sticky='sw')

        ttk.Label(
            self.side_frame, text="Median Blur").grid(row=4, column=2, padx=5, sticky='sw')

        self.median_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.median_action)
        self.median_slider.grid(row=5, column=2, padx=5, sticky='sw')

    def rotate_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Rotate Left", command=self.rotate_left_action).grid(
            row=0, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Rotate Right", command=self.rotate_right_action).grid(
            row=1, column=2, padx=5, pady=5, sticky='sw')

    def flip_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Vertical Flip", command=self.vertical_action).grid(
            row=0, column=2, padx=5, pady=5, sticky='se')

        ttk.Button(
            self.side_frame, text="Horizontal Flip", command=self.horizontal_action).grid(
            row=1, column=2, padx=5, pady=5, sticky='se')

    def adjust_action(self):
        self.refresh_side_frame()
        ttk.Label(
            self.side_frame, text="Brightness").grid(row=0, column=2, padx=5, pady=5,
                                                     sticky='sw')

        self.brightness_slider = Scale(
            self.side_frame, from_=0, to_=2, resolution=0.1, orient=HORIZONTAL,
            command=self.brightness_action)
        self.brightness_slider.grid(row=1, column=2, padx=5, sticky='sw')
        self.brightness_slider.set(1)

        ttk.Label(
            self.side_frame, text="Saturation").grid(row=2, column=2, padx=5,
                                                     pady=5, sticky='sw')
        self.saturation_slider = Scale(
            self.side_frame, from_=-200, to=200, resolution=0.5, orient=HORIZONTAL,
            command=self.saturation_action)
        self.saturation_slider.grid(row=3, column=2, padx=5, sticky='sw')
        self.saturation_slider.set(0)

    def save_action(self):

        original_file_type = self.filename.split('.')[-1]
        # filename = filedialog.asksaveasfilename()
        filename = self.filename
        img_name = "temp_img." + original_file_type

        save_as_image = self.edited_image
        cv2.imwrite(img_name, save_as_image)
        self.filename = filename

        top = tk.Toplevel()
        top.configure(bg="#055c57")
        top.title("Change Smile")
        top.geometry('750x630+250+10')
        top_menu = ttk.Frame(top)
        top_menu.pack()
        top_menu.config(relief=RIDGE, padding=(50, 15))
        ttk.Button(
            top_menu, text="Change Teeth", command=None).grid(
            row=0, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        # ttk.Button(
        #     top_menu, text="Crop Image", command=None).grid(
        #     row=1, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            top_menu, text="Adjust Levels", command=lambda: tadjust_action()).grid(
            row=6, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            top_menu, text="Rotate", command=lambda: trotate_action()).grid(
            row=7, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            top_menu, text="Flip", command=lambda: tflip_action()).grid(
            row=8, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        tcanvas = Canvas(top_menu, bg="#c481ff", width=300, height=400)
        tcanvas.grid(row=0, column=3, rowspan=10)

        tside_frame = ttk.Frame(top_menu)
        tside_frame.grid(row=0, column=4, rowspan=10)
        tside_frame.config(relief=GROOVE, padding=(50, 15))

        tapply_and_cancel = ttk.Frame(top)
        tapply_and_cancel.pack()
        tapply = ttk.Button(tapply_and_cancel, text="Apply", command=lambda: tapply_action()).grid(
            row=0, column=0, columnspan=1, padx=5, pady=5, sticky='sw')

        ttk.Button(
            tapply_and_cancel, text="Cancel", command=lambda: tcancel_action()).grid(
            row=0, column=1, columnspan=1, padx=5, pady=5, sticky='sw')

        ttk.Button(
            tapply_and_cancel, text="Revert All Changes", command=lambda: trevert_action()).grid(
            row=0, column=2, columnspan=1, padx=5, pady=5, sticky='sw')

        def trefresh_side_frame():
            try:
                tside_frame.grid_forget()
            except:
                pass

            tcanvas.unbind("<ButtonPress>")
            tcanvas.unbind("<B1-Motion>")
            tcanvas.unbind("<ButtonRelease>")
            tdisplay_image(self.edited_image)
            tside_frame = ttk.Frame(top_menu)
            tside_frame.grid(row=0, column=4, rowspan=10)
            tside_frame.config(relief=GROOVE, padding=(50, 15))

        def trotate_action():
            self.refresh_side_frame()
            ttk.Button(
                tside_frame, text="Rotate Left", command=trotate_left_action).grid(
                row=0, column=2, padx=5, pady=5, sticky='sw')

            ttk.Button(
                tside_frame, text="Rotate Right", command=trotate_right_action).grid(
                row=1, column=2, padx=5, pady=5, sticky='sw')

        def tflip_action():
            trefresh_side_frame()
            ttk.Button(
                tside_frame, text="Vertical Flip", command=tvertical_action).grid(
                row=0, column=2, padx=5, pady=5, sticky='se')

            ttk.Button(
                tside_frame, text="Horizontal Flip", command=thorizontal_action).grid(
                row=1, column=2, padx=5, pady=5, sticky='se')

        def tadjust_action():
            trefresh_side_frame()
            ttk.Label(
                tside_frame, text="Brightness").grid(row=0, column=2, padx=5, pady=5,
                                                     sticky='sw')

            tbrightness_slider = Scale(
                self.side_frame, from_=0, to_=2, resolution=0.1, orient=HORIZONTAL,
                command=lambda: tbrightness_action())
            tbrightness_slider.grid(row=1, column=2, padx=5, sticky='sw')
            tbrightness_slider.set(1)

            ttk.Label(
                tside_frame, text="Saturation").grid(row=2, column=2, padx=5,
                                                     pady=5, sticky='sw')
            tsaturation_slider = Scale(
                tside_frame, from_=-200, to=200, resolution=0.5, orient=HORIZONTAL,
                command=lambda: tsaturation_action())
            tsaturation_slider.grid(row=3, column=2, padx=5, sticky='sw')
            tsaturation_slider.set(0)

        #         ////////////////////////////////////////////////////////////////

        def tbrightness_action(value):
            self.filtered_image = cv2.convertScaleAbs(
                self.filtered_image, alpha=self.brightness_slider.get())
            tdisplay_image(self.filtered_image)

        def tsaturation_action(event):
            self.filtered_image = cv2.convertScaleAbs(
                self.filtered_image, alpha=1, beta=self.saturation_slider.get())
            tdisplay_image(self.filtered_image)

        def trotate_left_action():
            self.filtered_image = cv2.rotate(
                self.filtered_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            tdisplay_image(self.filtered_image)

        def trotate_right_action():
            self.filtered_image = cv2.rotate(
                self.filtered_image, cv2.ROTATE_90_CLOCKWISE)
            tdisplay_image(self.filtered_image)

        def tvertical_action():
            self.filtered_image = cv2.flip(self.filtered_image, 0)
            tdisplay_image(self.filtered_image)

        def thorizontal_action():
            self.filtered_image = cv2.flip(self.filtered_image, 2)
            tdisplay_image(self.filtered_image)

        def tapply_action():
            self.edited_image = self.filtered_image
            tdisplay_image(self.edited_image)

        def tcancel_action():
            tdisplay_image(self.edited_image)

        def trevert_action():
            self.edited_image = self.original_image.copy()
            tdisplay_image(self.original_image)

        def tdisplay_image(image=None):
            tcanvas.delete("all")
            if self.edited_image is None:
                image = timg.copy()
            else:
                image = timg

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channels = image.shape
            ratio = height / width

            new_width = width
            new_height = height

            if height > 400 or width > 300:
                if ratio < 1:
                    new_width = 300
                    new_height = int(new_width * ratio)
                else:
                    new_height = 400
                    new_width = int(new_height * (width / height))

            self.ratio = height / new_height
            self.new_image = cv2.resize(image, (new_width, new_height))

            self.new_image = ImageTk.PhotoImage(
                Image.fromarray(self.new_image))

            tcanvas.config(width=new_width, height=new_height)
            tcanvas.create_image(
                new_width / 2, new_height / 2, image=self.new_image)




        timg = cv2.imread(img_name)
        tdisplay_image(timg)

        # start from here.
        # Open timg in top window and make a new function that will overlay both images edited and of teeth.




    def top_save_action(self):

        original_file_type = self.filename.split('.')[-1]
        filename = filedialog.asksaveasfilename()
        filename = filename + "." + original_file_type

        save_as_image = self.edited_image
        cv2.imwrite(filename, save_as_image)
        self.filename = filename

    def negative_action(self):
        self.filtered_image = cv2.bitwise_not(self.edited_image)
        self.display_image(self.filtered_image)

    def bw_action(self):
        self.filtered_image = cv2.cvtColor(
            self.edited_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(
            self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.display_image(self.filtered_image)

    def stylisation_action(self):
        self.filtered_image = cv2.stylization(
            self.edited_image, sigma_s=150, sigma_r=0.25)
        self.display_image(self.filtered_image)

    def sketch_action(self):
        ret, self.filtered_image = cv2.pencilSketch(
            self.edited_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
        self.display_image(self.filtered_image)

    def emb_action(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.display_image(self.filtered_image)

    def sepia_action(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])

        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.display_image(self.filtered_image)

    def binary_threshold_action(self):
        ret, self.filtered_image = cv2.threshold(
            self.edited_image, 127, 255, cv2.THRESH_BINARY)
        self.display_image(self.filtered_image)

    def erosion_action(self):
        kernel = np.ones((5, 5), np.uint8)
        self.filtered_image = cv2.erode(
            self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)

    def dilation_action(self):
        kernel = np.ones((5, 5), np.uint8)
        self.filtered_image = cv2.dilate(
            self.edited_image, kernel, iterations=1)
        self.display_image(self.filtered_image)

    def averaging_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.blur(self.edited_image, (value, value))
        self.display_image(self.filtered_image)

    def gaussian_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.GaussianBlur(
            self.edited_image, (value, value), 0)
        self.display_image(self.filtered_image)

    def median_action(self, value):
        value = int(value)
        if value % 2 == 0:
            value += 1
        self.filtered_image = cv2.medianBlur(self.edited_image, value)
        self.display_image(self.filtered_image)

    def brightness_action(self, value):
        self.filtered_image = cv2.convertScaleAbs(
            self.filtered_image, alpha=self.brightness_slider.get())
        self.display_image(self.filtered_image)

    def saturation_action(self, event):
        self.filtered_image = cv2.convertScaleAbs(
            self.filtered_image, alpha=1, beta=self.saturation_slider.get())
        self.display_image(self.filtered_image)

    def rotate_left_action(self):
        self.filtered_image = cv2.rotate(
            self.filtered_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.display_image(self.filtered_image)

    def rotate_right_action(self):
        self.filtered_image = cv2.rotate(
            self.filtered_image, cv2.ROTATE_90_CLOCKWISE)
        self.display_image(self.filtered_image)

    def vertical_action(self):
        self.filtered_image = cv2.flip(self.filtered_image, 0)
        self.display_image(self.filtered_image)

    def horizontal_action(self):
        self.filtered_image = cv2.flip(self.filtered_image, 2)
        self.display_image(self.filtered_image)

    def apply_action(self):
        self.edited_image = self.filtered_image
        self.display_image(self.edited_image)

    def cancel_action(self):
        self.display_image(self.edited_image)

    def revert_action(self):
        self.edited_image = self.original_image.copy()
        self.display_image(self.original_image)

    def display_image(self, image=None):
        self.canvas.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height / width

        new_width = width
        new_height = height

        if height > 400 or width > 300:
            if ratio < 1:
                new_width = 300
                new_height = int(new_width * ratio)
            else:
                new_height = 400
                new_width = int(new_height * (width / height))

        self.ratio = height / new_height
        self.new_image = cv2.resize(image, (new_width, new_height))

        self.new_image = ImageTk.PhotoImage(
            Image.fromarray(self.new_image))

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(
            new_width / 2, new_height / 2, image=self.new_image)

    # def display_image2(self, image=None):



mainWindow = Tk()
FrontEnd(mainWindow)
mainWindow.mainloop() 
