# -*- coding: utf-8 -*-
'''
Created on 2017. 9. 20.
@author: HyechurnJang
'''

#===============================================================================
# Import Basic Tags
#===============================================================================
from page import TAG
from page import DIV, SPAN, ROW, COL, IFRAME, NAV, SCRIPT
from page import HEAD, PARA, ANCH, LABEL, STRONG, SMALL
from page import IMG, ICON
from page import THEAD, TBODY, TH, TR, TD, TABLE
from page import UL, LI
from page import FORM, INPUT, BUTTON

#===============================================================================
# Grid Widgets
#===============================================================================
class GRID:
    
    class WIDGET(DIV):
    
        def __init__(self, width, height, x=0, y=0, auto=False, **attrs):
            DIV.__init__(self,
                         CLASS='grid-stack-item',
                         **{'data-gs-x' : str(x),
                            'data-gs-y' : str(y),
                            'data-gs-auto-position' : '1' if auto else '0',
                            'data-gs-width' : str(width),
                            'data-gs-height' : str(height)})
            self.content = DIV(**TAG.ATTR(attrs, CLASS='grid-stack-item-content'))
            self['elems'].append(self.content)
        
        def html(self, *elems):
            self.content.html(*elems)
            return self
    
    class DESK(DIV):
        
        def __init__(self, height=100, **attrs):
            DIV.__init__(self, **TAG.ATTR(attrs, STYLE='padding:5px 0px 5px 0px;'))
            self.uuid = TAG.UUID()
            self.grid = DIV(ID=self.uuid, CLASS='grid-stack')
            self['elems'].append(self.grid)
            self['elems'].append(SCRIPT(TYPE='text/javascript').html('$(function(){$("#%s").gridstack({animate:true,cellHeight:%d,verticalMargin:10,removable:".grid-trash-area",removeTimeout:100,acceptWidgets:".grid-stack-item"});});' % (self.uuid, height)))
        
        def html(self, *elems):
            for elem in elems:
                if isinstance(elem, GRID.WIDGET): self.grid.html(elem)
            return self
    
    class TRASH(DIV):
        
        def __init__(self, **attrs):
            DIV.__init__(self, **TAG.ATTR(attrs, CLASS='grid-trash-area'))
    
    @classmethod
    def set(cls, page):
        page.addCSS('/extag/resource/css/gridstack.css')
        page.addCSS('/extag/resource/css/gridstack-extra.css')
        page.addJS('/extag/resource/js/lodash.js')
        page.addJS('/extag/resource/js/jquery-ui.min.js')
        page.addJS('/extag/resource/js/gridstack.min.js')
        page.addJS('/extag/resource/js/gridstack.jQueryUI.min.js')