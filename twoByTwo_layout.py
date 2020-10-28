# Define custom layouts with 4 3D viewers
twoByTwo = """
  <layout type=\"vertical\" split=\"true\" >
   <item splitSize=\"500\">
     <layout type=\"horizontal\">
       <item>
        <view class=\"vtkMRMLViewNode\" singletontag=\"1\">
         <property name=\"viewlabel\" action=\"default\">1</property>
        </view>
       </item>
       <item>
        <view class=\"vtkMRMLViewNode\" singletontag=\"2\" type=\"secondary\">"
         <property name=\"viewlabel\" action=\"default\">2</property>"
        </view>
      </item>
     </layout>
   </item>
   <item splitSize=\"500\">
    <layout type=\"horizontal\">
         <item>
          <view class=\"vtkMRMLViewNode\" singletontag=\"3\">
           <property name=\"viewlabel\" action=\"default\">3</property>
          </view>
         </item>
         <item>
          <view class=\"vtkMRMLViewNode\" singletontag=\"4\" type=\"secondary\">"
           <property name=\"viewlabel\" action=\"default\">4</property>"
          </view>
        </item>
       </layout>
     </item>
  </layout>
"""

# Register custom layout
twoByTwoLayoutId=601
layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(twoByTwoLayoutId, twoByTwo)
 
# Switch to the new custom layout 
layoutManager.setLayout(twoByTwoLayoutId)
