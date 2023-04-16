import glob, sys, copy
import asyncio, os

__BANNER__ = """Author : Gameye98
- https://github.com/Gameye98
- https://t.me/deletuserbot
Date   : Sun Apr 16 21:30:59 2023
Purpose: Find file based on the content
Team   :
  - BlackHole Security
	    (https://github.com/BlackHoleSecurity)
  - Schadenfreude
	    (https://t.me/schdenfreude)
"""

async def filecheck(fpath: str, tmatch: str, stdout: int) -> None:
    if os.path.isdir(fpath): return
    with open(fpath,"r") as f:
        try:
            fread = f.read()
        except UnicodeDecodeError:
            return
        flist = [x.strip() for x in fread.split("\n")]
        forig = copy.deepcopy(flist)
        match int(stdout):
            case 1:
                if tmatch in fread:
                    print(f"\x1b[1;92m{fpath}\x1b[0m")
            case 2:
                flist = list(filter(lambda x: tmatch in x, flist))
                list(map(lambda x: print(f"\x1b[1;92m{fpath}({forig.index(x)+1}): \x1b[97m{x}\x1b[0m"), flist))

async def main():
    ls = [filecheck(x, *sys.argv[2:]) for x in glob.iglob("**/*",root_dir=sys.argv[1],recursive=True,include_hidden=True)]
    await asyncio.gather(*ls)

if __name__ == "__main__":
    print(__BANNER__)
    if len(sys.argv) != 4:
        print("Usage: fileseek <PATH> <STRING> <STDOUT>")
        print("STDOUT: 1 = file path, 2 = filepath + content from read per lines")
    else:
        asyncio.run(main())
