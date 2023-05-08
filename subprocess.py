import subprocess

res = subprocess.run(["mkdir", "-p", dirname])
if res.returncode != 0:
    raise RuntimeError

res = subprocess.run(["ls"], capture_output=True, text=True)
print('res.stdout', res.stdout) # debug
print('res.stderr', res.stderr) # debug

