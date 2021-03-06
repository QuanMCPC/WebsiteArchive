# --------------[get_file_info_for_archive.py]-------------- #

import os, json, time, sys, re # Import important stuff
from datetime import date

argument = sys.argv
def log(mes):
    if len(argument) > 1:
        if argument[1] == "--verbose": print(mes)

log("\n========================================\nNow running \"get_file_info_for_archive.py\"\n")
start_path = "." # The path to get metadata
total_size = 0
listing = []
ignored_dir = r"\.git.*|\.github.*"
ignored_file = r"file_listing\.json|index\.html|LICENSE|README\.md|\.gitignore|get_file_info_for_archive\.py"

for path, dirs, files in os.walk(start_path):
    if re.search(ignored_dir, path):
        log("Ignoring: " + path)
        continue
    files.sort()
    for f1 in files:
        if re.search(ignored_file, f1):
            log("Ignoring: " + f1)
            continue
        #f: filename
        f = os.path.join(path, f1)
        fs = os.path.getsize(f) #file size
        mtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(f))) + " (GMT +7)" #Last modification time
        #isdir_ = os.path.isdir(f) #Is it a directory?
        #listing.append({"filename": f1, "filesize": fs, "mod_time": mtime, "isdir": isdir_})
        direc = {"filename": f1, "filesize": fs, "mod_time": mtime}
        log(direc)
        listing.append(direc)

data = {
    "type": "dir_listing",
    "last_updated_on": date.today().strftime("%Y-%m-%d"),
    "list": listing
}
# log(data)
with open(start_path + "/file_listing.json", "w") as outfile: #Dump metadata listing to JSON file
    json.dump(data, outfile, indent=4)

# --------------[get_file_info_for_archive.py]-------------- #