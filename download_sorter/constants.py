### PATHS CONSTANTS
DOWNLOADS_PATH='/Users/mlmg/Downloads'
PICTURES_PATHS='./Sorted downloads/Pictures/'
VIDEOS_PATHS ='./Sorted downloads/Videos/'
ZIP_PATHS='./Sorted downloads/Zip and installers/'
DOCS_PATHS='./Sorted downloads/PDFs/'
DATA_PATHS='./Sorted downloads/Data/'
OTHER_PATHS='./Sorted downloads/Others/'
DIR_PATHS ='./Sorted downloads/Directories/'

### LISTS OF FORMATS (used for sorting)
PICTURES_FORMATS = ['.apng', '.avif', '.gif', '.jpg', '.jpeg', '.png', '.svg', '.webp']
VIDEOS_FORMATS = ['.mp4', '.mov', '.avi']
ZIP_INSTALLERS_FORMATS = ['.zip', '.dmg']
DOCS_PDFS_FORMATS = ['.pdf', '.ppt', '.pages', '.doc', '.docx']
DATA_FORMATS = ['.csv', '.xls', '.xlsx', '.xlsm']

ALL_FORMATS = [PICTURES_FORMATS, VIDEOS_FORMATS, ZIP_INSTALLERS_FORMATS, DOCS_PDFS_FORMATS, DATA_FORMATS]

### LINKING FORMATS AND TARGET FOLDERS 
target_dir = {
    PICTURES_PATHS: PICTURES_FORMATS,
    VIDEOS_PATHS: VIDEOS_FORMATS,
    ZIP_PATHS: ZIP_INSTALLERS_FORMATS,
    DOCS_PATHS:DOCS_PDFS_FORMATS,
    DATA_PATHS:DATA_FORMATS
}
