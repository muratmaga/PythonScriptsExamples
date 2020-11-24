# From Andras Lasso
# https://discourse.slicer.org/t/multiple-3d-viewers/14725/6
# Set inputs

# Load a volume (just for this demo, we load a sample data set)
import SampleData
import os
volumeNode = SampleData.SampleDataLogic().downloadCTChest()

# Set output folder and filename
outputScreenshotsFilenamePattern = slicer.app.temporaryPath+"/screenshots/screenshot_%d.png"
outputGalleryFilename = slicer.app.temporaryPath+"/screenshots/gallery.png"

# Set up volume rendering
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
displayNode.SetVisibility(True)
displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName('CT-Chest-Contrast-Enhanced'))

# Set up visualization for screenshots
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
threeDWidget = slicer.app.layoutManager().threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetCamera()
originalZoomFactor = threeDView.zoomFactor
threeDView.zoomFactor = 0.25
threeDView.zoomIn()
threeDView.setZoomFactor(originalZoomFactor)
threeDViewNode = threeDWidget.mrmlViewNode()
threeDViewNode.SetBackgroundColor(0,0,0)
threeDViewNode.SetBackgroundColor2(0,0,0)
threeDViewNode.SetAxisLabelsVisible(False)
threeDViewNode.SetBoxVisible(False)
threeDViewNode.SetOrientationMarkerType(threeDViewNode.OrientationMarkerTypeAxes)

# Create output folders
filedir = os.path.dirname(outputScreenshotsFilenamePattern)
if not os.path.exists(filedir):
    os.makedirs(filedir)

# Capture screenshots
numberOfScreenshots = 6
axisIndex = [0, 2, 4, 1, 3, 5]  # order of views in the gallery image
import ScreenCapture
cap = ScreenCapture.ScreenCaptureLogic()
for screenshotIndex in range(numberOfScreenshots):
    threeDView.rotateToViewAxis(axisIndex[screenshotIndex])
    slicer.util.forceRenderAllViews()
    outputFilename = outputScreenshotsFilenamePattern % screenshotIndex
    cap.captureImageFromView(threeDView, outputFilename)

# Create gallery view of all images
cap.createLightboxImage(3,  # number of columns
    os.path.dirname(outputScreenshotsFilenamePattern),
    os.path.basename(outputScreenshotsFilenamePattern),
    numberOfScreenshots,
    outputGalleryFilename)
