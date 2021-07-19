import sys, re

#opens defined file, reads it's content, removes controlchars and rewrites the file
def findAndDeleteChar(file):
    with open (file, "r") as f:
        content = f.read()
        #print(content) #for the debuggings :D:D:D
    with open (file, "w") as f:
        NewContent = filter_non_printable(content)
        f.write(NewContent)

#removes all non printable charactares from str and returns the new, better string forwards
#in text, to access and modify chars, it is advised to use their ASCII hexacode values
def filter_non_printable(str):
    # exclude tab, and 2 different carridge returns in regex, didnt work but saved if needed later (?!\x0D|\x0A|\x09)
    str = re.sub(r'([\x01-\x08]+)', '', str) #substitute SOH -> BS with empty string
    str = re.sub(r'([\x0B-\x0C]+)', '', str) #substitute VT and FF with empty string
    str = re.sub(r'([\x0E-\x1F]+)', '', str) #substitute SO -> US with empty string

    # at this point, str should be cleaned from non-printable characters.
    return str

#filename requires the operated file to be second in arguments ex. py findSpecialChar.py <FileWhoWeWantToCleanHere>
def main():
    filename = sys.argv[1]
    findAndDeleteChar(filename)
    # add the zip extract and compress if even more laziness https://docs.python.org/3/library/zipfile.html & https://thecodinginterface.com/blog/python-zip-compression-extraction/
if __name__ == '__main__':
    main()
