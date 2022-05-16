
from photoshop import Session
import photoshop.api as ps

app = ps.Application()
app.load(r"E:\CS\automatingps\Template\webinar.psd")


with Session() as ps1:
    doc = ps1.active_document
    title = input()
    title = title.split(" ")
    new_title = ""
    for i in title:
        new_title = new_title + "\n" + i
    new_text_layer = doc.ArtLayers["Title"]
    new_text_layer.kind = ps1.LayerKind.TextLayer
    new_text_layer.textItem.contents = new_title
    ps1.echo(doc.ArtLayers["Speaker Image"])
    doc.activeLayer = doc.ArtLayers["Speaker Image"]
    idplacedLayerReplaceContents = ps1.app.stringIDToTypeID("placedLayerReplaceContents")
    desc = ps1.ActionDescriptor
    idnull = ps1.app.charIDToTypeID("null")
    desc.putPath(idnull, r"C:\Users\Ayush Jain\Downloads\christopher-campbell-rDEOVtE7vOs-unsplash.jpg")
    ps1.app.executeAction(idplacedLayerReplaceContents, desc)