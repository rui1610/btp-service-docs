from pathlib import Path, PurePath
import jinja2
import json
import os
import sys
import glob


def renderTemplateWithJson(templateFilename, targetFilename, parameters):

    templateFilenamePurePath = PurePath(str(templateFilename))
    targetFilenamePurePath = PurePath(str(targetFilename))

    templateFolder = templateFilenamePurePath.parent
    templateBasename = templateFilenamePurePath.name

    templateLoader = jinja2.FileSystemLoader(searchpath=str(templateFolder))
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(templateBasename)

    # this is where to put args to the template renderer
    renderedText = template.render(parameters)

    # create folder for target file, if folder not existing
    pathTargetFilename = targetFilenamePurePath.parent
    Path(pathTargetFilename).mkdir(parents=True, exist_ok=True)

    print("- writing " + str(targetFilename))

    with open(str(targetFilename), 'w') as f:
        f.write(renderedText)


def remove_path(entry, skip_files=[]):
    for child in entry.glob('*'):
        if child.is_file():
            if child.stem in skip_files or child.name in skip_files:
                print("skipping", child.name)
            else:
                child.unlink()
        else:
            remove_path(child)

            if not any(Path(entry).iterdir()):
                entry.rmdir()

def getJsonFromFile(fileObj):
    data = None
    foundError = False
    f = None

    filename = str(fileObj)

    try:
        f = open(filename, encoding="utf-8")

        data = json.load(f)
    except IOError:
        message = "Can't open json file >" + filename + "<"
        print(message)
        foundError = True
    except ValueError as err:
        message = "There is an issue in the json file >" + filename + \
            "<. Issue starts on character position " + \
            str(err.pos) + ": " + err.msg
        print(message)
        foundError = True
    finally:
        if f is not None:
            f.close()

    if foundError is True:
        message = "Can't run the use case before the error(s) mentioned above are not fixed"
        print(message)
        sys.exit(os.EX_DATAERR)
    return data


def loadJSONFiles(folder, pattern):
    result = []
    for file in glob.glob(str(folder) + "/" + pattern):
        result.append(getJsonFromFile(file))
    return result
