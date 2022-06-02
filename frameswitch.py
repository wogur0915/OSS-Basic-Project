from function import *
from data import *

# Load Image Files
def load_image():
    global plan0
    global type0
    
    plan0 = PhotoImage(file='src/plan0.png')
    type0 = PhotoImage(file='src/type0.png')

# Statistics Frame Switching
def show_statistics_frame(frame, typeLogo, firstGraph, firstCatagory, firstSum, secondGraph, secondCatagory, secondSum, thirdGraph, thirdCatagory, thirdSum, fourthGraph, fourthCatagory, fourthSum, fifthGraph, fifthCatagory, fifthSum):
    if typeLogoNum == 0:
        typeLogo.config(image=type0, text="0")
    elif typeLogoNum == 1:
        typeLogo.config(image=image, text="1")
    frame.tkraise()
    
# Assets Frame Switching
def show_assets_frame(frame, commentsLogo, assetsSumPrice, assetsPlusPrice, assetsMinusPrice):
    if flagAM:
        assetsPlusPrice.config(text=(str(sumIncomes())+" 원"))
        assetsMinusPrice.config(text=(str(sumExpends())+" 원"))
        assetsSumPrice.config(text=(str(total())+" 원"))
    else:
        assetsPlusPrice.config(text=("1 원"))
        assetsMinusPrice.config(text=("1 원"))
        assetsSumPrice.config(text=("1 원"))
    if commentsLogoNum == 0:
        commentsLogo.config(image=plan0)
    elif commentsLogoNum == 1:
        commentsLogo.config(image=test)
    frame.tkraise()