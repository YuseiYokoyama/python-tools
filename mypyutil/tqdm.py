from tqdm import tqdm

for c in tqdm(text, desc="[train]"):
    sleep(0.1)

for i, line in enumerate(tqdm(lines)):
    sleep(1)
