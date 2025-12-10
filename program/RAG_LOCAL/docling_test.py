from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=PdfPipelineOptions(do_picture_description=False)),
        InputFormat.DOCX: PdfFormatOption(pipeline_options=PdfPipelineOptions(do_picture_description=False)),
        InputFormat.PPTX: PdfFormatOption(pipeline_options=PdfPipelineOptions(do_picture_description=False)),
        InputFormat.MD: PdfFormatOption(pipeline_options=PdfPipelineOptions(do_picture_description=False)),
    }
)

source = "data2/test.pdf"
converter = DocumentConverter()
doc = converter.convert(source).document
print(doc.export_to_markdown())