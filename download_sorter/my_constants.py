### PATHS CONSTANTS 
### TO COMPLETE
DOWNLOADS_PATH='wherever your downloads folder is'
PICTURES_PATHS='where you want to store your pictures'
VIDEOS_PATHS ='where you want to store your videos'
ZIP_PATHS='where you want to store your zip files'
DOCS_PATHS='where you want to store your documents'
DATA_PATHS='where you want to store your data files'
OTHER_PATHS='where you want to store your other files'
DIR_PATHS ='where you want to store your directories'

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
