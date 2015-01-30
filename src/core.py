# -*- coding: utf-8 -*-
'''
Created on 2015/1/2

@author: sam
'''

import re
import xlrd
# import docx
from itertools import izip_longest
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.enum.table import WD_TABLE_ALIGNMENT 
from wx import ITEM_CHECK
import lpod
import lpod.document
import lpod.paragraph
import lpod.table
import lpod.style

def itoa(num):
    return str(int(num)) if isinstance(num,(int,long,float)) else num

def parseSheet(sheet):
    parseResult={}
    pDate = re.compile("^(\d{4,4})/(\d{1,2})/(\d{1,2})")
    pId = re.compile("^\d{7,7}$")
    for i in range(0,sheet.nrows):
        m1 = re.match(pDate,sheet.row_values(i)[0])
        if m1 :
            date = "{0:d}/{1:02d}/{2:02d}".format(*map(int,m1.groups()))
            ptlist = parseResult.setdefault(date,[])
        item4 = sheet.row_values(i)[4]
        item5 = sheet.row_values(i)[5]
        id4 = itoa(item4)
        id5 = itoa(item5)
        m4 = re.match(pId,id4)
        m5 = re.match(pId,id5)
        if m4 :
            info = sheet.row_values(i,1)
            ptlist.append(info)
        elif m5:
            info = sheet.row_values(i,1)
            info = info[0:1]+ [info[1]+"\n"+info[2]] + info[3:]
            ptlist.append(info)
    return parseResult

def genCardString(pt):
    if pt:
        s = [pt[0] ]
        s = ( pt[0] + "\n\n"
            + "\n".join(map(itoa ,pt[3:6]))
            + "," + pt[6] + "\n\n"
            + "\n\n".join(map(itoa ,pt[7:]))
            + pt[2] )
    else:
        s = ""
    return s

def writeCell(row,index,pt,style_name):
    cell = row.get_cell(index)
    cell.set_style(style_name["cell"])
    cell.set_text_content("")
    paragraph = cell.get_paragraph()
    paragraph.set_style(style_name["para"])
    paragraph.append_plain_text(genCardString(pt))
    #paragraph.set_style("")
    row.set_cell(index,cell)

def writeRow(table,index,row_info,style_name):
    # row_info: list of pt_info of length 6
    pt_list = row_info
    row = table.get_row(index)
    map(lambda index, pt : writeCell(row,index,pt,style_name), range(6), pt_list)
    table.set_row(index,row)

def addTable(doc,table_info,style_name):
    #table_info: list of pt_info of length 3x6
    body = doc.get_body()
    table = lpod.table.odf_create_table(u"Table1", width=6, height=3)
    #table = doc.add_table(3,6,style="a3")
    #table.autofit=False
    #table.alignment=WD_TABLE_ALIGNMENT.CENTER    
    row_info_iter = izip_longest(*[iter(table_info)]*6,fillvalue=[])
    map(lambda index, row_info: writeRow(table, index, row_info,style_name), range(3), row_info_iter)
    #map(lambda col:col.set_style(style_name["column"]),table.traverse_columns())
    body.append(table)
    

def makeCard(doc,ptlist,style_name):
    table_info_iter = izip_longest(*[iter(ptlist)]*18,fillvalue=[])
    map( lambda table_info: addTable(doc,table_info,style_name) , table_info_iter)

def docsetup(doc):
    section = doc.sections[0]
    section.top_margin = docx.shared.Cm(1)
    section.bottom_margin = docx.shared.Cm(1)
    section.left_margin = docx.shared.Cm(1)
    section.right_margin = docx.shared.Cm(1)
    section.page_width = docx.shared.Cm(21)
    section.page_height = docx.shared.Cm(29.7)

def getptlist(filename,sheetname,datelabel):
    pDate = re.compile("^(\d{4,4})/(\d{1,2})/(\d{1,2})")
    m = re.match(pDate,datelabel)
    date = "{0:4}/{1:02}/{2:02}".format(*map(int,m.groups()))
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name(sheetname)
    parseResult = parseSheet(sheet)
    ptlist = parseResult.get(date,[])
    ptlist = [[datelabel]+x for x in ptlist]
    return ptlist

def addStyle(doc):
    tempdoc = lpod.document.odf_get_document("templates/template.odt")
    style_name={}
#     columnStyle = lpod.style.odf_create_style('table-column',name = u"mycolumn",display_name=u"mycolumn", 
#                                               border="1pt solid #000000",width='5cm')
#     style_name['column']=doc.insert_style(columnStyle, automatic=True)
#     rowStyle = lpod.style.odf_create_style('table-row',name = u'myrow',display_name=u"myrow", 
#                                            border="1pt solid #000000",height='6cm')
#     style_name['row']=doc.insert_style(rowStyle, automatic=True)
    #textStyle=lpod.style.odf_create_style('text',name=u'mytext',display_name=u"mytext")
    #textStyle.s
    #style_name['text']=doc.insert_style(textStyle, automatic=True)
    paraStyle = tempdoc.get_style("paragraph","mypara")
    style_name['para'] = doc.insert_style(paraStyle, automatic=True)
    cell_style = lpod.style.odf_create_table_cell_style(border="0.5pt solid #000000")
    style_name['cell'] = doc.insert_style(style=cell_style, automatic=True)
    return style_name

def main(filenamelist,sheetname,outputfile,datelabel):
    # doc = docx.Document("templates/Doc1.docx")
    doc = lpod.document.odf_new_document('text')
    style_name = addStyle(doc)
    body = doc.get_body()
    paragraph = lpod.paragraph.odf_create_paragraph(datelabel+u" 入院列表", style=style_name['para'])
    #print paragraph.get_text()
    body.append(paragraph)
    #title = lpod.heading.odf_create_heading(1, text=datelabel+u" 入院列表")
    #body.append(title)
    ptlist = sum(map(lambda filename: getptlist(filename,sheetname,datelabel),filenamelist),[])
    makeCard(doc,ptlist,style_name)
    doc.save(outputfile, pretty=True)
    print "success"
    return u"產生清單成功！！"

if __name__ == '__main__':
    main(["../Cath20150102.xls","../Hema20150102.xls","../others20150102.xls"],"201501","../output.odt","2015/1/12(W1)")