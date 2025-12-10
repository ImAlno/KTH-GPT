"""
text="Max Emilian Verstappen (Dutch pronunciation: [ˈmɑks fɛrˈstɑpə(n)]; born 30 September 1997) is a Dutch and Belgian racing driver who competes under the Dutch flag in Formula One for Red Bull Racing. Verstappen has won four Formula One World Drivers' Championship titles, which he won consecutively from 2021 to 2024 with Red Bull, and has won 70 Grands Prix across 11 seasons." 
meta=DocMeta(schema_name='docling_core.transforms.chunker.DocMeta', version='1.0.0', doc_items=[DocItem(self_ref='#/texts/0', parent=RefItem(cref='#/body'), children=[], content_layer=<ContentLayer.BODY: 'body'>, meta=None, label=<DocItemLabel.TEXT: 'text'>, prov=[ProvenanceItem(page_no=1, bbox=BoundingBox(l=72.0, t=761.334, r=509.596, b=687.259, coord_origin=<CoordOrigin.BOTTOMLEFT: 'BOTTOMLEFT'>), charspan=(0, 375))])], headings=None, captions=None, origin=DocumentOrigin(mimetype='application/pdf', binary_hash=15723405278806470466, filename='Max Test.pdf', uri=None))
"""
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from transformers import AutoTokenizer

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
MAX_TOKENS = 256

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=PdfPipelineOptions(do_picture_description=False)),
        InputFormat.DOCX: PdfFormatOption(pipeline_options=PdfPipelineOptions(do_picture_description=False)),
        InputFormat.PPTX: PdfFormatOption(pipeline_options=PdfPipelineOptions(do_picture_description=False)),
        InputFormat.MD: PdfFormatOption(pipeline_options=PdfPipelineOptions(do_picture_description=False)),
    }
)

print("Converting document...")
read = converter.convert("data2/Max Test.pdf")
print("Document converted.")

tokenizer = HuggingFaceTokenizer(
    tokenizer=AutoTokenizer.from_pretrained(EMBEDDING_MODEL),
    max_tokens=MAX_TOKENS,  # optional, by default derived from `tokenizer` for HF case
)

chunker = HybridChunker(
    tokenizer=tokenizer,
    merge_peers=True,  # optional, defaults to True
)
chunk_iter = chunker.chunk(dl_doc=read.document)
chunks = list(chunk_iter)
