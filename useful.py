import os
import glob

def getAllFiles(path, ext):
    os.chdir(path)
    l = glob.glob('*.{}'.format(ext))
    return l

l = getFile(r'C:\Users\Daniel\Documents\GitHub\StockPortfolio\data', 'csv')
