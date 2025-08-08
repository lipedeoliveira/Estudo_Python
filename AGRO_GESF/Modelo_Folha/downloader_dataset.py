from duckduckgo_search import DDGS
import os
import requests
from PIL import Image
from io import BytesIO

output_dir = "not_leaf"
os.makedirs(output_dir, exist_ok=True)

search_terms = [
    "empty desk", "sky", "wooden floor", "plastic bag", "brick wall", "metal surface",
    "random objects", "table", "tools", "books", "keyboard", "street", "abstract background",
    "fabric texture", "kitchen", "bed", "pillow", "mug", "door", "mousepad"
]

max_images_per_term = 10
count = 0

with DDGS() as ddgs:
    for term in search_terms:
        print(f"🔍 Buscando por: {term}")
        results = ddgs.images(term, max_results=max_images_per_term)
        for result in results:
            url = result["image"]
            try:
                response = requests.get(url, timeout=5)
                image = Image.open(BytesIO(response.content)).convert("RGB")
                image = image.resize((128, 128))
                filename = os.path.join(output_dir, f"not_leaf_{count}.jpg")
                image.save(filename)
                count += 1
            except Exception as e:
                print(f"Erro ao baixar {url}: {e}")

print(f"\n✅ Total de imagens salvas: {count}")
