import time

from matplotlib.style import context
import resources

try:
    import zroya
    oldWin = False
except:
    import win10toast as wToast
    oldWin = True


def useZroya(context):
    resources.UseZroyaPopup(context).ZoraToast()

def useToaster():
    print("Using Toaster")

if __name__ == "__main__":
    context = resources.WordOfTheDay.get_word_of_the_day_details()
    if oldWin == False:
        useZroya(context)
    else:
        useToaster(context)