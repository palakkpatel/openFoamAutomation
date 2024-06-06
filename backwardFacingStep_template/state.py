# state file generated using paraview version 5.10.0-RC1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview

import sys
sys.path.append("/usr/lib/python3/dist-packages/")

from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1550, 755]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [-0.5080000162124634, 0.05714999884366989, 0.00634999992325902]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.03682399643574315, 0.06606004077861001, 2.0691513024947747]
renderView1.CameraFocalPoint = [0.03682399643574315, 0.06606004077861001, 0.00634999992325902]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.06887872702965271
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1550, 755)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVFoamReader'
# pitzDailySteadyOpenFOAM = PVFoamReader(registrationName='pitzDailySteady.OpenFOAM', FileName='/home/palak/Desktop/openFoam/pitzDailySteady/pitzDailySteady.OpenFOAM')
pitzDailySteadyOpenFOAM = OpenDataFile('para.foam') 
pitzDailySteadyOpenFOAM.add_attribute("MeshParts", ['internalMesh', 'inlet - patch', 'outlet - patch', 'upperWall - wall', 'lowerWall - wall'])
# pitzDailySteadyOpenFOAM.MeshParts = ['internalMesh', 'inlet - patch', 'outlet - patch', 'upperWall - wall', 'lowerWall - wall']
pitzDailySteadyOpenFOAM.add_attribute("Fields", ['p', 'U'])

# create a new 'Gradient'
gradient1 = Gradient(registrationName='Gradient1', Input=pitzDailySteadyOpenFOAM)
gradient1.ScalarArray = ['POINTS', 'U']
gradient1.ComputeVorticity = 1
gradient1.ComputeQCriterion = 1

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=pitzDailySteadyOpenFOAM,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'U']
streamTracer1.MinimumStepLength = 0.002
streamTracer1.MaximumStepLength = 0.05
streamTracer1.MaximumStreamlineLength = 1.0515600061416626

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [0.014569, 0.0, 0.01269999984651804]
streamTracer1.SeedType.Point2 = [0.014569, 0.11429999768733978, 0.01269999984651804]
streamTracer1.SeedType.Resolution = 80

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from gradient1
gradient1Display = Show(gradient1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Vorticity'
vorticityLUT = GetColorTransferFunction('Vorticity')
vorticityLUT.AutomaticRescaleRangeMode = 'Never'
vorticityLUT.RGBPoints = [-5000.0, 0.231373, 0.298039, 0.752941, 0.0, 0.865003, 0.865003, 0.865003, 5000.0, 0.705882, 0.0156863, 0.14902]
vorticityLUT.ScalarRangeInitialized = 1.0
vorticityLUT.VectorComponent = 2
vorticityLUT.VectorMode = 'Component'

# trace defaults for the display properties.
gradient1Display.Representation = 'Surface'
gradient1Display.ColorArrayName = ['POINTS', 'Vorticity']
gradient1Display.LookupTable = vorticityLUT
gradient1Display.Ambient = 0.3
gradient1Display.SelectTCoordArray = 'None'
gradient1Display.SelectNormalArray = 'None'
gradient1Display.SelectTangentArray = 'None'
gradient1Display.OSPRayScaleArray = 'Gradient'
gradient1Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradient1Display.SelectOrientationVectors = 'None'
gradient1Display.ScaleFactor = 0.22860000133514405
gradient1Display.SelectScaleArray = 'None'
gradient1Display.GlyphType = 'Arrow'
gradient1Display.GlyphTableIndexArray = 'Gradient'
gradient1Display.GaussianRadius = 0.011430000066757203
gradient1Display.SetScaleArray = ['POINTS', 'Gradient']
gradient1Display.ScaleTransferFunction = 'PiecewiseFunction'
gradient1Display.OpacityArray = ['POINTS', 'Gradient']
gradient1Display.OpacityTransferFunction = 'PiecewiseFunction'
gradient1Display.DataAxesGrid = 'GridAxesRepresentation'
gradient1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
gradient1Display.ScaleTransferFunction.Points = [-226.22047424316406, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
gradient1Display.OpacityTransferFunction.Points = [-226.22047424316406, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.AmbientColor = [0.0, 0.0, 0.0]
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.DiffuseColor = [0.0, 0.0, 0.0]
streamTracer1Display.LineWidth = 2.0
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 0.2277349054813385
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.011386745274066926
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-4.9967121076252534e-14, 0.0, 0.5, 0.0, 7.179355650241476e-14, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-4.9967121076252534e-14, 0.0, 0.5, 0.0, 7.179355650241476e-14, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for vorticityLUT in view renderView1
vorticityLUTColorBar = GetScalarBar(vorticityLUT, renderView1)
vorticityLUTColorBar.AutoOrient = 0
vorticityLUTColorBar.Orientation = 'Horizontal'
vorticityLUTColorBar.WindowLocation = 'Any Location'
vorticityLUTColorBar.Position = [0.3648387096774194, 0.8741721854304637]
vorticityLUTColorBar.Title = 'Vorticity'
vorticityLUTColorBar.ComponentTitle = 'Z(1/s)'
vorticityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
vorticityLUTColorBar.TitleFontFamily = 'Courier'
vorticityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
vorticityLUTColorBar.LabelFontFamily = 'Courier'
vorticityLUTColorBar.RangeLabelFormat = '%0.f'
vorticityLUTColorBar.ScalarBarLength = 0.19999999999999984

# set color bar visibility
vorticityLUTColorBar.Visibility = 1

# show color legend
gradient1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Vorticity'
vorticityPWF = GetOpacityTransferFunction('Vorticity')
vorticityPWF.Points = [-5000.0, 0.0, 0.5, 0.0, 5000.0, 1.0, 0.5, 0.0]
vorticityPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(gradient1)

animationScene = GetAnimationScene()
animationScene.GoToLast()

# ----------------------------------------------------------------

myview = GetActiveView()
SaveScreenshot("SteadyState_Vorticity_Stream_line.png", myview)

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')