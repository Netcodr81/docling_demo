from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
import os
import json

source = './pdfs/EventStorming_Cheat_Sheet.pdf'
output = 'converted_to_markdown'
os.makedirs(output, exist_ok=True)  # Create the output directory if it doesn't exist

output_path = os.path.join(output, 'EventStorming_Cheat_Sheet.md')

converter = DocumentConverter()

# Markdown Output
result = converter.convert(source)
with open(output_path, 'w', encoding="utf-8") as f:
    content = result.document.export_to_markdown()
    f.write(content)

# Chunking Output
output = 'converted_to_chunked' # Directory updated for chunked data
os.makedirs(output, exist_ok=True)

doc = result.document
output_path = os.path.join('converted_to_chunked', 'EventStorming_Cheat_Sheet_chunked')

chunker = HybridChunker(tokenizer="BAAI/bge-small-en-v1.5", chunk_size=500, chunk_overlap=100)
chunked_content = chunker.chunk(doc)

chunk_dicts = [chunk.model_dump() for chunk in chunked_content]  

with open("converted_to_chunked/EventStorming_Cheat_Sheet_chunked.json", "w", encoding="utf-8") as f:
    json.dump(chunk_dicts, f, ensure_ascii=False, indent=2)

