dotdepot = input("Where is depotdownloader located? (absolute path) > ").rstrip("/").rstrip("\\").replace("\\", "/")
version = input("Version to download? (leave blank for list) > ").replace("s", "") + "s"
username = input("Steam username? > ")
password = input("Steam password? > ")
import asyncio
async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')
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
try:
    systemstring = f"dotnet {dotdepot}/DepotDownloader.dll -app {config['appID']} -depot {config['DepotID']} -manifest {config['Version'][version]['manifestId']} -username {username} -password {password}"
except KeyError:
    print(f"Version {version!r} not found")
    raise SystemExit(0)
asyncio.run(run(systemstring))
print("Finished!")
asyncio.run(run(f"explorer ./depots/{config['DepotID']}/"))