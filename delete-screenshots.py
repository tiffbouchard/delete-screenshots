import os, time

def find_screenshots():
    os.chdir('/Users/tiffanybouchard/Desktop')
    filenames = [filename for filename in os.listdir() if filename.startswith("Screen Shot")]
    current_time = time.time()
    for f in filenames:
        time_created = os.path.getmtime(f)
        if (current_time - time_created) // (24 * 3600) < 7:
            title = "Check your screenshots"
            message = (f + " may need to be deleted")
            command = f'''
            osascript -e 'display notification "{message}" with title "{title}"'
            '''
            os.system(command)
            print("This screenshot is a week old: " + f)
        if (current_time - time_created) // (24 * 3600) >= 30:
            os.remove(f)

find_screenshots()
