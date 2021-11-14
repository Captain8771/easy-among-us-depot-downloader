dotdepot = "./depotdownloader-2.4.5"
version = input("Version to download? (leave blank for list) > ").replace("s", "") + "s"
from os import getcwd, name
import asyncio
async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')
    return (proc, stdout, stderr)
import json
with open("DoNotTouch.json", "r") as f:
    config = json.load(f)['Among Us']
if version == "s":
    e = []
    for key in config['Version']:
        e.append(key)
    e.reverse()
    print("\n".join(e))
    raise SystemExit(0)
username = input("Steam username? > ")
password = input("Steam password? > ")
try:
    systemstring = f"dotnet {dotdepot}/DepotDownloader.dll -app {config['appID']} -depot {config['DepotID']} -manifest {config['Version'][version]['manifestId']} -username {username} -password {password}"
except KeyError:
    print(f"Version {version!r} not found")
    raise SystemExit(0)
p, s, e = asyncio.run(run(systemstring))
if p.returncode == 0:
    print("Finished!")
    if name == "nt":
        asyncio.run(run(f"explorer {getcwd()}\\depots\\{config['DepotID']}"))
else:
    print("Something went wrong!\n", e)
