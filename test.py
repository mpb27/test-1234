import vtk


def main():

    print(vtk.vtkVersion.GetVTKSourceVersion())

    colors = vtk.vtkNamedColors()
    # Set the background color.
    bkg = map(lambda x: x / 255.0, [26, 51, 102, 255])
    colors.SetColor("BkgColor", *bkg)

    # This creates a polygonal cylinder model with eight circumferential
    # facets.
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(32)

    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other
    # attributes are defined.
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it -22.5 degrees.
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
    cylinderActor.RotateX(30.0)
    cylinderActor.RotateY(-45.0)

    # Create the graphics structure. The renderer renders into the render
    # window. The render window interactor captures mouse events and will
    # perform appropriate camera or actor manipulation depending on the
    # nature of the events.
    ren = vtk.vtkRenderer()    
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the actors to the renderer, set the background and size
    ren.AddActor(cylinderActor)
    ren.SetBackground(colors.GetColor3d("BkgColor"))
    renWin.SetSize(800, 600)
    renWin.SetWindowName('CylinderExample')



    # Create the widget
    # https://lorensen.github.io/VTKExamples/site/Python/Widgets/BalloonWidget/
    balloonRep = vtk.vtkBalloonRepresentation()
    balloonRep.SetBalloonLayoutToImageRight()

    balloonWidget = vtk.vtkBalloonWidget()
    balloonWidget.SetInteractor(iren)
    balloonWidget.SetRepresentation(balloonRep)
    balloonWidget.AddBalloon(cylinderActor, "This is a cylinder")
    #balloonWidget.AddBalloon(regularPolygonActor, "This is a regular polygon")
    




    # This allows the interactor to initalize itself. It has to be
    # called before an event loop.
    iren.Initialize()

    # Add axis
    axes = vtk.vtkAxesActor()
    widget = vtk.vtkOrientationMarkerWidget()
    widget.SetOutlineColor( 0.9300, 0.5700, 0.1300 )
    widget.SetOrientationMarker( axes )
    widget.SetInteractor( iren )
    widget.SetViewport( 0.0, 0.0, 0.4, 0.4 )
    widget.SetEnabled( 1 )
    widget.InteractiveOn()

    iren.GetInteractorStyle().SetCurrentStyleToTrackballCamera()


    # We'll zoom in a little by accessing the camera and invoking a "Zoom"
    # method on it.
    ren.ResetCamera()
    ren.GetActiveCamera().Zoom(1.5)
    renWin.Render()

    # balloonWidget.EnabledOn()

    # Info
    print(renWin.GetRenderingBackend())
    print(renWin.ReportCapabilities())

    # Start the event loop.
    iren.Start()


if __name__ == '__main__':
    main()

